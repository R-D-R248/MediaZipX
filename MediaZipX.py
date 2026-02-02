#Contributors:
#CodeR-D-R(R-D-R248)
from colorama import Fore, Back, Style, init
import os
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
import ffmpeg
import re
import zipfile
import requests
import sys

init(autoreset=True)

def logof():
    media_txt = """
███╗   ███╗███████╗██████╗ ██╗ █████╗ 
████╗ ████║██╔════╝██╔══██╗██║██╔══██╗
██╔████╔██║█████╗  ██║  ██║██║███████║
██║╚██╔╝██║██╔══╝  ██║  ██║██║██╔══██║
██║ ╚═╝ ██║███████╗██████╔╝██║██║  ██║
╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝
    """
    zip_txt = """
███████╗██╗██████╗ 
╚══███╔╝██║██╔══██╗
  ███╔╝ ██║██████╔╝
 ███╔╝  ██║██╔═══╝ 
███████╗██║██║     
╚══════╝╚═╝╚═╝     
    """
    x_txt = """
██╗  ██╗
╚██╗██╔╝
 ╚███╔╝ 
 ██╔██╗ 
██╔╝ ██╗
╚═╝  ╚═╝
    """
    media_l = [line for line in media_txt.splitlines() if line.strip()]
    zip_l = [line for line in zip_txt.splitlines() if line.strip()]
    x_l = [line for line in x_txt.splitlines() if line.strip()]
    for i in range(0,6):
        print(Fore.BLUE + media_l[i], end="")
        print(Fore.YELLOW + zip_l[i], end="")
        print(Fore.RED + x_l[i], end="")
        print()
        
    return None

directory_path="C:\\ffmpeg"
if os.path.isdir(directory_path):
    pass
