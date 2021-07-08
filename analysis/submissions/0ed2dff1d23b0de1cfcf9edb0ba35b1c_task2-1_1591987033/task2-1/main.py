# Example code, write your program here
import csv
from pathlib import Path


def main():
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        edited = []
        for line in reader:
            edited.append(line[1:-1])
    output_dir = Path("output/")
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "output.csv").open("w") as f:
        writer = csv.writer(f)
        for line in edited:
            writer.writerow(line)


if __name__ == '__main__':
    main()
