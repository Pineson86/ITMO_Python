#requirements = keyboard
import os
import shutil
import time
import keyboard
from datetime import datetime

#Folder paths
#my_folder_path = r"C:\Users\User\Documents\Codding\Python\ITMO_Python"
#backup_folder_path = r"C:\Users\User\Documents\Codding\Python\backup"

try:
    print('Press "Ctrl+C" to exit')
    #get folder paths from user     
    my_folder_path = input('insert your folder path. To exit press "ctrl+C": ').replace('\\', '/')
    backup_folder_path = input('insert backup folder path. To exit press "Ctrl+C": ').replace('\\', '/')
except Exception as E:
    print(f'Path data from user was not excepted. Error: {E}')
backup = True
while backup:
    if keyboard.is_pressed('Ctrl+C'):
        backup = False
    if not backup:
        time.sleep(3)
        break
    
    #Get variables for folder names
    current_date = str(datetime.now().date())
    current_time = str(datetime.now().time()).replace(':', '-')

    try:
        #get folder paths in backup folder which are going to be created
        mainfolder_path = os.path.join(backup_folder_path, current_date)
        subfolder_path = os.path.join(mainfolder_path, current_time)

        #create folders
        os.makedirs(mainfolder_path, exist_ok=True)
        os.makedirs(subfolder_path, exist_ok=True)

        #copy files
        shutil.copytree(my_folder_path, subfolder_path, dirs_exist_ok=True)
    except Exception as E:
        print(f'While backuping error occured. Eroor: {E}')

    time.sleep(60)
    print('Next loup of backuping is starting now') 