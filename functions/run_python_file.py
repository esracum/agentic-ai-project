import os
import subprocess

def run_python_file(working_directory: str, file_path: str):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error"{file_path}" is not in the working dir'


    if not os.path.isfile(abs_file_path):
        return f'Error"{file_path}" is not file'

    
    if not file_path.endswith(".py"):
        return f'Eror: "{file_path} is not a Python file.'

    try:
        output = subprocess.run(
            ["python",file_path], cwd=abs_working_dir, 
            timeout=30,
            capture_output=True
        )
        final_string = f"""
STDOUT: {output.stdout}
STDERR: {output.stderr}
"""
        

        if output.stdout == "" and output.stderr == "":
            final_string = "No output produced. \n"

        if output.returncode != 0:
            final_string += f"Process exited with code. {output.returncode}"
        
        return final_string

    except Exception as e:
        return f'Error:executing Python file: {e}'

    

