import yt_dlp
def progesive_hook(d):
    index = d["fragment_index"]
    total = d["fragment_count"]
    percent = index/total
    print(percent)
    print()
def download_youtube_video(url):
    ydl_opts = {
        'format': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=mp4]',
        'outtmpl': '%(title)s.%(ext)s',     
        'progress_hooks':[progesive_hook]
        
    }

    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        ydl.add
    return True   


download_youtube_video("https://www.youtube.com/watch?v=_gnE88gOleE")