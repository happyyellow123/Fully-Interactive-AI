import yt_dlp

def download_video(video_url):
    # 1. Define configuration options
    ydl_opts = {
        # Select the best available video quality and best audio, or fallback to general best
        'format': 'ext=mp4/best',
        
        # Merge video and audio into a standard MP4 container
        'merge_output_format': 'mp4',
        
        # Name the output file using the video title and extension
        'outtmpl': '%(title)s.%(ext)s',
        
        # Do not download the entire playlist if the link points to one
        'noplaylist': True,
        
        # Suppress excessive warning logs in the console
        'no_warnings': True,
    }

    try:
        # 2. Initialize YoutubeDL with options
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Extracting video metadata...")
            # extract_info fetches details. Setting download=False prevents downloading yet.
            info_dict = ydl.extract_info(video_url, download=False)
            
            video_title = info_dict.get('title', 'Unknown Title')
            print(f"Ready to download: '{video_title}'")
            
            # 3. Trigger the actual file download
            ydl.download([video_url])
            print("Download completed successfully!")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with any valid video link (YouTube, Vimeo, Twitch, etc.)
    target_url = "https://www.youtube.com/watch?app=desktop&v=pjmiWlImawg"
    download_video(target_url)
