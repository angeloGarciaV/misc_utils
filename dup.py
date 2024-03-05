import os
import sys
from re import split


def duplicate_file(file, num=1, *args):
    print("============")
    if len(sys.argv) >= 3:
        num = int(sys.argv[2])
        new_name = sys.argv[3]
    elif len(sys.argv) >= 4:
        new_type = sys.argv[4]

    file_name_split = split("-|\.", file)
    print(file_name_split)
    file_type = file_name_split[2]
    old_file_num = int(file_name_split[0])

    num += old_file_num
    sum = num
    new_file_num = str(sum)
    file_name_split[0] = new_file_num

    if len(sys.argv) >= 3:
        file_name_split[1] = new_name
    new_file_name = f"{file_name_split[0]}-{file_name_split[1]}.{file_type}"

    if not os.path.isfile(file):
        print(f"{file} does not exist.")
        print("============")
        return
    elif os.path.isfile(new_file_name):
        print(f"{new_file_name} already exists.")
        print("============")
        return
    else:
        print(f"You're creating {new_file_name} from {file}.")
        with open(file, "r") as file_a:
            content = file_a.read()
        with open(new_file_name, "w") as new_file:
            new_file.write(content)
    print("============")


if __name__ == "__main__":
    duplicate_file(sys.argv[1], num=1)
