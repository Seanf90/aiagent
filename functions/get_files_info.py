import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    try:
        absolute_path = os.path.abspath(working_directory)

        target_dir = os.path.join(absolute_path, directory)
        combined_target_dir = os.path.normpath(target_dir)
        
        valid_target_dir = os.path.commonpath([absolute_path, combined_target_dir]) == absolute_path

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        valid_directory = os.path.isdir(combined_target_dir)

        if not valid_directory:
            return f'Error: "{directory}" is not a directory'
        
        directory_contents = os.listdir(combined_target_dir)

        directory_list = []

        for item in directory_contents:
            combined_path = os.path.join(combined_target_dir ,item)
            name = item
            file_size = os.path.getsize(combined_path)
            is_dir = os.path.isdir(combined_path)
            directory_string = f"- {name}: file_size={file_size} bytes, is_dir={is_dir}"
            directory_list.append(directory_string)

        return "\n".join(directory_list)

    except Exception as e: 
        return f"Error: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)