from code_parser import parse_codebase
from generate import generate_documentation

CODEBASE_PATH = "codebases"


def main():
    # Parses functions using code_parser.py
    parsed_functions = parse_codebase(CODEBASE_PATH)
    
    # Iterates throuch each parsed function 
    for function in parsed_functions:
        docstring = generate_documentation(
            function["name"], function["signature"], function["description"]
        )
    
        # Print results
        print(f"\nFunction: {function['signature']}\nDocstring:\n{docstring}\n")

    print("Process Completed")


if __name__ == "__main__":
    main()