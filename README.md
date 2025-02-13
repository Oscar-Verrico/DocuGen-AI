DocuGen-AI is a OpemAI-powered tool designed to automatically generate documentation for entire codebases by analyzing function signatures and descriptions.
Currently, it only extracts information from python files, but other popular programming languages will be supported soon.

The program also relies on a .env foel to store your OpenAI API key and selected model, so yoiu will have to manualy change that with your own OpenAI info for the program to utilize.

To set up the program's needed requirements run this command in the base directory of the project:
pip install -r requirements.txt

TO run the program run this command in a python 3.10+ environment:
python main.py

Planned features:

* More language support
    - Java,
    - JavaScript
    - HTML
    - C/C++
      
* Better context-based prompting logic
  
* Config.json file to store options for running code and saving results
  - Auto-add generated documentation to parsed files
  - Save results to an output.txt
  - a token limit per documentation generated 
