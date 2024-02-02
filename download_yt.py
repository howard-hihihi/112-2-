from pytube import YouTube

# YouTube 影片的 URL
video_url = "https://www.youtube.com/watch?v=210R0ozmLwg"

# 下載影片
yt = YouTube(video_url)
video_stream = yt.streams.get_highest_resolution() # 下載為最高畫質影片
video_stream.download(output_path="video")
