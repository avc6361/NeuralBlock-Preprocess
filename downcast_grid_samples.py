import csv
import json

def downcast_grids(csv_file_path = "grid_sample_1.csv"):
    # load downcast from file
    downcast_map = "downcasted_blocks.json"
    with open(downcast_map) as f:
        downcast_map = json.load(f)
    
    input_csv_path = csv_file_path
    output_csv_path = csv_file_path.replace(".csv", "_downcasted.csv")

    with open(input_csv_path, "r", newline="") as input, open(output_csv_path, "w", newline="") as output:
        reader = csv.reader(input)
        writer = csv.writer(output)

        # read and write header row
        header = next(reader)
        writer.writerow(header)

        # col_index range is 0-7201, only want even cols starting from 2
        # replace each block_type with downcasted value
        for grid_row in reader:
            for col_index in range(2, len(grid_row), 2):
                block_type = grid_row[col_index]
                grid_row[col_index] = downcast_map[block_type]
            writer.writerow(grid_row)

    print(f"Generated {output_csv_path}")

if __name__ == "__main__":
    csv_name = input("Enter name for CSV file: ")
    if csv_name.endswith(".csv") == False:
        csv_name += ".csv"
    print()

    downcast_grids(csv_name)