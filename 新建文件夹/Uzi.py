def count_and_replace_terrible(input_file, output_file):
    try:
        # Read the content of the input file
        with open(input_file, 'r') as file:
            text = file.read()

        # Split the text into words and initialize counters
        words = text.split()
        total_terrible_count = 0

        # Count and replace "terrible" with "pathetic" or "marvellous"
        for i in range(len(words)):
            word = words[i].strip('.,!?()";:')
            if word.lower() == "terrible":
                total_terrible_count += 1
                if total_terrible_count % 2 == 0:
                    words[i] = "pathetic"
                else:
                    words[i] = "marvellous"

        # Join the modified words back into a text
        modified_text = ' '.join(words)

        # Write the modified text to the output file
        with open(output_file, 'w') as file:
            file.write(modified_text)

        print(f"Total occurrences of 'terrible': {total_terrible_count}")
        print(f"Modified text written to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")

if __name__ == "__main__":
    input_file = "file_to_read.txt"
    output_file = "result.txt"
    count_and_replace_terrible(input_file, output_file)