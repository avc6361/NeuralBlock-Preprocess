# NeuralBlock-Preprocess
A collection of helper scripts to process block grid data.

# Looking for a sample dataset?
Premade datasets are available [on the releases page](https://github.com/avc6361/NeuralBlock-Preprocess/releases/)\
`NeuralBlock-CombinedGrid.csv` contains raw data from the NeuralBlock mod.\
`NeuralBlock-CombinedGrid_downcasted` contains downcasted data for model training.

# Looking to create your own dataset?
Follow these workflow steps:
1. Get your data .csv from [the NeuralBlock mod](https://github.com/TheIcyStar/NeuralBlock) or use `generate_grid_samples.py` to create synthetic data.
2. If you have multiple .csv files, use `combine_csvs.py`.
3. "Downcast" the block types with `downcast_grid_samples.py`.
4. You're ready to train the model

If you need to change the block downcasting process for step 3, modify `downcasted_blocks.json`. You may want to use an LLM to generate this json file for you.

## generate_grid_samples.py
Generates a CSV file containing 45x80 grids of Minecraft block data (includes xRot,
yRot, block types, and distances)

1. Run the script and enter the name of the CSV file (with or without `.csv`)
2. Then, enter the number of grids to generate
- If the CSV already exists, new grids will be appended to it

## combine_csvs.py
Combines all CVSs in the current working directory into one csv named "combined-grid.csv"\
Ignores CSVs with the same name, and only uses the header from the first .csv it finds.

1. Simply run the script

## downcast_grid_samples.py
Simplifies block types in a grid CSV using a downcasted_blocks.json file

1. Run the script and enter the name of the CSV file (with or without `.csv`)
