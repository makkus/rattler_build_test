import os
import sys
from pathlib import Path

import click


@click.command()
@click.argument('input_file')
@click.pass_context
def cli(ctx, input_file: str):

    current_dir = os.getcwd()
    current_dir_path = Path(current_dir).absolute()

    print(f"Input file: {input_file}")
    input_file_path = Path(input_file).absolute()


    print("Current folder contents:")
    for file in current_dir_path.iterdir():
        print(file)

    if not input_file_path.exists():
        print(f"File {input_file_path} does not exist")
        sys.exit(1)


    sys.exit(0)

