import csv


def write_to_csv(output_list, file_name="files/options/search_data/option_data.csv"):
    with open(file_name, mode="a", newline='') as csvfile:

        fieldnames = ["Option Symbol", "Strike Price", "Contract Type", "Expiration Date", "Delta", "Day Change Percent", 
                      "Implied Volatility", "Underlying Price", "Break Even Price", "Result", "Day Volume", 
                      "Day VWAP", "Underlying", "Open Interest"]
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header only if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow(output_list)


