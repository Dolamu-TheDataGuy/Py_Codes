from pytube import Playlist # Importing dependencies
""" Program that automates Youtube playlist download based on a provided link"""


def download_playlist(prov_link):
    """Function that download all the video
     from a provided YouTube playlist"""
    playlist = Playlist(prov_link)
    print(playlist)  # puts the link of each video in the playlist in the
    for video in playlist.videos:
        print("Downloading " + video.title)
        mp4_vid = video.streams.filter(file_extension="mp4").filter(res="1080p")
        mp4_vid.first().download()


link = "https://www.youtube.com/playlist?list=PLeo1K3hjS3uuASpe-1LjfG5f14Bnozjwy"
download_playlist(link)
