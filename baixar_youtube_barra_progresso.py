#pip install pytube
import pytube

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)


def main():
    #chunk_size = 1024
    url = "https://www.youtube.com/watch?v=hHEDr2V_1iA"
    yt = pytube.YouTube(url)
    video = yt.streams.get_highest_resolution()
    yt.register_on_progress_callback(on_progress)
    print(f"Fetching \"{video.title}\"..")
    print(f"Fetching successful\n")
    print(f"Information: \n"
          f"File size: {round(video.filesize * 0.000001, 2)} MegaBytes\n"
          f"Highest Resolution: {video.resolution}\n"
          f"Author: {yt.author}")
    print("Views: {:,}\n".format(yt.views))

    print(f"Downloading \"{video.title}\"..")
    video.download('C:\\Users\\fabio\\Downloads')

main()