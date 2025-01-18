import os

def scrape_lines_with_keyword(keyword):
    try:
        input_file = os.path.join(os.getcwd(), "692.txt")
        output_file = os.path.join(os.getcwd(), "692_output.txt")

        with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:

            for line in infile:
                line = line.strip()
                
                # Only process lines that contain the keyword
                if keyword in line:
                    # Split only on the first two colons
                    colon_split = line.split(":", 2)
                    
                    # Make sure we actually have 3 parts (2 colons)
                    if len(colon_split) == 3:
                        # The part after the second colon
                        after_second_colon = colon_split[2].strip()
                        
                        # If there's anything left, write it
                        if after_second_colon:
                            outfile.write(after_second_colon + "\n")

        print(f"Extraction completed. Results saved to {output_file}.")
        
    except FileNotFoundError:
        print(f"Error: File {input_file} not found in the current directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    keyword = input("Enter the keyword to search for: ").strip()
    scrape_lines_with_keyword(keyword)
