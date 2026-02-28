import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        absolute_path = os.path.abspath(working_directory)

        target_dir = os.path.join(absolute_path, file_path)
        combined_target_dir = os.path.normpath(target_dir)
            
        valid_target_dir = os.path.commonpath([absolute_path, combined_target_dir]) == absolute_path

        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        valid_file = os.path.isfile(combined_target_dir)

        if not valid_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(combined_target_dir, "r") as f:
            content = f.read(MAX_CHARS)

            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    
        return content
    
    except Exception as e: 
        return f"Error: {e}"
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Takes a file, opens and reads the content returning it to the caller",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Provide a path to the file",
            ),
        },
    ),
)