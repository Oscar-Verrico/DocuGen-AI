import openai
from dotenv import load_dotenv
import os

load_dotenv() 

openai.api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("MODEL")

def generate_documentation(function_name, signature, description):
    prompt =  f"""
    Generate a docstring for the following function:
    
    Function Name: {function_name}
    Signature: {signature}
    Description: {description}
    
    Provide a well-structured docstring including:
    - Parameters (names and types)
    - Return type/types
    - A brief function explanation
    """
    
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert system, mimicing a Python developer generating documentation for any given codebase."},
            {"role": "user", "content": prompt}
        ]
    )

    return response["choices"][0]["message"]["content"].strip()