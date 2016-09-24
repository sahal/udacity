from os import listdir,getcwd,rename,chdir

def rename_files():
# 1) get filenames
    file_list=listdir("/home/sahal/Downloads/exploded_prank/")
    print(file_list)
# 2) foreach filename rename files
    chdir("/home/sahal/Downloads/exploded_prank/")
    for file_name in file_list:
        print("Old filename %s" % file_name)
        print("New filename %s" % file_name.translate(None,"0123456789"))
        rename(file_name,file_name.translate(None,"0123456789"))

rename_files()
