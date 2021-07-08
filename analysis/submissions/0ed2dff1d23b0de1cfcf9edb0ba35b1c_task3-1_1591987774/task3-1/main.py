# Example code, write your program here
import os
import re
import shutil

DATE_REGEX = re.compile(r"(\d{4})-(\d\d)-(\d\d)")


def replace_name(name: str) -> str:
    return DATE_REGEX.sub(r"\2-\3-\1", name)


def main():
    input_dir = "data/"
    output_dir = "output/"
    for dirname, dirnames, filenames in os.walk(input_dir):
        target_path = replace_name(os.path.join(output_dir, *dirname.split("/")[1:]))
        for subdirname in dirnames:
            os.makedirs(os.path.join(target_path, replace_name(subdirname)))
        for filename in filenames:
            shutil.copy2(os.path.join(dirname, filename),
                         os.path.join(target_path, replace_name(filename)))


if __name__ == '__main__':
    main()
