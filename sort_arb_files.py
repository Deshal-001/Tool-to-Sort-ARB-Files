import json

# arb to Json
def read_arb_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

# Json to arb
def write_sorted_arb_file(sorted_data, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(sorted_data, file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    #get file paths from the user
    input_file_path = input("Enter the path of the input .arb file: ").strip()
    output_file_path = input("Enter the path of the output .arb file: ").strip()

    if not output_file_path:
        output_file_path = input_file_path

    # read the input file
    data = read_arb_file(input_file_path)

    # sort the dictionary by keys
    sorted_data = {"@@locale": data["@@locale"]}  # Keep @@locale key at the top
    sorted_data.update({key: data[key] for key in sorted(data) if key != "@@locale"})

    #write the sorted data to the output file
    write_sorted_arb_file(sorted_data, output_file_path)

    print(f"Done ! path: {output_file_path}")
