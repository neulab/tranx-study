# Example code, write your program here
import os


def list_text_file_paths(dir):
    def _():
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".txt"):
                    yield os.path.join(root, file)
    return tuple(_())


def strip_fh_contents(fh):
    for line in fh:
        stripped_line = line.strip()
        if stripped_line:
            yield stripped_line + "\n"


def get_output_filepath(source_filepath):
    original_filename = os.path.basename(source_filepath)
    return os.path.join("output", original_filename)

text_filepath_seq = list_text_file_paths("data")

for filepath in text_filepath_seq:
    with open(filepath, encoding="ISO-8859-15") as file_in:
        gen_stripped_contents = strip_fh_contents(file_in)
        output_filepath = get_output_filepath(filepath)
        with open(output_filepath, 'w') as file_out:
            file_out.writelines(gen_stripped_contents)
