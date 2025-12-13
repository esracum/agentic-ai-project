import os
import sys
from dotenv import load_dotenv 
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info

from functions.get_file_content import schema_get_file_content

from functions.run_python_file import schema_run_python_file

from functions.write_file import schema_write_file

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")


    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Write to files(create or update)
    - Run python file with optional arguments

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    client = genai.Client(api_key=api_key)

    if len(sys.argv)<2:
        print("i need a prompt")
        sys.exit(1)
    verbose_flag = False

    if len(sys.argv)==3 and sys.argv[2]=="--verbose":
        verbose_flag = True
    prompt=sys.argv[1]

    messages=[
        types.Content(role='user',parts=[types.Part(text=prompt)])
    ]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]
    )

    config = types.GenerateContentConfig(
        tools = [available_functions],
        system_instruction = system_prompt

    )

    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=messages,
        config= config
    )

    if response is None or response.usage_metadata is None:
        print("response is malformed")
        return
    

    if verbose_flag:
        print(f"user prompt:{prompt}")
        print(f"prompt tokens:{response.usage_metadata.prompt_token_count}")
        print(f"response tokens:{response.usage_metadata.candidates_token_count}")
    


    if response.function_calls:
        
        for function_call_part in response.function_calls:
             print(f"Calling function {function_call_part.name} args: {function_call_part.args}")
            

    else:
        print(response.text)
    
    



if __name__ == "__main__":
    main()



