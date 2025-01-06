

### README: YouTube Video Downloader

---

#### Overview
This is a Python-based desktop application for downloading YouTube videos using the **yt-dlp** library. It features a graphical user interface (GUI) built with the **customtkinter** module, making it simple and user-friendly.

---

#### Features
- **Download YouTube videos**: Simply paste a valid YouTube URL and click the "Download" button.
- **Error handling**: Alerts the user if the URL field is empty or if an error occurs during the download process.
- **Minimal design**: Compact GUI with intuitive controls.

---

#### Prerequisites
Ensure the following dependencies are installed in your environment:

1. **Python 3.x**: Install Python from [python.org](https://www.python.org/).
2. **yt-dlp**: Install using pip:
   ```bash
   pip install yt-dlp
   ```
3. **customtkinter**: Install using pip:
   ```bash
   pip install customtkinter
   ```

---

#### Installation and Usage

1. **Clone or download the repository**.
2. Save the script as `youtube_downloader.py` (or any name you prefer).
3. Open a terminal or command prompt in the script's directory.
4. Run the script:
   ```bash
   python youtube_downloader.py
   ```
5. Enter a valid YouTube URL in the input field of the GUI and click "Download".

---

#### How It Works

1. **Input field**: Accepts the YouTube video URL.
2. **Download function**: 
   - Utilizes the `YoutubeDL` class from the **yt-dlp** library to handle the video download.
   - If successful, shows a "Download complete" message.
   - If an error occurs, displays an error message.

---

#### Customization
You can customize the download options by modifying the `ydl_opts` dictionary. For example:

```python
ydl_opts = {
    'format': 'bestvideo+bestaudio',
    'outtmpl': 'downloads/%(title)s.%(ext)s',
}
```

---

#### Notes
- This application does not support downloading playlists by default. Modify the code to include playlist handling if required.
- Ensure proper permissions for the directory where videos will be downloaded.

---

#### Troubleshooting
- **Missing dependencies**: Install missing packages using pip.
- **Download errors**: Check your internet connection or ensure the URL is valid.
- **Permission issues**: Verify that the script has write permissions for the target directory.

---

Enjoy your video downloads! 🚀
