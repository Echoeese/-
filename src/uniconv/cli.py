import typer
from .dispatcher import convert as dispatch_convert

app = typer.Typer(help="uniconv - universal file converter (prototype)")


@app.command()
def convert(
    input_path: str = typer.Argument(..., help="Path to input file"),
    to: str = typer.Option(..., "-t", "--to", help="Output format or filename extension (e.g. mp4, mp3, png)"),
    ffmpeg_args: str = typer.Option("", help="Additional ffmpeg CLI args as a single string"),
):
    """Convert INPUT_PATH to format TO using best-effort adapter selection.

    Example:
      uniconv convert video.mov --to mp4 --ffmpeg-args "-c:v libx264 -crf 23"
    """
    try:
        result = dispatch_convert(input_path, to, ffmpeg_args)
        if result.get("success"):
            typer.secho(f"Conversion successful: {result.get('output')}", fg=typer.colors.GREEN)
        else:
            typer.secho(f"Conversion failed: {result.get('error')}", fg=typer.colors.RED)
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)


if __name__ == "__main__":
    app()
