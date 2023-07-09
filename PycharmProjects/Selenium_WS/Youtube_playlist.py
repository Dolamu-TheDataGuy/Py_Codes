import pytube
from pytube import Playlist # Importing dependencies
import moviepy.editor as mpe
""" Program that automates Youtube playlist download based on a provided link"""


def download_playlist(prov_link):
    """Function that download all the video
     from a provided YouTube playlist"""
    vname = "clip.mp4"
    aname = "audio.mp3"
    playlist = Playlist(prov_link)
    print(playlist)  # puts the link of each video in the playlist in the
    for video in playlist.videos:
        print("Downloading " + video.title)
        mp4_vid = video.streams.filter(file_extension="mp4").filter(res="1080p")
        mp4_vid.first().download()
        mp3_aud = pytube.YouTube(prov_link).streams.filter(only_audio=True).first().download()

        mp4_vid = mpe.VideoFileClip(vname)
        mp3_aud = mpe.AudioFileClip(aname)
        final_video = mp4_vid.set_audio(mp3_aud)

        final_video.write_videofile("")


link = "https://www.youtube.com/playlist?list=PLhW3qG5bs-L81R4w0jyLo95JdFHtaxRp4"
download_playlist(link)
