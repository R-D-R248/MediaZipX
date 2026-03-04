#Contributors:
#CodeR-D-R(R-D-R248): https://github.com/R-D-R248

#Special Thanks to:
#thegamerprogrammer: https://github.com/Thegamerprogrammer
import time
version = "MediaZipX 1.6.1"
from colorama import Fore, Back, Style, init
import os
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
import zipfile
import requests
import sys
import random
import webbrowser
import keyboard
#These are the User Agents or Fake Cookies
#This Idea has been implemented thanks to https://github.com/Thegamerprogrammer/CrystalMedia
fake_cookies = [
    # Windows 10
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    # macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.2 Safari/605.1.15",
    # Linux
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:146.0) Gecko/20100101 Firefox/146.0",
]

#Download Path
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

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
    
def get_ffmpeg_bin(path):
    for name in os.listdir(path):
        full_path = os.path.join(path, name, "bin")
        if os.path.isdir(full_path):
            return full_path
    return path

ffmpeg_bin = get_ffmpeg_bin(path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "ffmpeg"))

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"\rProgress: {d.get('_percent_str','0%')}", end="")

while True:
    os.system("cls")
    time.sleep(0.5)
    logof()
    print(Fore.BLUE + f"{version}")
    print("by Code" + Fore.RED + "R" + Fore.WHITE + "-" + Fore.BLUE + "D" + Fore.WHITE + "-" + Fore.RED + "R")
    print("https://github.com/R-D-R248")
    print(Fore.WHITE + Style.DIM + "-"*96)
    print(Fore.RED + "DISCLAIMER!")
    print(Fore.WHITE + "The creator (Code" + Fore.RED + "R" + Fore.WHITE + "-" + Fore.BLUE + "D" + Fore.WHITE + "-" + Fore.RED + "R"+ Fore.WHITE +") is not responsible for")
    print(Fore.WHITE + "Misuse of MediaZipX in " + Fore.RED + "violation" + Fore.WHITE + " of YouTube’s or other platforms’ Terms of Service.")
    print(Fore.WHITE + Style.DIM + "-"*96)
    print(Fore.BLUE + Style.BRIGHT + "[1]Download from YouTube")
    print(Fore.BLUE + Style.BRIGHT + "[2]About")
    print(Fore.BLUE + "[3]Troubleshoorting")
    print(Fore.RED + "[4]Exit")
    choice = keyboard.read_key()
    if choice == "4":
        sys.exit()
    elif choice == "3":
        time.sleep(0.5)
        while True:
            os.system("cls")
            print(Style.BRIGHT + "Options")
            print("[1]Report an Error or Suggest a Feature")
            print("[2]Exit to Main Menu")
            choice_a = keyboard.read_key()                 
            if choice_a == "1":
                os.system("cls")
                webbrowser.open("https://github.com/R-D-R248/MediaZipX/issues")
                print("Check the New Browser Window\nClick Enter to Exit")
                print(input())
            elif choice_a == "2":
                break
            
            else:
                os.system("cls")
                print(Fore.RED + Style.BRIGHT + "Invalid Choice")
                print(input("Press Enter to Return to Options"))
                os.system("cls")
                continue
    elif choice == "2":
        time.sleep(0.5)
        os.system("cls")
        print(Style.BRIGHT + "About MediaZipX")
        print("MediaZipX is a Python-based Media Downloader designed to make Downloading videos and audio easy and accessible.")
        print("Developed " + "by Code" + Fore.RED + "R" + Fore.WHITE + "-" + Fore.BLUE + "D" + Fore.WHITE + "-" + Fore.RED + "R")
        print("YouTube is a trademark of Google LLC. MediaZipX is not affiliated with, endorsed by, or sponsored by YouTube or Google.")
        print("Chrome is a trademark of Google LLC. MediaZipX is not affiliated with, endorsed by, or sponsored by Chrome or Google.")
        print("Edge is a trademark of Microsoft. MediaZipX is not affiliated with, endorsed by, or sponsored by Edge or Microsoft.")

        print(input("Press Enter to Return to Menu"))
        os.system("cls")
        continue
    elif choice == "1":
        time.sleep(0.5)
        while True:
            os.system("cls")
            print(Fore.RED + Style.BRIGHT + "YouTube" + Fore.WHITE + " Downloader")
            print(Fore.BLUE + Style.BRIGHT + "[1]MP4(Best Quality Video)")
            print(Fore.BLUE + Style.BRIGHT + "[2]MP3(High Quality Audio)")
            print(Fore.BLUE + Style.BRIGHT + "[3]WAV(High Quality Audio)")
            print(Fore.BLUE + Style.BRIGHT + "[4]FLAC(Best Quality Audio)")
            print(Fore.BLUE + Style.BRIGHT + "[5]MP4(Compact Video)")
            print(Fore.BLUE + Style.BRIGHT + "[6]MP4(No Audio)")
            print(Fore.RED + "[7]Back to Menu")
            choice_a = keyboard.read_key()
            
            agent = random.choice(fake_cookies)
            if choice_a == "6":
                url = input("Enter the URL: ")
                ydl_opts = {
                    "format": "bestvideo[ext=mp4]/bestvideo",
                    "outtmpl": os.path.join(downloads_path, "%(title)s.%(ext)s"),
                    "restrictfilenames": True,
                    "progress_hooks": [progress_hook],
                    "retries": 10,
                    "http_headers": {"User-Agent": agent},
                }
    
            elif choice_a == "2":
                url = input("Enter the URL: ")
                ydl_opts = {
                    "format": "bestaudio[ext=m4a]",
                    "outtmpl": os.path.join(downloads_path, "%(title)s.%(ext)s"),
                    "restrictfilenames": True,
                    "progress_hooks": [progress_hook],
                    "retries": 10,
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }],
                    "ffmpeg_location": ffmpeg_bin,
                    "http_headers": {"User-Agent": agent},

                }
            elif choice_a == "3":
                url = input("Enter the URL: ")
                ydl_opts = {
                    "format": "bestaudio[ext=m4a]",
                    "outtmpl": os.path.join(downloads_path, "%(title)s.%(ext)s"),
                    "restrictfilenames": True,
                    "progress_hooks": [progress_hook],
                    "retries": 10,
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "wav",
                        "preferredquality": "192",
                    }],
                    "ffmpeg_location": ffmpeg_bin,
                    "http_headers": {"User-Agent": agent},

                }
            elif choice_a == "4":
                url = input("Enter the URL: ")
                ydl_opts = {
                    "format": "bestaudio[ext=m4a]",
                    "outtmpl": os.path.join(downloads_path, "%(title)s.%(ext)s"),
                    "restrictfilenames": True,
                    "progress_hooks": [progress_hook],
                    
                    "retries": 10,
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "flac",
                        "preferredquality": "300",
                    }],
                    "ffmpeg_location": ffmpeg_bin,
                    "http_headers": {"User-Agent": agent},

                }
            elif choice_a == "1":
                url = input("Enter the URL:")
                ydl_opts = {
                    "format": "bestvideo[height<=2160]+bestaudio[ext=m4a]/best",
                    "outtmpl": os.path.join(downloads_path, "%(title)s.%(ext)s"),
                    "restrictfilenames": True,
                    "merge_output_format": "mp4",
                    "ffmpeg_location": ffmpeg_bin,
                    "progress_hooks": [progress_hook],
                    "http_headers": {"User-Agent": agent},
                    "retries": 10,
                }
            elif choice_a == "5":
                url = input("Enter the URL:")
                ydl_opts = {
                    "format": "bestvideo[height<=720]+bestaudio[ext=m4a]/best[ext=mp4][height<=720]",
                    "outtmpl": os.path.join(downloads_path, "%(title)s.%(ext)s"),
                    "restrictfilenames": True,
                    "merge_output_format": "mp4",
                    "ffmpeg_location": ffmpeg_bin,
                    "progress_hooks": [progress_hook],
                    "http_headers": {"User-Agent": agent},
                    "retries": 10,
                }
            
            elif choice_a == "7":
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
                print("An Error Has occured, you can report this at https://github.com/R-D-R248/MediaZipX/issues")
                print(f"Download failed: {e}")
            except Exception as e:
                os.system("cls")
                print("An Error Has occured, you can report this at https://github.com/R-D-R248/MediaZipX/issues")
                print(f"An error occurred: {e}")


                
            print(input("Click Enter to Download more Videos"))
            

    else:
        time.sleep(0.5)
        os.system("cls")
        print(Fore.RED + Style.BRIGHT + "Invalid Choice")
        print(input("Press Enter to Return to Menu"))
        os.system("cls")
        continue
