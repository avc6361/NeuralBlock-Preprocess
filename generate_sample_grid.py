import csv
import random

minecraft_blocks_path = "minecraft_blocks.txt"
sample_csv_path = "grid_sample.csv"

# dimensions of grid
grid_rows = 9 # 45
grid_columns = 16 # 80

# not sure about max_dist
min_dist = 1
max_dist = 20

# not sure about xRot and yRot values
xRot = round(random.uniform(-90, 90), 2)
yRot = round(random.uniform(0, 360), 2)

with open(minecraft_blocks_path) as f:
    blocks = [line.strip() for line in f]

grid = []
header = ["xRot", "yRot", "row", "col", "block_type", "dist"]
grid.append(header)

for row in range(1, grid_rows + 1):
    for column in range(1, grid_columns + 1):
        block_type = random.choice(blocks)
        dist = random.randint(min_dist, max_dist)
        grid.append([xRot, yRot, row, column, block_type, dist])

with open(sample_csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(grid)

print("Generated grid_sample.csv")