
def modify_file_content(content):
    """
    Modifies the file content by converting it to uppercase.
    """
    return content.upper()

def main():
    """
    Reads a file, modifies its content, and writes it to a new file,
    with error handling for file operations.
    """
    try:
        # Get input and output filenames from the user
        input_filename = input("Enter the name of the input file: ")
        output_filename = input("Enter the name of the output file: ")

        # Read the content of the input file
        try:
            with open(input_filename, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' was not found.")
            return
        except IOError as e:
            print(f"Error reading file '{input_filename}': {e}")
            return

        # Modify the content
        modified_content = modify_file_content(content)

        # Write the modified content to the output file
        try:
            with open(output_filename, 'w') as f:
                f.write(modified_content)
            print(f"Successfully modified '{input_filename}' and wrote to '{output_filename}'.")
        except IOError as e:
            print(f"Error writing to file '{output_filename}': {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
