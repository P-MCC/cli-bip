import click
from .helpers import getImageList

@click.group()
def commands():
    """
    CLI tool for image processing.
    """
    pass

@click.command()
@click.option('--path', type=click.Path(exists=True, file_okay=False, resolve_path=True), help='Path to the directory containing image files.')
# @click.argument('path', nargs=-1, type=click.Path())
def hello(path):
    """
    Main function that takes an optional path argument and prints the list of image names.
    """
    for filename in path:
        click.echo(filename)
    try:
        if path:
            image_files = getImageList(path)
            if image_files:
                print("List of image files:")
                for img_name in image_files:
                    print(img_name)
            else:
                print("No image files found in the specified directory.")
        else:
            print("Please provide a path to the directory containing image files using --path.")
    except Exception as e:
        print(f"An error occurred: {e}")


commands.add_command(hello)

if __name__ == '__main__':
    commands()