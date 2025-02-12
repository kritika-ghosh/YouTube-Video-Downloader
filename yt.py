import customtkinter as tk
from tkinter import messagebox, filedialog
from yt_dlp import YoutubeDL
import threading
import time

download_location = ""

def select_download_location():
    global download_location
    download_location = filedialog.askdirectory()
    if download_location:
        location_label.configure(text=f"Download Location: {download_location}")
    else:
        location_label.configure(text="Download Location: Not selected")

# Track progress for smooth updates
prev_progress = 0
is_downloading = False

def dwl_vid(video_url, progress_callback, download_type):
    global prev_progress, is_downloading
    try:
        if not download_location:
            return "Error: Download location not selected."

        class MyLogger:
            def debug(self, msg):
                pass

            def warning(self, msg):
                pass

            def error(self, msg):
                messagebox.showerror("Error", msg)

        prev_progress = 0  # Reset progress
        is_downloading = True  # Mark as downloading

        def hook(d):
            global prev_progress
            if d['status'] == 'downloading':
                downloaded = d.get('downloaded_bytes', 0)
                total = d.get('total_bytes') or d.get('total_bytes_estimate', 1)  # Handle missing total size
                progress = int(downloaded / total * 100)
                
                if progress > prev_progress:
                    smooth_progress_update(prev_progress, progress, progress_callback)
                    prev_progress = progress

        ydl_opts_with_hooks = {
            'format': 'bestvideo+bestaudio/best' if download_type == "MP4 (Video)" else 'bestaudio/best',
            'outtmpl': f'{download_location}/%(title)s.%(ext)s',
            'progress_hooks': [hook],
            'logger': MyLogger()
        }
        
        if download_type == "MP3 (Audio)":
            ydl_opts_with_hooks['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]

        with YoutubeDL(ydl_opts_with_hooks) as ydl:
            ydl.download([video_url])

        is_downloading = False
        smooth_progress_update(prev_progress, 100, progress_callback)  # Ensure it reaches 100%
        return "Download complete."
    except Exception as e:
        is_downloading = False
        return f"Error: {e}"

def smooth_progress_update(start, end, callback):
    """Gradually update the progress bar for a smooth effect."""
    def step(progress):
        if progress <= end and is_downloading:
            callback(progress)
            root.after(50, lambda: step(progress + 2))  # Update every 50ms
    step(start)

def start_download():
    link = url_entry.get().strip()
    download_type = type_dropdown.get()
    if not link:
        messagebox.showerror("Error", "URL field cannot be empty!")
        return
    if not download_type:
        messagebox.showerror("Error", "Please select a download type!")
        return

    def run_download():
        result = dwl_vid(link, update_progress, download_type)
        root.after(100, lambda: messagebox.showinfo("Status", result))
        root.after(100, lambda: progress_bar.set(0))
        root.after(100, lambda: progress_label.configure(text="Download Progress: 0%"))

    threading.Thread(target=run_download, daemon=True).start()

def update_progress(value):
    progress_bar.set(value / 100)
    progress_label.configure(text=f"Download Progress: {value}%")

# GUI Setup
root = tk.CTk()
root.title("YouTube Downloader")
root.geometry("500x350")

url_label = tk.CTkLabel(root, text="Enter YouTube URL:")
url_label.pack(pady=5)

url_entry = tk.CTkEntry(root, width=450)
url_entry.pack(pady=5)

type_label = tk.CTkLabel(root, text="Select Download Type:")
type_label.pack(pady=5)

type_dropdown = tk.CTkComboBox(root, values=["MP4 (Video)", "MP3 (Audio)"])
type_dropdown.pack(pady=5)

location_label = tk.CTkLabel(root, text="Download Location: Not selected")
location_label.pack(pady=5)

location_button = tk.CTkButton(root, text="Select Location", command=select_download_location, width=150)
location_button.pack(pady=5)

progress_bar = tk.CTkProgressBar(root, width=450)
progress_bar.pack(pady=10)
progress_bar.set(0)

progress_label = tk.CTkLabel(root, text="Download Progress: 0%")
progress_label.pack(pady=5)

download_button = tk.CTkButton(root, text="Download", command=start_download, width=100)
download_button.pack(pady=10)

root.mainloop()
