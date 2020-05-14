import glob
file_name_list = glob.glob('sub_folders\**\*.py', recursive=True)

print(len(file_name_list))