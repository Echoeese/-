import os
import pathlib
import filetype
from .adapters.ffmpeg_adapter import ffmpeg_convert


def convert(input_path: str, to: str, ffmpeg_args: str = "") -> dict:
    """Dispatch conversion based on detected file type.

    Currently supports audio/video/image via ffmpeg adapter.
    """
    input_path = str(input_path)
    if not os.path.exists(input_path):
        return {"success": False, "error": "input file not found"}

    kind = filetype.guess(input_path)
    mime = kind.mime if kind else None

    # Build output path: same dir, same stem + new ext
    p = pathlib.Path(input_path)
    out_ext = to.lstrip('.')
    output_path = str(p.with_suffix('.' + out_ext))

    # Simple dispatch rules
    if mime and (mime.startswith('video') or mime.startswith('audio') or mime.startswith('image')):
        res = ffmpeg_convert(input_path, output_path, ffmpeg_args)
        return res

    return {"success": False, "error": f"no adapter for mime={mime}. Try using --ffmpeg-args or implement adapter."}
