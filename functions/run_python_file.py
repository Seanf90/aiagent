import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        absolute_path = os.path.abspath(working_directory)

        target_dir = os.path.join(absolute_path, file_path)
        combined_target_dir = os.path.normpath(target_dir)
            
        valid_target_dir = os.path.commonpath([absolute_path, combined_target_dir]) == absolute_path

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'


        valid_file = os.path.isfile(combined_target_dir)

        if not valid_file:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", combined_target_dir]
        if args:
            command.extend(args)

        completed = subprocess.run(
            command,
            cwd=absolute_path,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output_parts = []

        if completed.returncode != 0:
            output_parts.append(f"Process exited with code {completed.returncode}")

        if not completed.stdout and not completed.stderr:
            output_parts.append("No output produced")
        else:
            if completed.stdout:
                output_parts.append(f"STDOUT: {completed.stdout}")
            if completed.stderr:
                output_parts.append(f"STDERR: {completed.stderr}")

        return "\n".join(output_parts)
        
            
    except Exception as e: 
        return f"Error: executing Python file: {e}"
    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python 3 file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)