#from functions.get_files_info import get_files_info
#from functions.get_file_content import get_file_content
#from functions.write_file import write_file
from functions.run_python_file import run_python_file




'''def main():
    #test get_files_info
    working_dir = "calculator"
    root_contents = get_files_info(working_dir)
    print(root_contents)
    pkg_contents = get_files_info(working_dir, "pkg")
    print(pkg_contents)
    pkg_content = get_files_info(working_dir, "/bin")
    print(pkg_content)
    pkg_conten = get_files_info(working_dir, "../")
    print(pkg_conten)'''

    
'''def main():
    working_dir= "calculator"
    #print(get_file_content(working_dir, "lorem.txt"))
    print(get_file_content(working_dir, "main.py"))
    print(get_file_content(working_dir, "pkg/calculator.py"))
    print(get_file_content(working_dir, "/bin/cat"))
    print(get_file_content(working_dir, "pkg/not_exists.py"))


'''
'''def main():

    working_dir = "calculator"
    print(write_file("calculator", "lorem.txt", "wait this is not lorem ipsum. this is differentolopokoliskom"))

    print(write_file( working_dir, "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    print(write_file(working_dir, "/tmp/temp.txt", "wait this is should not be allowed"))
    
    print(write_file( working_dir, "pkg_not_exist/morelorem.txt", "lorem ipsum dolor sit amet")) '''

def main():
    working_dir = "calculator"
    print(run_python_file(working_dir, "main.py"))
    print(run_python_file(working_dir, "tests.py"))



main()