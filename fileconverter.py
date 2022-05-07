#!/usr/bin/env python3
import os
from pathlib import Path
from pydub import AudioSegment
import typer

app = typer.Typer()

audio_extensions = ['.mp3', '.wav', '.ogg', '.flac']


@app.command()
def convert(file: str):
    filepath = f"{os.getcwd()}/{file}"
    if os.path.exists(filepath) == False and os.path.exists(file):
        filepath = file
    elif os.path.exists(filepath) == False and os.path.exists(file.replace('~', str(Path.home()))):
        filepath = file.replace('~', str(Path.home()))
    else:
        typer.echo(typer.style("File not exists!", fg=typer.colors.RED))
        return
    # File extension
    file_extension = '.' + filepath.split('.')[-1]

    typer.echo(typer.style(
        f'To which extension convert the {os.path.basename(file)}:', fg=typer.colors.GREEN))

    # Print file extensions to which file can be converted
    for extension in audio_extensions:
        extension_index = audio_extensions.index(extension)
        if extension == file_extension:
            typer.echo(typer.style(
                f'[{extension_index}]{extension}', fg=typer.colors.BRIGHT_GREEN, bold=True))
        else:
            typer.echo(typer.style(
                f'[{extension_index}]{extension}', fg=typer.colors.WHITE))

    # Select file extension
    selected_option = audio_extensions[int(typer.prompt(typer.style(
        "Select option", fg=typer.colors.BRIGHT_BLACK, bold=True)))]
    if selected_option == file_extension:
        typer.echo(typer.style(
            'An existing file extension was selected!', fg=typer.colors.RED))
    else:
        # File extension == TXT
        if file_extension in audio_extensions:
            convert_audio(filepath, selected_option, file_extension)
        else:
            typer.echo(typer.style(
            'No audio file selected!', fg=typer.colors.RED))

def convert_audio(path: str, convert_to: str, file_extension: str):
    # Save location
    save_location = f"{os.getcwd()}/{Path(path).stem}{convert_to}"

    # Converting
    audio_file = AudioSegment.from_file(
        path, format=file_extension.replace('.', ''))
    audio_file.export(save_location, format=convert_to.replace('.', ''))


if __name__ == "__main__":
    app()
