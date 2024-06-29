from pytube import YouTube


SAVE_PATH = "C:/Users/ACER/Video"
RESOLUTION = '720p'
URL = 'https://youtu.be/GBnif5tUJl4?si=ozhNRNobe4xqrQyr'

try:
    video = YouTube(URL)
    video_streams_mp4 = video.streams.filter(file_extension='mp4')

    try:
        video_streams_mp4.get_by_resolution(resolution=RESOLUTION).download(output_path=SAVE_PATH)
        print("Video Downloaded!")
    except:
        print(f"Resolusi {RESOLUTION} tidak tersedia.")
        print(f"Resolusi tertinggi yang tersedia: {video_streams_mp4.get_highest_resolution().resolution}")
        confirm = input("Download?[y/n] ")

        if confirm.lower() == 'y':
            print("Downloading...")
            try:
                video_streams_mp4.get_highest_resolution().download(output_path=SAVE_PATH)
                print("Video Downloaded!")
            except:
                print("Terjadi Error saat menyimpan video.")
except:
    print('Connection Error!')
