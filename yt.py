import customtkinter as tk
from tkinter import messagebox
from yt_dlp import YoutubeDL

ydl_opts = {}

def dwl_vid(video_url):
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return "Download complete."
    except Exception as e:
        return f"Error: {e}"

def download_video():
    link = url_entry.get().strip()
    if not link:
        messagebox.showerror("Error", "URL field cannot be empty!")
        return

    result = dwl_vid(link)
    messagebox.showinfo("Status", result)

# Create the GUI
root = tk.CTk()
root.title("YouTube Video Downloader")
root.geometry("400x120")

# URL Entry
url_label = tk.CTkLabel(root, text="Enter YouTube URL:")
url_label.pack(pady=5)

url_entry = tk.CTkEntry(root, width=350)
url_entry.pack(pady=5)

# Buttons
download_button = tk.CTkButton(root, text="Download", command=download_video, width=80)
download_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
