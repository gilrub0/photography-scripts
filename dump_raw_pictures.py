import datetime
import glob
import os
import shutil


def copy_and_rename(path=r"I:\\"):
    found_files = [y for x in os.walk(path) for y in glob.glob(os.path.join(x[0], '*.NEF'))]
    root_dist_path = r"F:\photography\RAW"
    dates = []
    files_counter = len(found_files)
    if not os.path.exists(root_dist_path):
        os.mkdir(root_dist_path)
        print("create root dist path")
    for f in found_files:
        file_creation_date = datetime.datetime.fromtimestamp(os.stat(f).st_mtime).strftime('%Y.%m.%d')
        dates.append(file_creation_date)
    dates = list(tuple(dates))
    for d in dates:
        date_folder = os.path.join(root_dist_path, d.replace('.', '\\'))
        if not os.path.exists(date_folder):
            os.makedirs(date_folder)

    copied_files = 0
    for f in found_files:
        file_creation_date = datetime.datetime.fromtimestamp(os.stat(f).st_mtime).strftime('%Y_%m_%d')
        new_file_path = os.path.join(root_dist_path, os.path.join(
            datetime.datetime.fromtimestamp(os.stat(f).st_mtime).strftime('%Y_%m_%d').split("_")[0],
            datetime.datetime.fromtimestamp(os.stat(f).st_mtime).strftime('%Y_%m_%d').split("_")[1],
            datetime.datetime.fromtimestamp(os.stat(f).st_mtime).strftime('%Y_%m_%d').split("_")[2]),
                                     file_creation_date + '_' + f.split('\\')[-1])
        if not os.path.exists(new_file_path):
            shutil.copy2(os.path.join(path, f), new_file_path)
            print("copied " + str(copied_files) + "/" + str(files_counter) + " files")
        else:
            print("file already exists: ", new_file_path)
        copied_files += 1




def only_rename(path=r"F:\photography\RAW"):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if name.startswith('DSC') and name.endswith(('NEF', 'jpg', 'xmp', 'MOV')):
                os.rename(os.path.join(root, name), os.path.join(root, datetime.datetime.fromtimestamp(
                    os.stat(os.path.join(root, name)).st_mtime).strftime('%Y_%m_%d') + '_' + name))


while True:
    print("")
    print("   menu")
    print('________________________')
    print(r"1. copy and rename (default path is I:\)")
    print(r"2. only fix name (default path is F:\photography\RAW)")
    print("input exit to exit")
    ans = input("chose number: ")
    if ans == "1":
        a = input("input path to copy and rename from or return by 'b' (default path is I:\\): ")
        if len(a) > 0:
            copy_and_rename(a)
        if a == 'exit' or a == 'b':
            print('returning to main menu')
        else:
            copy_and_rename()
    if ans == "2":
        a = input("input path to scan and rename or return by 'b' (default is F:\\photography\\RAW): ")
        if a == "exit" or a == 'b':
            print('returning to main menu')
        if len(a) > 0:
            only_rename(a)
        else:
            only_rename()
    exit_opt = ['exit','e','E','q','Q']
    if ans in exit_opt:
        exit()
