import pytube

url = 'https://www.youtube.com/watch?v=MowJTU3Lf88'
youtube = pytube.YouTube(url)
video = youtube.streams.get_by_itag(135)
video.download('C://Users//User//Desktop//youtube//code')
print('Done')
