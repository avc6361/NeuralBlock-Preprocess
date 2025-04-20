import csv
import os
import random

def generate_grid_data(csv_file_path = "grid_sample_1.csv", num_grids = 0): 
    # load minecraft block types from file
    minecraft_blocks_path = "minecraft_blocks.txt"
    with open(minecraft_blocks_path) as f:
        block_types = [line.strip() for line in f]

    # dimensions of grid
    grid_rows = 45
    grid_cols = 80

    # distance
    min_dist = 1
    max_dist = 160

    # create header
    # 7202 columns (xRot, yRot, block_1, block_1_dist, block_2, block_2_dist, etc.)
    header = ["xRot", "yRot"]
    for i in range(1, grid_rows * grid_cols + 1):
        header.append(f"block_{i}")
        header.append(f"block_{i}_dist")
    
    file_exists = os.path.exists(csv_file_path)
    
    with open(csv_file_path, "a", newline="") as f:
        writer = csv.writer(f)
        # if csv file exists, append without creating header
        if file_exists == False:
            writer.writerow(header)
            print("Created", csv_file_path)
        
        for i in range(num_grids):
            # rotation
            xRot = random.uniform(-90, 90)
            xRot_rounded = format(xRot, ".2f")
            yRot = random.uniform(-180, 180)
            yRot_mod = yRot % 90
            yRot_rounded = format(yRot_mod, ".2f")
        
            # add blocks and distances to grid
            grid = [xRot_rounded, yRot_rounded]
            for i in range(grid_rows * grid_cols):
                block = random.choice(block_types)
                dist = random.randint(min_dist, max_dist)
                grid.extend([block, dist])

            # add grid to csv
            writer.writerow(grid)
    print(f"Appended {num_grids} new grid(s) to", csv_file_path)

if __name__ == "__main__":
    csv_name = input("Enter name for CSV file (ex grid_sample_1): ")
    if csv_name.endswith(".csv") == False:
        csv_name += ".csv"
    num_grids = int(input("Enter number of grids to generate: "))
    print()

    generate_grid_data(csv_name, num_grids)


