import csv
from pathlib import Path

import numpy as np
import xarray as xr
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.gridspec import GridSpec
from matplotlib.backends.backend_pdf import PdfPages

mpl.style.use("ggplot")


class AnalyseRos2Test:
    """Create dataset from raw data.

    Parameters
    ----------
    data_dir: str or pathlib.Path
        Directory where the data is stored.

    Attributes
    ----------
    data: dict of xarray.Dataset
        Formatted data of all measurements.

    Examples
    --------
    >>> path = Path('path/to/data')
    >>> art = AnalyseRos2Test(path)
    >>> art.data
    {'cputemp': <xarray.Dataset> Dimensions: (core: 3, index: 7, measurement: 4) ...
    """

    def __init__(self, data_dir):
        self.paths = Path(data_dir).iterdir()
        self._data = self.format_data()
        self.reformat_cputemp_data()

    @property
    def data(self):
        return self._data

    def format_data(self):
        """Combine data from multiple files."""
        data_list = []
        for path in self.paths:
            if path.suffix != ".csv":
                continue
            data_list.append(self.read_data(path))
        measurement_types = np.unique([dat.Type for dat in data_list])
        data = {m_type: [] for m_type in measurement_types}
        for dat in data_list:
            m_type = str(dat.Type)
            data[m_type].append(dat)
        for m_type in measurement_types:
            if len(data[m_type]) == 1:
                data[m_type] = data[m_type][0]
            else:
                data[m_type] = xr.concat(
                    data[m_type], join="outer", dim="measurement"
                ).sortby("NodesPerGroup")
        return data

    @staticmethod
    def read_data(path):
        """Format data in single file to Dataset."""

        def path2mode():
            measurement_type = "".join(path.stem.split("_")[:-2])
            config = path.stem.split("_")[-2:]
            nodes_per_group = int(config[0][1:4])
            num_of_groups = int(config[0][5:8])
            shift = int(config[1][1:])
            params = {
                "coords": {
                    "NodesPerGroup": nodes_per_group,
                    "NumOfGroups": num_of_groups,
                },
                "attrs": {"Type": measurement_type, "Shift": shift},
            }
            return params

        with open(path, newline="") as csvfile:
            content = csv.DictReader(csvfile)
            fields = content.fieldnames
            data = {name: [] for name in fields}
            for row in content:
                [data[name].append(eval(row[name])) for name in fields]
        for name in fields:
            data[name] = xr.DataArray(
                data[name],
                dims=["index"],
                coords={"index": np.arange(len(data[name]))},
            )
        params = path2mode()
        data_array = xr.Dataset(
            data, coords=params["coords"], attrs=params["attrs"]
        ).assign_coords({"measurement": path.stem})
        return data_array

    def reformat_cputemp_data(self):
        """Fix irregularly formatted data."""
        try:
            cpuTemp = {}
            labels = self._data["cputemp"].groupby("label")._unique_coord.values
            for label in labels:
                cpuTemp[label] = self._data["cputemp"].where(
                    self._data["cputemp"].label == label, drop=True
                )
                cpuTemp[label] = (
                    cpuTemp[label]
                    .assign_coords(
                        {
                            "m_index": ("index", np.arange(len(cpuTemp[label].index))),
                            "core": label,
                        }
                    )
                    .swap_dims({"index": "m_index"})
                )
            self._data["cputemp"] = (
                xr.concat(cpuTemp.values(), dim="core")
                .reset_coords(["label", "index"], drop=True)
                .rename({"m_index": "index"})
            )
        except KeyError:  # this data cannot be taken in some OS
            pass
        return


