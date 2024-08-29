
import os
import dvuploader as dv
import csv
import subprocess
import yaml


# CSV to YML converter adapted from https://github.com/hfionte/csv_to_yaml
# Takes a file CSV file called "config.csv" and outputs rows into a YAML file.
# Data in the first row of the CSV is assumed to be the column heading.

# Open our data file in read-mode.
csvfile = open(os.path.join('C:/Users/Dickinson Lab Member/DVU', 'config.csv'), 'r')

# Save a CSV Reader object.
datareader = csv.reader(csvfile, delimiter=',', quotechar='"')

# Empty array for data headings, which we will fill with the first row from our CSV.
data_headings = []
# List to store each row as a dictionary
data_list = []

# Loop through each row...
for row_index, row in enumerate(datareader):
    # If this is the first row, populate our data_headings variable.
    if row_index == 0:
        data_headings = row
    else:
        # Create a dictionary for this row.
        row_dict = {}
        
        # Loop through each cell in this row...
        for cell_index, cell in enumerate(row):
            # Convert headings to lowercase and replace spaces with underscores.
            cell_heading = data_headings[cell_index].lower().replace(" ", "_").replace("-", "")
            row_dict[cell_heading] = cell.replace("\n", ", ")
        
        # Append the dictionary to the list.
        data_list.append(row_dict)

# Write all rows to a single YAML file.
filename = os.path.join('C:/Users/Dickinson Lab Member/DVU', 'config.yml')
with open(filename, 'w') as yaml_file:
    yaml.dump(data_list, yaml_file, default_flow_style=False)

# Close the CSV file.
csvfile.close()

# The rest of the code runs the DVuploader CLI commands (see Command Line Interface section of DVuploader readme) 

# Define the command and its arguments
command = ['dvuploader', '--config-path', 'config.yml']

# Run the command
result = subprocess.run(command, capture_output=True, text=True)

# Print the standard output and error (if any)
print("Standard Output:", result.stdout)
print("Standard Error:", result.stderr)
print("Return Code:", result.returncode)
