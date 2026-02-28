import os
from config import MAX_CHARS
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        absolute_path = os.path.abspath(working_directory)

        target_dir = os.path.join(absolute_path, file_path)
        combined_target_dir = os.path.normpath(target_dir)
            
        valid_target_dir = os.path.commonpath([absolute_path, combined_target_dir]) == absolute_path

        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        valid_directory = os.path.isdir(combined_target_dir)

        if valid_directory:
            return f'Error: Cannot write to "{file_path}" as it is a directory'


        abs_path = os.path.dirname(combined_target_dir)
        missing_dir = os.makedirs(abs_path, exist_ok=True)

        with open(combined_target_dir, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e: 
        return f"Error: {e}"
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write the content to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content you want to write into a file.",
            ),
        },
        required=["file_path", "content"],
    ),
)