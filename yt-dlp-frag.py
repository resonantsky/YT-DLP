import sys
from typing import Any
import deno
from yt_dlp import YoutubeDL


def download_video(url: str):
  deno_path = deno.find_deno_bin()

  ydl_opts: dict[str, Any] = {
      'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/best[ext=mp4]/best',
      'merge_output_format': 'mp4',
      'js_runtimes': {'deno': {'path': deno_path}},
      'remote_components': {'ejs': 'github'},
      # --- Fix for 410 Gone / Expired Fragments ---
      # Force ffmpeg to handle the HLS stream download instead of python's hlsnative
      'hls_prefer_native': False,
      # Mimic a standard desktop browser User-Agent so the CDN doesn't reject chunk requests
      'http_headers': {
          'User-Agent': (
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
              'AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/124.0.0.0 Safari/537.36'
          ),
          'Accept': '*/*',
          'Accept-Language': 'en-US,en;q=0.5',
      },
      'fragment_retries': 5,
      'retries': 5,
  }

  print(f'Connecting and downloading video for:\n{url}\n')

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
    video_url = input('Enter video URL: ').strip()

  if video_url:
    download_video(video_url)
  else:
    print('Error: No URL provided.')