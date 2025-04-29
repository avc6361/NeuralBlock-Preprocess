import os
import csv

OUTPUT_FILE_NAME = "combined-grid.csv"
LINES_PROCESSED_PRINT_FREQ = 250

csvs = []
for file in os.listdir():
    if file.endswith(".csv") and file != OUTPUT_FILE_NAME:
        csvs.append(file)

print(f"Found {len(csvs)} CSVs...")

lines_written = 0
header_written = False
with open(OUTPUT_FILE_NAME, "w", newline="") as output:
    for file in csvs:
        with open(file, "r") as input:
            line = input.readline()
            if not header_written:
                output.write(line)
                header_written=True

            line = input.readline()
            while line:
                output.write(line)
                lines_written += 1
                if lines_written % LINES_PROCESSED_PRINT_FREQ == 0:
                    print(f"{file}: Processed {lines_written} lines so far...")
                line = input.readline()

        print(f"{file}: Processed {lines_written} lines ✅")
        lines_written = 0

print("Done")