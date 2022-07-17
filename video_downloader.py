import pytube
link = str(input('Enter the video link -'))
try:
    video = pytube.YouTube(link)
    video = video.streams.get_highest_resolution()
    video.download()
    print('Video Downloaded In Current Directory !!!!')
except:
    print('Something Went Wrong ...')
