import datetime
import glob
import os
import shutil

from tqdm import tqdm


def copy_and_rename(path=r"I:\\", **kwargs):
    found_files = [y for x in os.walk(path) for y in glob.glob(os.path.join(x[0], '*.NEF'))]
    root_dist_path = kwargs.get('req_dest') if kwargs.get('req_dest') else r"F:\photography\RAW"
    dates = []
    if not os.path.exists(root_dist_path):
        os.makedirs(root_dist_path)
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
            jpg_version = f.replace('NEF', 'JPG')
            if os.path.exists(os.path.join(path, jpg_version)):
                shutil.copy2(os.path.join(path, jpg_version), new_file_path_jpg)
        else:
            continue


def only_rename(path=r"F:\photography\RAW"):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in tqdm(files):
            if name.lower().endswith(('nef', 'jpg', 'xmp', 'mov')):
                os.rename(os.path.join(root, name), os.path.join(root, datetime.datetime.fromtimestamp(
                    os.stat(os.path.join(root, name)).st_mtime).strftime('%Y_%m_%d') + '_' + name))


while True:
    exit_opt = ['exit', 'e', 'E', 'q', 'Q']
    print("")
    print("   menu")
    print('________________________')
    print(r"1. copy and rename (default path is I:\)")
    print(r"2. only fix name (default path is F:\photography\RAW)")
    print(f"enter {' / '.join(exit_opt)} to exit")
    ans = input("chose number: ")
    if ans == "1":
        a = input(r"input path to copy and rename from or return by 'b' (default path is I:\\): ")
        if a in ['exit', 'b']:
            print('returning to main menu')
            continue
        else:
            req_dest = input(r"input path destination path or return by 'b' (default path is F:\photography\RAW)")
            if len(a) > 0 and req_dest not in ['exit', 'b']:
                copy_and_rename(a, req_dest=req_dest)
            else:  # copy and rename default path
                copy_and_rename(req_dest=req_dest)
    if ans == "2":
        a = input(r"input path to scan and rename or return by 'b' (default is F:\\photography\\RAW): ")
        if a == "exit" or a == 'b':
            print('returning to main menu')
            continue
        if len(a) > 0:
            only_rename(a)
        else:  # only rename default path
            only_rename()

    if ans in exit_opt:
        print("Thank you!")
        print("bye!")
        exit()
