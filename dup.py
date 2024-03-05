import os
import sys


def duplicate_file(file, num=1):
    print("============")

    num = int(sys.argv[2])

    file_name_split = file.split("-")
    old_file_num = int(file_name_split[0])
    num += old_file_num
    sum = num
    new_file_num = str(sum)
    file_name_split[0] = new_file_num
    new_file_name = "-".join(file_name_split)

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
