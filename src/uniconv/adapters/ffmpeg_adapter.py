import shlex
import subprocess
from typing import Dict


def ffmpeg_convert(input_path: str, output_path: str, extra_args: str = "") -> Dict:
    """Run a generic ffmpeg conversion: ffmpeg -y -i input [extra_args] output

    This is intentionally minimal: users can pass codec/quality args via extra_args.
    """
    cmd = ["ffmpeg", "-y", "-i", input_path]
    if extra_args:
        cmd += shlex.split(extra_args)
    cmd.append(output_path)

    try:
        completed = subprocess.run(cmd, capture_output=True, text=True, check=False)
        success = completed.returncode == 0
        return {
            "success": success,
            "returncode": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
            "output": output_path if success else None,
            "error": None if success else "ffmpeg failed",
        }
    except FileNotFoundError:
        return {"success": False, "error": "ffmpeg not found on PATH"}
    except Exception as e:
        return {"success": False, "error": str(e)}
