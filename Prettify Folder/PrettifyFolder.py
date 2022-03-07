# Objectives - Take a folder path, take exclusion file names in a text file, take file extension
# Make all files in that folder in Sentence case without the file name and extensions

import os
from glob import glob


def soldier(folder_path: str, exclusion_file: str = None, extension: str = None):
    print("File prettifying in progress...")
    os.chdir(folder_path)

    index = 1
    if exclusion_file:
        with open(exclusion_file, "rt") as f:
            exclusion_list = f.read().split("\n")
        for file in glob("*.*"):
            if file not in exclusion_list:
                if extension:
                    if file.split(".")[1] != extension:
                        os.rename(file, f"{file.split('.')[0].upper()}.{file.split('.')[1]}")
                    else:
                        os.rename(file, f"{index}.{file.split('.')[1]}")
                        index += 1
                else:
                    os.rename(file, f"{file.split('.')[0].upper()}.{file.split('.')[1]}")
        else:
            print("File renamed successfully!")
    else:
        for file in glob("*.*"):
            if extension:
                if file.split(".")[1] != extension:
                    os.rename(file, f"{file.split('.')[0].upper()}.{file.split('.')[1]}")
                else:
                    os.rename(file, f"{index}.{file.split('.')[1]}")
                    index += 1
            else:
                os.rename(file, f"{file.split('.')[0].upper()}.{file.split('.')[1]}")
        else:
            print("File renamed successfully!")


def user_input():
    global param1, param2, param3
    user_dir = input("! WARNING: Case-sensitive input ahead.\n"
                     "Write the complete folder path (e.g., C:/Some Path/My Folder): ").strip()
    if user_dir:
        try:
            os.chdir(user_dir)
        except FileNotFoundError:
            print(f"Path {user_dir} doesn't exists or entered incorrectly. Try again.")
            os.chdir("./") if input("Press, 'Y' to select current directory as folder path "
                                    "or any key to try again: ").lower().strip() == "y" else user_input()
        except NotADirectoryError:
            print(f"Sorry, {user_dir} is not a directory. Try again.")
            os.chdir("./") if input("Press, 'Y' to select current directory as folder path "
                                    "or any key to try again: ").lower().strip() == "y" else user_input()
        except PermissionError:
            print(f"Permission Denied! {user_dir} is set to restricted access only. Try again")
            os.chdir("./") if input("Press, 'Y' to select current directory as folder path "
                                    "or any key to try again: ").lower().strip() == "y" else user_input()
        else:
            print("OK, Folder path taken.")
        finally:
            param1 = user_dir
    else:
        print("You have to specify a folder path to proceed.")
        user_input()

    user_excl_file = input("! WARNING: Case-sensitive input ahead.\nWrite the full path for the "
                           "exclusion file (e.g., C:/My File.txt) or leave blank for none: ").strip()
    if user_excl_file:
        try:
            os.path.isfile(user_excl_file)
        except FileNotFoundError:
            print(f"Sorry, your specified exclusion file {user_excl_file} is not found. Try again.")
            user_excl_file = None if input("Press, 'Y' to proceed without exclusion file or any key to try again "
                                           "from the beginning: ").lower().strip() == "y" else user_input()
        except FileExistsError:
            print(f"Sorry, {user_excl_file} file with wrong extension. Try with proper file extension.")
            user_excl_file = None if input("Press, 'Y' to proceed without exclusion file or any key to try again "
                                           "from the beginning: ").lower().strip() == "y" else user_input()
        else:
            print("OK, exclusion file specified.")
        finally:
            param2 = user_excl_file
    else:
        param2 = None

    user_ext = input(f"Write the numbering file type extension in the folder path {user_dir}"
                     " (e.g., JPG or PDF) or leave blank for none: ").strip().lower()
    if user_ext:
        try:
            glob(f"*{user_ext}")[0]  # try to access at least one occurrence of file with given extension
        except Exception as e:
            print(f"Sorry, your specified numbering file type {user_ext} is not found "
                  f"in the specified folder path. Try again.")
            user_ext = None if input("Press, 'Y' to proceed without numbering file type or any key to try again "
                                     "from the beginning: ").lower().strip() == "y" else user_input()
        else:
            print("OK, numbering file specified.")
        finally:
            param3 = user_ext
    else:
        param3 = None

    soldier(param1, param2, param3)


if __name__ == '__main__':

    title = "Exercise 8 - Oh Soldier Prettify My Folder"
    subtitle = "[Note: Files and Folder organizer by transforming their names' case]"
    underline = int(len(subtitle)) * "-"
    print("\n{}\n{}\n{}\n".format(title, underline, subtitle))

    param1, param2, param3 = None, None, None
    user_input()
    exit()
