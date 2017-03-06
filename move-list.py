import csv
import subprocess
import sys

with open(sys.argv[1]) as f:
    records = csv.reader(f)
    for r in records:
        print(subprocess.check_output(["./attachment", "move", r[0], r[2]]).decode("utf-8").strip())
