#pip install pytube
import pytube

url =   'https://www.youtube.com/watch?v=hHEDr2V_1iA'
        #'https://www.youtube.com/watch?v=2xkSkgOw6I8'
        #'https://www.youtube.com/watch?v=hHEDr2V_1iA'

youtube = pytube.YouTube(url)

#"Tenta" baixar o vídeo com a resolução máxima
video = youtube.streams.get_highest_resolution()

video.download('C:\\Users\\fabio\\Downloads')