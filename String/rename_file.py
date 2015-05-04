import os

def rename_file():
    file_list = os.listdir("C:\Users\Zachary\Documents\GitHub\PythonPractice\String\RenameFiles")
    #print file_list
    saved_path = os.getcwd()
    os.chdir("C:\Users\Zachary\Documents\GitHub\PythonPractice\String\RenameFiles")
    for file_name in file_list:
        os.rename("tom","austin")

rename_file()
