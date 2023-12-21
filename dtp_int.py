import argparse

def evaluate_expression(part, variables):
    for var_name, var_value in variables.items():
        if (var_value != None):
            try:
                result = eval(part, {}, variables)
                return str(result)
            except (SyntaxError, ZeroDivisionError, NameError) as e:
                return '?'
        else:
            return '?'

def execute_dtp(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        variables = {}  # Variable dictionary, values held by names

        for line in lines:
            line = line.strip()  # Remove leading/trailing whitespaces
            if line.endswith('¤'):  # Check for '¤' as end-of-line symbol
                line = line[:-1]  # Remove the trailing '¤'
                if line.startswith('.:'):
                    line = line[2:].rstrip('¤')  # Remove '.:' and ending '¤'
                    parts = [p.strip() for p in line.split(',')]

                    for part in parts:
                        if '=' in part:
                            var_name, value = part.split('=')
                        else:
                            var_name, *value = part.split()
                            value = ' '.join(value) if value else None

                        if (value != None):
                            var_name = var_name.strip()
                            value = value.strip()
                        
                            variables[var_name] = eval(value)
                        else:
                            variables[var_name] = None # It would be better if its value was None
                elif line.startswith('.∿'):
                    line = line[2:].rstrip('¤')  # Remove '.∿' and ending '¤'

                    parts = line.split(',')

                    for part in parts:
                        if '=' in part:
                            var_name, value = part.split('=', 1) # Split into one
                        else:
                            var_name, value = part.split('«', 1) # Split into one

                        var_name = var_name.strip()
                        value = value.strip()

                        if value.endswith('»'):
                            value = value[:-1]  # Remove the ending '»'

                            if var_name not in variables:
                                variables[var_name] = value
                            else:
                                print(f"Variable '{var_name}' already declared.")
                        else:
                            print("Invalid string declaration format:", part)
                elif line.startswith(':*'):
                    print_parts = []

                    content = line[3:].strip(')¤')  # Extract content after ':*(' and remove ending ')¤'
                    parts = content.split(';')  # Split by ';'

                    for part in parts:
                        part = part.strip()
                        
                        if part.startswith('«') and part.endswith('»'):
                            # String literal, strip quotes and append
                            print_parts.append(part[1:-1])
                        elif part.startswith('.'):
                            var_name = part[1:]
                            var_names = list(variables.keys())

                            if var_name.isdigit():
                                var_number = int(var_name)
                                if 0 <= var_number < len(var_names):
                                    print_parts.append(var_names[var_number])
                                else:
                                    print_parts.append('?')
                            else:
                                if var_name in variables:
                                    print_parts.append(var_name)
                                else:
                                    print_parts.append('?')
                        elif part.startswith('_'):
                            var_ref = part[1:]  # Remove the prefix

                            if var_ref.isdigit():
                                index = int(var_ref)
                                var_names = list(variables.keys())
                                if 0 <= index < len(var_names):
                                    print_parts.append(str(variables[var_names[index]]))
                                else:
                                    print_parts.append('?')
                            elif var_ref in variables:
                                    value = variables[var_ref]
                                    print_parts.append(str(variables[var_names[index]]))
                            else:
                                print_parts.append('?')
                        else:
                            # Check if the part contains an arithmetic expression
                            if any(op in part for op in ['+', '-', '*', '/']):
                                print_parts.append(evaluate_expression(part, variables))
                            else:
                                # Not a string literal, check if it's a number or variable
                                if part.isdigit():
                                    # If it's a regular integer, append
                                    print_parts.append(part)
                                elif part in variables:
                                    # If it's a variable name, append its value
                                    if (variables[part] != None):
                                        print_parts.append(str(variables[part]))
                                    else:
                                        print_parts.append('?')
                                else:
                                    # Unrecognized, print '?'
                                    print_parts.append('?')

                    print(' '.join(print_parts))  # Print the joined elements after each ':*' command

parser = argparse.ArgumentParser(description="Interpreter for .dtp files")
parser.add_argument('-o', help="Specify the .dtp file to execute")
parser.add_argument('-i', metavar='FILE', help="Show the code of the .dtp file")

args = parser.parse_args()

if args.o:
    execute_dtp(args.o)
elif args.i:
    file_input = args.i

    try:
        if os.path.exists(file_input):
            if os.name == 'nt':  # For Windows
                os.system(f"start {file_input}")
            elif os.name == 'posix':  # For Linux/Unix/MacOS
                os.system(f"xdg-open {file_input}")
            else:
                raise NotImplementedError(f"Unsupported OS: {os.name}")
        else:
            print(f"Error: File '{file_input}' not found.")
    except Exception as e:
        print(f"Error: Failed to open '{file_input}' in the default text editor: {e}")
        print(f"Opening '{file_input}' content in the command-line interface:")
        try:
            with open(file_input, 'r', encoding='utf-8') as file:
                print(file.read())
        except Exception as file_error:
            print(f"Error: Failed to read '{file_input}': {file_error}")
else:
    print("No input specified. Use '-o' to execute a file or '-i' to display code.")