else:
    url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl-shared.zip"
    save_folder = r"C:\ffmpeg"
    save_path = os.path.join(save_folder, "ffmpeg.zip")

    os.makedirs(save_folder, exist_ok=True)

    print("Downloading FFmpeg... This may take a few minutes.")

    response = requests.get(url, stream=True)

    with open(save_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    zip_path = r"C:\ffmpeg\ffmpeg.zip"
    extract_to = r"C:\ffmpeg"

    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(extract_to)
    for name in os.listdir(save_folder):
        if name.startswith("ffmpeg"):
            ffmpeg_bin = os.path.join(save_folder, name, "bin")
            os.environ["PATH"] += os.pathsep + ffmpeg_bin
            break
    os.remove(save_path)
    print(input("Click Enter to finish Setup"))
    
def get_ffmpeg_bin(path="C:\\ffmpeg"):
    for name in os.listdir(path):
        full_path = os.path.join(path, name, "bin")
        if os.path.isdir(full_path):
            return full_path
    return path

ffmpeg_bin = get_ffmpeg_bin()

while True:
    os.system("cls")
    logof()
    print(Fore.BLUE + "MediaZipX 1.2")
    print("by Code" + Fore.RED + "R" + Fore.WHITE + "-" + Fore.BLUE + "D" + Fore.WHITE + "-" + Fore.RED + "R")
    print("https://github.com/R-D-R248")
    print(Fore.WHITE + Style.DIM + "-"*96)
    print(Fore.RED + "DISCLAIMER!")
    print(Fore.WHITE + "The creator (Code" + Fore.RED + "R" + Fore.WHITE + "-" + Fore.BLUE + "D" + Fore.WHITE + "-" + Fore.RED + "R"+ Fore.WHITE +") is not responsible for")
    print(Fore.WHITE + "Misuse of MediaZipX in " + Fore.RED + "violation" + Fore.WHITE + " of YouTube’s or other platforms’ Terms of Service.")
    print(Fore.WHITE + Style.DIM + "-"*96)
    print(Fore.BLUE + Style.BRIGHT + "[1]Download from YouTube")
    print(Fore.BLUE + Style.BRIGHT + "[2]About")
    print(Fore.RED + "[3]Exit")
    choice = input("Choose(1-3): ")
    if choice == "3":
        sys.exit()
    elif choice == "2":
        os.system("cls")
        print(Style.BRIGHT + "About MediaZipX")
        print("MediaZipX is a Python-based Media Downloader designed to make Downloading videos and audio easy and accessible.")
        print("Developed " + "by Code" + Fore.RED + "R" + Fore.WHITE + "-" + Fore.BLUE + "D" + Fore.WHITE + "-" + Fore.RED + "R")
        print("YouTube is a trademark of Google LLC. MediaZipX is not affiliated with, endorsed by, or sponsored by YouTube or Google.")
        print(input("Press Enter to Return to Menu"))
        os.system("cls")
        continue
    elif choice == "1":
        while True:
            os.system("cls")
            print(Fore.RED + Style.BRIGHT + "YouTube" + Fore.WHITE + " Downloader")
            print(Fore.BLUE + Style.BRIGHT + "[1]MP4(No Audio)")
            print(Fore.BLUE + Style.BRIGHT + "[2]MP3(Audio)")
            print(Fore.BLUE + Style.BRIGHT + "[3]MP4")
            print(Fore.RED + "[4]Back to Menu")
            choice_a = input("Choose(1-4): ")
            if choice_a == "1":
                url = input("Enter the URL: ")
                ydl_opts = {
                    "format": "bestvideo[ext=mp4]/bestvideo",
                    "outtmpl": "%(title)s.%(ext)s",
                    "restrictfilenames": True,
                    "progress_hooks": [lambda d: print(f"Progress: {d['_percent_str']}") if d['status']=='downloading' else None],
                    "http_headers": {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                        "Referer": "https://www.youtube.com/",
                    },
                    "geo_bypass": True,
                    "retries": 10,
                    "continuedl": True,
                    "nocheckcertificate": True,
                }
    
            elif choice_a == "2":
                url = input("Enter the URL: ")
                ydl_opts = {
                    "format": "bestaudio",
                    "outtmpl": "%(title)s.mp3",
                    "restrictfilenames": True,
                    "progress_hooks": [lambda d: print(f"Progress: {d['_percent_str']}") if d['status']=='downloading' else None],
                    "http_headers": {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                        "Referer": "https://www.youtube.com/",
                    },
                    "geo_bypass": True,
                    "retries": 10,
                    "continuedl": True,
                    "nocheckcertificate": True,
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }],
                    "ffmpeg_location": ffmpeg_bin,

                }
            elif choice_a == "3":
                url = input("Enter the URL:")
                ydl_opts = {
                    "format": "bestvideo+bestaudio/best",
                    "outtmpl": "%(title)s.%(ext)s",
                    "restrictfilenames": True,
                    "merge_output_format": "mp4",
                    "ffmpeg_location": ffmpeg_bin,
                    "progress_hooks": [lambda d: print(f"Progress: {d['_percent_str']}") if d['status']=='downloading' else None],
                    "http_headers": {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                        "Referer": "https://www.youtube.com/",
                    },
                    "geo_bypass": True,
                    "retries": 10,
                    "continuedl": True,
                    "nocheckcertificate": True,
                }
            
            elif choice_a == "4":
                break
            
            else:
                os.system("cls")
                print(Fore.RED + Style.BRIGHT + "Invalid Choice")
                print(input("Press Enter to Return to Menu"))
                os.system("cls")
                continue
            try:
                os.system("cls")
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                os.system("cls")
                print("Download Success")
            except DownloadError as e:
                os.system("cls")
                print(f"Download failed: {e}")
            except Exception as e:
                os.system("cls")
                print(f"An error occurred: {e}")


                
            print(input("Click Enter to Download more Videos"))
            

    else:
        os.system("cls")
        print(Fore.RED + Style.BRIGHT + "Invalid Choice")
        print(input("Press Enter to Return to Menu"))
        os.system("cls")
        continue
