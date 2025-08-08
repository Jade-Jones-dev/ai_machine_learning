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

url = "https://www.youtube.com/watch?v=hmtuvNfytjM"
save_path = "/Users/jade/Desktop/REPOS/ai_machine_learning/python_projects/youtube"

download_video(url, save_path)

def open_file_dialog():
    pass

root = tk.Tk()
root.withdraw()
