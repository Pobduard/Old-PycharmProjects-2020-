import os
from natsort import natsorted

starting_num = 2 # The desired number that you want the count to start with, or +1 the number you already have on the files
end_num = starting_num + 6 # How many files you wat to add
start_count, end_count = 1, end_num - starting_num
name = "screen"


os.chdir("C:/Users/JANETH/PycharmProjects/Snasa/screenchots")
for f in natsorted(os.listdir()):
    file, file_ext = os.path.splitext(f)
    file.split(".")
    new_name = "{}{}{}".format(name, str(starting_num), file_ext)
    if start_count <= end_count:
        os.rename(f, new_name)
        starting_num += 1
        start_count += 1
    elif end_num < starting_num:
        print("Done")
        break