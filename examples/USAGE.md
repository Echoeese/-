# Usage examples for uniconv

Convert a video to mp4:

  python -m uniconv convert examples/sample.mov --to mp4

Convert an image to png:

  python -m uniconv convert examples/photo.heic --to png

Pass extra ffmpeg args (e.g. re-encode with libx264):

  python -m uniconv convert examples/video.mov --to mp4 --ffmpeg-args "-c:v libx264 -crf 23"

Notes
-----
- These examples assume ffmpeg is installed on your PATH or available in the runtime (Docker image builds ffmpeg into the image).
