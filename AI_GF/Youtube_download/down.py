import yt_dlp

def download_video(video_url):
    ydl_opts = {
        'format': 'ext=mp4/best',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'no_warnings': True,

        # FIX FOR AGE RESTRICTION: Triggers a secure TV login prompt in your terminal
        'username': 'oauth2',
        'password': '',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Extracting video metadata...")
            info_dict = ydl.extract_info(video_url, download=False)
            
            video_title = info_dict.get('title', 'Unknown Title')
            print(f"Ready to download: '{video_title}'")
            
            ydl.download([video_url])
            print("Download completed successfully!")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_url = "https://www.youtube.com/watch?app=desktop&v=pjmiWlImawg"
    download_video(target_url)
