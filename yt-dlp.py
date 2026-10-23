import sys
from typing import Any
import deno
from yt_dlp import YoutubeDL


def download_video(url: str):
  deno_path = deno.find_deno_bin()

  ydl_opts: dict[str, Any] = {
      'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/best[ext=mp4]',
      'merge_output_format': 'mp4',
      'js_runtimes': {'deno': {'path': deno_path}},
      # Explicitly allow downloading/using the EJS challenge solver component
      'remote_components': {'ejs': 'github'},
  }

  print(f'Connecting and downloading highest quality MP4 for:\n{url}\n')

  try:
    with YoutubeDL(ydl_opts) as ydl:
      ydl.download([url])
    print('\nDownload completed successfully!')
  except Exception as e:
    print(f'\nAn error occurred: {e}', file=sys.stderr)


if __name__ == '__main__':
  if len(sys.argv) > 1:
    video_url = sys.argv[1]
  else:
    video_url = input('Enter YouTube video URL: ').strip()

  if video_url:
    download_video(video_url)
  else:
    print('Error: No URL provided.')