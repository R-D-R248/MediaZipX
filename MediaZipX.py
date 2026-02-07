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

try:
    app_folder = os.path.join(os.getenv("APPDATA"), "MediaZipX")
    data_file = os.path.join(app_folder, "browser.txt")
    with open(data_file, "r") as f:
        browser = f.read().strip()
except:
    browser = "edge"

while True:
    os.system("cls")
    logof()
    print(Fore.BLUE + "MediaZipX 1.3")
    print("by Code" + Fore.RED + "R" + Fore.WHITE + "-" + Fore.BLUE + "D" + Fore.WHITE + "-" + Fore.RED + "R")
    print("https://github.com/R-D-R248")
    print(Fore.WHITE + Style.DIM + "-"*96)
    print(Fore.RED + "DISCLAIMER!")
    print(Fore.WHITE + "The creator (Code" + Fore.RED + "R" + Fore.WHITE + "-" + Fore.BLUE + "D" + Fore.WHITE + "-" + Fore.RED + "R"+ Fore.WHITE +") is not responsible for")
    print(Fore.WHITE + "Misuse of MediaZipX in " + Fore.RED + "violation" + Fore.WHITE + " of YouTube’s or other platforms’ Terms of Service.")
    print(Fore.WHITE + Style.DIM + "-"*96)
    print(Fore.BLUE + Style.BRIGHT + "[1]Download from YouTube")
    print(Fore.BLUE + Style.BRIGHT + "[2]About")
    print(Fore.RED + "[3]Options")
    print(Fore.RED + "[4]Exit")
    choice = input("Choose(1-3): ")
    if choice == "4":
        sys.exit()
    elif choice == "3":
        os.system("cls")
        print(Style.BRIGHT + "Options")
        print("[1]Choose Browser(for Anti-Bot Error Prevention)")
        print("[2]Exit to Main Menu")
        choice_a = input("Choose(1-7): ")
        while True:
            if choice_a == "1":
                while True:
                    print(Style.BRIGHT + "Browsers")
                    print("Please Select the Browser You use.")
                    print(Fore.BLUE + Style.BRIGHT + "[1]Chrome")
                    print(Fore.BLUE + Style.BRIGHT + "[2]Edge")
                    print(Fore.BLUE + Style.BRIGHT + "[3]Opera")
                    print(Fore.BLUE + Style.BRIGHT + "[4]Firefox")
                    print(Fore.BLUE + Style.BRIGHT + "[5]Brave")
                    print(Fore.BLUE + Style.BRIGHT + "[6]Chromium")
                    print(Fore.BLUE + Style.BRIGHT + "[7]Vivaldi")
                    print(Fore.RED + "[8]Exit Browser Select")
                    choice_a = input("Choose(1-8): ")
                    browser = choice_a
                    app_folder = os.path.join(os.getenv("APPDATA"), "MediaZipX")
                    os.makedirs(app_folder, exist_ok=True)
                    data_file = os.path.join(app_folder, "browser.txt")
                    if browser == "6":
                        text_to_save = "chromium"
                    elif browser == "1":
                        text_to_save = "chrome"
                    elif browser == "2":
                        text_to_save = "edge"
                    elif browser == "3":
                        text_to_save = "opera"
                    elif browser == "4":
                        text_to_save = "firefox"
                    elif browser == "5":
                        text_to_save = "brave"
                    elif browser == "7":
                        text_to_save = "vivaldi"
                    elif browser == "8":
                        break
                    else:
                        os.system("cls")
                        print(Fore.RED + Style.BRIGHT + "Invalid Choice")
                        print(input("Press Enter to Return to Options"))
                        os.system("cls")
                        continue
                    with open(data_file, "w", encoding="utf-8") as f:
                        f.write(text_to_save)
                    print("Your Browser Option has been Saved.\nClick Enter to Return to Options")
                    print(input())
                    os.system("cls")
                    break
                
            elif choice_a == "2":
                break
            
            else:
                os.system("cls")
                print(Fore.RED + Style.BRIGHT + "Invalid Choice")
                print(input("Press Enter to Return to Options"))
                os.system("cls")
                continue
    elif choice == "2":
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
            choice_a = input("Choose(1-7): ")
            if choice_a == "6":
                url = input("Enter the URL: ")
                ydl_opts = {
                    "format": "bestvideo[ext=mp4]/bestvideo",
                    "outtmpl": "%(title)s.%(ext)s",
                    "restrictfilenames": True,
                    "progress_hooks": [lambda d: print(f"Progress: {d['_percent_str']}") if d['status']=='downloading' else None],
                    "cookiesfrombrowser": (browser,),
                    "retries": 10,
                }
    
            elif choice_a == "2":
                url = input("Enter the URL: ")
                ydl_opts = {
                    "format": "bestaudio[ext=m4a]",
                    "outtmpl": "%(title)s.%(ext)s",
                    "restrictfilenames": True,
                    "progress_hooks": [lambda d: print(f"Progress: {d['_percent_str']}") if d['status']=='downloading' else None],
                    "cookiesfrombrowser": (browser,),
                    "retries": 10,
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }],
                    "ffmpeg_location": ffmpeg_bin,

                }
            elif choice_a == "3":
                url = input("Enter the URL: ")
                ydl_opts = {
                    "format": "bestaudio[ext=m4a]",
                    "outtmpl": "%(title)s.%(ext)s",
                    "restrictfilenames": True,
                    "progress_hooks": [lambda d: print(f"Progress: {d['_percent_str']}") if d['status']=='downloading' else None],
                    "cookiesfrombrowser": (browser,),
                    "retries": 10,
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "wav",
                        "preferredquality": "192",
                    }],
                    "ffmpeg_location": ffmpeg_bin,

                }
            elif choice_a == "4":
                url = input("Enter the URL: ")
                ydl_opts = {
                    "format": "bestaudio[ext=m4a]",
                    "outtmpl": "%(title)s.%(ext)s",
                    "restrictfilenames": True,
                    "progress_hooks": [lambda d: print(f"Progress: {d['_percent_str']}") if d['status']=='downloading' else None],
                    "cookiesfrombrowser": (browser,),
                    "retries": 10,
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "flac",
                        "preferredquality": "300",
                    }],
                    "ffmpeg_location": ffmpeg_bin,

                }
            elif choice_a == "1":
                url = input("Enter the URL:")
                ydl_opts = {
                    "format": "bestvideo[height<=2160]+bestaudio[ext=m4a]/best",
                    "outtmpl": "%(title)s.%(ext)s",
                    "restrictfilenames": True,
                    "merge_output_format": "mp4",
                    "ffmpeg_location": ffmpeg_bin,
                    "progress_hooks": [lambda d: print(f"Progress: {d['_percent_str']}") if d['status']=='downloading' else None],
                    "cookiesfrombrowser": (browser,),
                    "retries": 10,
                }
            elif choice_a == "5":
                url = input("Enter the URL:")
                ydl_opts = {
                    "format": "bestvideo[height<=720]+bestaudio[ext=m4a]/best[ext=mp4][height<=720]",
                    "outtmpl": "%(title)s.%(ext)s",
                    "restrictfilenames": True,
                    "merge_output_format": "mp4",
                    "ffmpeg_location": ffmpeg_bin,
                    "progress_hooks": [lambda d: print(f"Progress: {d['_percent_str']}") if d['status']=='downloading' else None],
                    "cookiesfrombrowser": (browser,),
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
