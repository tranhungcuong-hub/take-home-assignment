import csv

def dataProcessing(input_file, output_file, columns):
    try:
        with open(input_file, 'r', newline='') as input_csv, \
             open(output_file, 'w', newline='') as output_csv:

            reader = csv.DictReader(input_csv)
            
            # Check if the required columns exist
            for column in columns:
                if column not in reader.fieldnames:
                    raise ValueError(f"Column '{column}' not found in the input file.")

            writer = csv.DictWriter(output_csv, fieldnames=columns)
            
            # Write header to the output file
            writer.writeheader()

            # Extract and write specified columns
            for row in reader:
                if row['Age'].strip():  # Assuming empty strings should be skipped
                    row['Age'] = int(float(row['Age']))
                else:
                    row['Age'] = None
                data = {column: row[column] for column in columns}
                writer.writerow(data)

        print(f"Data from columns {', '.join(columns)} in '{input_file}' has been successfully written to '{output_file}'.")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

dataProcessing("input_data.csv", "data.csv", ["Name", "Age"])
