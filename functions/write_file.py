import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error"{file_path}" is not in the working dir'
    
    if not os.path.isfile(abs_file_path):
        parent_dir = os.path.dirname(abs_file_path)

        try:
            os.makedirs(parent_dir,exist_ok=True)

        except Exception as e:
            return f"could not create parent dirs: {parent_dir} = {e}"
    
    try:
        with open(abs_file_path,"w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Failed to write to file: {file_path}, {e}"


