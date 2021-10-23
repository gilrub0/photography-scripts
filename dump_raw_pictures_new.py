import datetime
import glob
import os
import shutil

from tqdm import tqdm


def copy_and_rename(path=r"I:\\"):
    found_files = [y for x in os.walk(path) for y in glob.glob(os.path.join(x[0], '*.NEF'))]
    root_dist_path = r"F:\photography\RAW"
    dates = []
    if not os.path.exists(root_dist_path):
        os.mkdir(root_dist_path)
        print("create root dist path")
    for f in found_files:
        file_creation_date = datetime.datetime.fromtimestamp(os.stat(f).st_mtime).strftime('%Y.%m.%d')
        dates.append(file_creation_date)
    dates = list(tuple(dates))
    for d in dates:
        date_folder = os.path.join(root_dist_path, d.replace('.', '\\')) + '\\jpg'
        if not os.path.exists(date_folder):
            os.makedirs(date_folder)
    for f in tqdm(found_files):
        file_creation_date = datetime.datetime.fromtimestamp(os.stat(f).st_mtime).strftime('%Y_%m_%d')
        new_file_location = os.path.join(root_dist_path, root_dist_path, os.path.join(
            datetime.datetime.fromtimestamp(os.stat(f).st_mtime).strftime('%Y_%m_%d').split("_")[0],
            datetime.datetime.fromtimestamp(os.stat(f).st_mtime).strftime('%Y_%m_%d').split("_")[1],
            datetime.datetime.fromtimestamp(os.stat(f).st_mtime).strftime('%Y_%m_%d').split("_")[2]))
        new_file_path_NEF = os.path.join(new_file_location, file_creation_date + '_' + f.split('\\')[-1])
        new_file_path_jpg = os.path.join(new_file_location + '\\jpg\\',
                                         file_creation_date + '_' + f.split('\\')[-1].replace('NEF', 'JPG'))
        if not os.path.exists(new_file_path_NEF):
            shutil.copy2(os.path.join(path, f), new_file_path_NEF)
            shutil.copy2(os.path.join(path, f.replace('NEF', 'JPG')), new_file_path_jpg)


def only_rename(path=r"F:\photography\RAW"):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in tqdm(files):
            if name.lower().endswith(('nef', 'jpg', 'xmp', 'mov')):
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
        a = input(r"input path to copy and rename from or return by 'b' (default path is I:\\): ")
        if len(a) > 0:
            copy_and_rename(a)
        if a == 'exit' or a == 'b':
            print('returning to main menu')
        else:
            copy_and_rename()
    if ans == "2":
        a = input(r"input path to scan and rename or return by 'b' (default is F:\\photography\\RAW): ")
        if a == "exit" or a == 'b':
            print('returning to main menu')
        if len(a) > 0:
            only_rename(a)
        else:
            only_rename()
    exit_opt = ['exit', 'e', 'E', 'q', 'Q']
    if ans in exit_opt:
        exit()
