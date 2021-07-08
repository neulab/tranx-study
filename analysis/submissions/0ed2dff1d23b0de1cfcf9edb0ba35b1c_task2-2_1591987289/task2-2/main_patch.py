# Example code, write your program here
from pathlib import Path


def main():
    input_dir = Path("data/")
    output_dir = Path("output/")
    for file in input_dir.iterdir():
        if file.suffix != ".txt": continue
        lines = []
        with file.open("r", encoding="ISO-8859-15") as f:
            for line in f:
                lines.append(line.strip())
        with (output_dir / file.name).open("w", encoding="utf-8") as f:
            f.write("\n".join(lines))


if __name__ == '__main__':
    main()
