# Example code, write your program here
import itertools
import json
from collections import defaultdict
from pathlib import Path


def read_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def main():
    input_dir = Path("data/")
    output_dir = Path("output/")
    for subdir in input_dir.iterdir():
        files_by_suffix = defaultdict(list)
        for file in subdir.iterdir():
            files_by_suffix[file.suffix].append(file)

        # Concat txt files.
        txt_files = sorted(files_by_suffix[".txt"])
        if len(txt_files) > 0:
            all_content = [read_file(file) for file in txt_files]
            with (output_dir / f"{subdir.stem}.txt").open("w") as f:
                f.write("".join(all_content))

        # Concat JSON files.
        json_files = sorted(files_by_suffix[".json"])
        if len(json_files) > 0:
            all_jsons = itertools.chain.from_iterable(json.loads(read_file(file)) for file in json_files)
            edited_jsons = [
                {**j, "id": idx + 1}
                for idx, j in enumerate(all_jsons)
            ]
            with (output_dir / f"{subdir.stem}.json").open("w") as f:
                json.dump(edited_jsons, f)


if __name__ == '__main__':
    main()
