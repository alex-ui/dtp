import argparse

def execute_dtp(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        variables = {}  # Dictionary to hold numerical values by variable names

        for line in lines:
            line = line.strip()  # Remove leading/trailing whitespaces
            if line.endswith('¤'):  # Check for '¤' as end-of-line symbol
                line = line[:-1]  # Remove the trailing '¤'
                if line.startswith('.:'):
                    parts = line[2:].split(',')
                    for part in parts:
                        subparts = part.strip().split()
                        if len(subparts) >= 2 and subparts[1].isdigit():
                            variable_name = subparts[0]
                            value = ''.join(subparts[1:])
                            variables[variable_name] = int(value)
                        else:
                            print("Invalid .: command:", part)
                elif line.startswith(':*'):
                    print_parts = []

                    content = line[3:].strip(')¤')  # Extract content after ':*(' and remove ending ')¤'
                    parts = content.split(';')  # Split by ';'

                    for part in parts:
                        part = part.strip()
                        if part.startswith('«') and part.endswith('»'):
                            # String literal, strip quotes and append
                            print_parts.append(part[1:-1])
                        else:
                            # Not a string literal, check if it's a number or variable
                            if part.isdigit():
                                # If it's a regular integer, append
                                print_parts.append(part)
                            elif part in variables:
                                # If it's a variable name, append its value
                                print_parts.append(str(variables[part]))
                            else:
                                # Unrecognized, print '?'
                                print_parts.append('?')

                    print(' '.join(print_parts))  # Print the joined elements after each ':*' command

parser = argparse.ArgumentParser(description="Interpreter for .dtp files")
parser.add_argument('-o', help="Specify the .dtp file to execute")
parser.add_argument('-i', action='store_true', help="Show the code of the .dtp file")

args = parser.parse_args()

if args.o:
    execute_dtp(args.o)
elif args.i:
    file_input = input("Enter the name of the .dtp file: ")
    with open(file_input, 'r', encoding='utf-8') as file:
        print(file.read())
else:
    print("No input specified. Use '-o' to execute a file or '-i' to display code.")
