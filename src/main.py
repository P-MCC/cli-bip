import typer
from helpers import getImageList

app = typer.Typer()

@app.command()
def hello(path: str = typer.Option(None, help='Path to the directory containing image files')):
    """
    Main function that takes an optional path argument and prints the list of image names.
    """
    typer.echo(path)
    try:
        if path:
            # Perform existence check inside the function
            if not typer.confirm(f"Are you sure you want to process images in '{path}'?"):
                typer.echo("Operation canceled.")
                return
            
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

if __name__ == '__main__':
    app()
