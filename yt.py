import customtkinter as tk
from tkinter import messagebox
from yt_dlp import YoutubeDL
import threading

ydl_opts = {}

def dwl_vid(video_url, progress_callback):
    try:
        class MyLogger:
            def debug(self, msg):
                pass

            def warning(self, msg):
                pass

            def error(self, msg):
                messagebox.showerror("Error", msg)

        def hook(d):
            if d['status'] == 'downloading':
                downloaded = d.get('downloaded_bytes', 0)
                total = d.get('total_bytes', 1)
                progress = int(downloaded / total * 100)
                progress_callback(progress)

        ydl_opts_with_hooks = {
            'progress_hooks': [hook],
            'logger': MyLogger()
        }

        with YoutubeDL(ydl_opts_with_hooks) as ydl:
            ydl.download([video_url])
        return "Download complete."
    except Exception as e:
        return f"Error: {e}"

def download_video():
    link = url_entry.get().strip()
    if not link:
        messagebox.showerror("Error", "URL field cannot be empty!")
        return

    def run_download():
        result = dwl_vid(link, update_progress)
        messagebox.showinfo("Status", result)
        progress_bar.set(0)
        progress_label.configure(text="Download Progress: 0%")

    threading.Thread(target=run_download, daemon=True).start()

def update_progress(value):
    progress_bar.set(value / 100)
    progress_label.configure(text=f"Download Progress: {value}%")

# Create the GUI
root = tk.CTk()
root.title("YouTube Video Downloader")
root.geometry("400x200")

# URL Entry
url_label = tk.CTkLabel(root, text="Enter YouTube URL:")
url_label.pack(pady=5)

url_entry = tk.CTkEntry(root, width=350)
url_entry.pack(pady=5)

# Progress Bar
progress_bar = tk.CTkProgressBar(root, width=350)
progress_bar.pack(pady=10)
progress_bar.set(0)

progress_label = tk.CTkLabel(root, text="Download Progress: 0%")
progress_label.pack(pady=5)

# Buttons
download_button = tk.CTkButton(root, text="Download", command=download_video, width=80)
download_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
