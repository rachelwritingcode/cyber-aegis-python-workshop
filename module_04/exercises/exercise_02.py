import os
from zipfile import ZipFile

def unzip():
   # Unzip the zip file 
   with ZipFile('secret_folder.zip', 'r') as zip_object:
      zip_object.extractall()

def navigate_folders():
   # change directory to secret_folder
   os.chdir("./secret_folder/")
   # change directory to secret_subfolder
   os.chdir("./secret_subfolder/")
   # read the secret_file.txt
   f = open("secret_file.txt", "r")
   print(f.read()) 

unzip()
navigate_folders()
