import csv
import json

downcast_map = "downcasted_blocks_v1.json"
input_csv_path = "grid_sample.csv"
output_csv_path = "grid_sample_downcasted.csv"

with open(downcast_map) as f:
    downcast_map = json.load(f)

with open(input_csv_path, "r", newline="") as input, \
    open(output_csv_path, "w", newline="") as output:
    
    reader = csv.reader(input)
    writer = csv.writer(output)

    header = next(reader)
    writer.writerow(header)

    for row in reader:
        # block_type is in 5th column
        block_type = row[4]

        if block_type in downcast_map:
            row[4] = downcast_map[block_type]
        
        writer.writerow(row)

print("Completed downcast map on grid sample.")
print("Generated grid_sample_downcasted.csv")