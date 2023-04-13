#!/usr/bin/python3

import sys
from collections import defaultdict

files = 0
status = defaultdict(int)
lines = 0

try:
    for line in sys.stdin:
        lines += 1
        fields = line.split()

        if len(fields) != 7:
            continue

        file_size = int(fields[6])
        status_code = int(fields[5])

        files += file_size
        status[status_code] += 1

        if lines % 10 == 0:
            print(f"Total file size: {files}")

            for code in sorted(status.keys()):
                if code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    print(f"{code}: {status[code]}")

        try:
            pass
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(0)

except KeyboardInterrupt:
    print("Exiting...")
    sys.exit(0)