class Ros2TestFigure:

    PCOLOR_KWARGS = dict(cmap="viridis", vmax=100, vmin=0)
    MEASUREMENT_LABEL_KWARGS = dict(x=1, y=1, ha="right", va="bottom")

    def draw_figure(self, data):
        num_threads = len(data["cpuusage"])
        try:
            num_cores_p1 = len(data["cputemp"].core)
        except KeyError:
            num_cores_p1 = 1

        fig = plt.figure(figsize=(12, 7.5))

        gs = GridSpec(
            nrows=5, ncols=1, height_ratios=[num_threads, num_cores_p1, 1, 3, 3]
        )
        data_type = ["CpuUsage", "CpuTemp", "MemUsage", "NetCount", "Delay"]
        axes = {d_type: fig.add_subplot(spec) for d_type, spec in zip(data_type, gs)}
        [ax.set_title(title, loc="left") for title, ax in axes.items()]

        _, cpuusage = self.draw_cpuusage(data["cpuusage"].squeeze(), axes["CpuUsage"])
        try:
            self.draw_cputemp(data["cputemp"].squeeze(), axes["CpuTemp"])
        except KeyError:
            self.draw_empty(axes["CpuTemp"])
        self.draw_memusage(data["memusage"].squeeze(), axes["MemUsage"])
        _, netcount = self.draw_netcount(data["netcount"].squeeze(), axes["NetCount"])
        _, delay = self.draw_delay(data["delay"].squeeze(), axes["Delay"])

        plt.tight_layout()

        fig.colorbar(
            cpuusage,
            ax=[axes["CpuUsage"], axes["CpuTemp"], axes["MemUsage"]],
            fraction=0.1,
            pad=0.02,
            label="CPU usage [%]\n"
            "CPU temperature [$^\\circ\\mathrm{{C}}$]\n"
            "Memory usage [%]",
        )
        cbar_kwargs = dict(fraction=0.1, pad=0.02, aspect=5)
        fig.colorbar(
            netcount, ax=axes["NetCount"], **cbar_kwargs, label="Net count [bytes]"
        )
        fig.colorbar(delay, ax=axes["Delay"], **cbar_kwargs, label="Delay [ms]")
        return fig, axes

    @staticmethod
    def draw_empty(ax):
        """Fill a space for certain IF which data isn't available.

        Parameters
        ----------
        ax: matplotlib.axes._subplots.AxesSubplot [optional]
            Axis to fill.
        """
        ax.text(
            0.5,
            0.5,
            "No data",
            fontsize=25,
            ha="center",
            va="center",
            transform=ax.transAxes,
        )
        return ax

    @classmethod
    def draw_cpuusage(cls, data, ax=None):
        if ax is None:
            fig, ax = plt.subplots(1, 1)
        cpuusage = ax.pcolorfast(
            [dat.data for dat in data.values()], **cls.PCOLOR_KWARGS
        )
        num_threads = len(data)
        ax.set(
            xlabel="",
            ylabel="",
            yticks=np.arange(num_threads) + 0.5,
            yticklabels=data.keys(),
        )
        ax.text(
            s=data.measurement.data,
            transform=ax.transAxes,
            **cls.MEASUREMENT_LABEL_KWARGS,
        )
        ax.grid()
        return (ax, cpuusage)

    @classmethod
    def draw_cputemp(cls, data, ax=None):
        if ax is None:
            fig, ax = plt.subplots(1, 1)
        cputemp = ax.pcolorfast(data.current, **cls.PCOLOR_KWARGS)
        num_cores_p1 = len(data.core)
        ax.set(
            xlabel="",
            ylabel="",
            yticks=np.arange(num_cores_p1) + 0.5,
            yticklabels=data.core.data,
        )
        ax.text(
            s=data.measurement.data,
            transform=ax.transAxes,
            **cls.MEASUREMENT_LABEL_KWARGS,
        )
        ax.axhline(num_cores_p1 - 1, c="k")
        ax.grid()
        return (ax, cputemp)

    @classmethod
    def draw_memusage(cls, data, ax=None):
        if ax is None:
            fig, ax = plt.subplots(1, 1)
        memusage = ax.pcolorfast([data.percent], **cls.PCOLOR_KWARGS)
        ax.set(xlabel="", ylabel="", yticks=[], yticklabels=[])
        ax.text(
            s=data.measurement.data,
            transform=ax.transAxes,
            **cls.MEASUREMENT_LABEL_KWARGS,
        )
        ax.grid()
        return (ax, memusage)

    @classmethod
    def draw_netcount(cls, data, ax=None):
        if ax is None:
            fig, ax = plt.subplots(1, 1)
        netcount = ax.pcolormesh(
            # this data can contain 0, so increment by 1 to plot in log scale
            [1 + data.bytes_sent.diff("index"), 1 + data.bytes_recv.diff("index")],
            cmap="viridis",
            norm=LogNorm(vmin=1, vmax=1e8),
        )
        ax.set(
            xlabel="",
            ylabel="",
            yticks=np.arange(2) + 0.5,
            yticklabels=["bytes_sent", "bytes_recv"],
        )
        ax.text(
            s=data.measurement.data,
            transform=ax.transAxes,
            **cls.MEASUREMENT_LABEL_KWARGS,
        )
        return (ax, netcount)

    @classmethod
    def draw_delay(cls, data, ax=None):
        if ax is None:
            fig, ax = plt.subplots(1, 1)
        delay = ax.pcolormesh(
            [1000 * data.delay],  # to milli-second
            cmap="viridis",
            norm=LogNorm(vmin=5e-1, vmax=1e1),
        )
        ax.set(xlabel="index (time series)", ylabel="", yticks=[], yticklabels=[])
        ax.text(
            s=data.measurement.data,
            transform=ax.transAxes,
            **cls.MEASUREMENT_LABEL_KWARGS,
        )
        return (ax, delay)


def draw_figure(data_dir, save=False):
    """
    Parameters
    ----------
    data_dir: str or pathlib.Path
        Directory where the data is stored.
    save: bool, str or pathlib.Path
        Directory in which the figure to be saved. If ``True``,
        the figure will be saved in the current directory.
    """
    if save is True:
        save = Path("./results/")
    if save:
        test_date = "".join(Path(data_dir).stem.split("_")[-2:])

        filename = (
            (Path(save) / f"ros2_test_result_{test_date}")
            .with_suffix(".pdf")
            .absolute()
        )

    data = AnalyseRos2Test(data_dir).data

    if (np.unique([dat.measurement.size for dat in data.values()]) == 1).all():
        Ros2TestFigure().draw_figure(data)
        if save:
            plt.savefig(filename)
            return filename
    elif save:
        pdf_file = PdfPages(filename)
        for NumOfGroups in data["cpuusage"].NumOfGroups:
            Ros2TestFigure().draw_figure(
                {
                    d_type: dat.where(dat.NumOfGroups == NumOfGroups, drop=True)
                    for d_type, dat in data.items()
                }
            )  # if multiple measurements have been done
            pdf_file.savefig()
        pdf_file.close()
        return filename
    else:
        for NumOfGroups in data["cpuusage"].NumOfGroups:
            Ros2TestFigure().draw_figure(
                {
                    d_type: dat.where(dat.NumOfGroups == NumOfGroups, drop=True)
                    for d_type, dat in data.items()
                }
            )  # if multiple measurements have been done
    return
