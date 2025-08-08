from pytubefix import YouTube
from pytubefix.cli import on_progress
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        ys = yt.streams.get_highest_resolution()
        ys.download(output_path=save_path)
        print(f"Video downloaded successfully {yt.title}")
    except Exception as e:
        print(e)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please add your youtube url: ")
    save_dir = open_file_dialog()

    if not save_dir:
        print("Please select a folder")
    else:
        download_video(video_url, save_dir)
