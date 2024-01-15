import csv

def averageAgeCalculate(file_path):
    try:
        with open(file_path, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            
            # Check if the required columns exist
            if "Name" not in reader.fieldnames or "Age" not in reader.fieldnames:
                raise ValueError("CSV file must contain 'Name' and 'Age' columns.")

            total_age = 0.0
            num_people = 0

            for row in reader:
                try:
                    age = int(row['Age'])
                    total_age += age
                    num_people += 1
                except ValueError:
                    print(f"Skipped row due to invalid age: {row}")

            if num_people == 0:
                print("No valid data to calculate average age.")
            else:
                average_age = total_age / num_people
                print(f"Average Age: {average_age:.2f}")
                
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

averageAgeCalculate("data.csv")