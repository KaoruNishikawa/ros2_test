#!/usr/bin/env python3

import time
import psutil
import os


def main():
    with open(f"{os.environ['HOME']}/Documents/netcount.txt", 'w') as f:
        for i in range(50):
            netcount = psutil.net_io_counters()
            sent = netcount.bytes_sent
            recv = netcount.bytes_recv
            f.write(str(sent)+" "+str(recv))
            time.sleep(2)
    return


if __name__ == "__main__":
    main()
