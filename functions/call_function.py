from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.run_python_file import run_python_file, schema_run_python_file
from functions.write_file import write_file, schema_write_file
from google.genai import types

working_directory = "calculator"


def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    function_args = function_call_part.args

    if verbose:
        print(f"Calling function {function_name} with args: {function_args}")
    else:
        print(f"Calling function {function_name} ")
    
    # --- DÜZELTME 1: Başlangıçta result değişkenini tanımla ---
    result = None 

    # --- DÜZELTME 2: Return etmek yerine result değişkenine ata ---
    try:
        if function_name == "get_files_info":
            result = get_files_info(working_directory, **function_args)

        elif function_name == "get_file_content":
            result = get_file_content(working_directory, **function_args)

        elif function_name == "run_python_file":
            result = run_python_file(working_directory, **function_args)
        
        elif function_name == "write_file":
            result = write_file(working_directory, **function_args)
            
        else:
            # Bilinmeyen fonksiyon durumu
            return {"error": f"Unknown function: {function_name}"}

    except Exception as e:
        return {"error": f"Function execution failed: {str(e)}"}

    # --- DÜZELTME 3: Kontrolü şimdi yapabilirsin ---
    # Eğer sonuç None ise veya boşsa (fonksiyonuna göre değişir)
    if result is None:
         return {"result": "No output"}
         
         
    return result
    
    if result == "":
        return types.Content(
            role="tool", 
            parts=[types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_name}"}
        )
    ])

    