import os
import ast # python interpreter

# Scans a codebase for files to parse functions
def parse_codebase(codebase_path):
    parsed_elements = []

    for root, _, files in os.walk(codebase_path):
        for file in files:
            
            if file.endswith(".py"):                 # python interpret case
                file_path = os.path.join(root, file) # concatonates file path 
                parsed_elements.extend(parse_py_file(file_path))
            
            # add other interpret cases here
    return parsed_elements 


# Interprets a python file and breaks it down to base function elements to analyze
def parse_py_file(file_path):
    
    with open(file_path, "r") as file:
        to_parse=ast.parse(file.read())

    elements = []
    for element in ast.walk(to_parse):
        if isinstance(element, ast.FunctionDef):
            elements.append({
                "id": f"{file_path}:{element.lineno}",
                "name": element.name, 
                "signature": f"{element.name}({', '.join(arg.arg for arg in element.args.args)})", # functions name and arguments
                "description": "Extracted with AST",
                "file_path": file_path,
                "line": element.lineno,
                "length": len(element.body)
            })
    
    return elements