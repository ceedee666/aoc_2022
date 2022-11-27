from pathlib import Path

import typer


app = typer.Typer()


def read_input_file(input_file_path):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda l: l.strip(), lines))


@app.command()
def part1(input_file: str):
    data = read_input_file(input_file)

    print(f"The input data is: {data}")


if __name__ == "__main__":
    app()
