import pytube  # importing youtube class from pytube
import validators 
from urllib.parse import urlparse

def download(video):
    streams = set()								
    print("Your video title is: "+ video.title)

    for stream in video.streams.filter(type="video"):  # Only look for video streams to avoid None values
        streams.add(stream.resolution)

    print(streams)
    x = False
    y = False
    while x is False:
        video_quality = str(input("Enter quality: "))
        if video_quality in streams:
            x = True
           
        else:
            x = False
            print("\ntry again\n")
    streams.clear()


    for stream in video.streams.filter(resolution=video_quality):
        print(stream)
        streams.add(stream.itag)
        print(streams)


    while y is False:
         itag_input =  int(input("Give the desired itag from above : "))
         if itag_input in streams:
            y = True
         else:
            y = False
            print("\ntry again\n")  


    stream = video.streams.get_by_itag(int(itag_input))
    print("starting download ")
    stream.download("C:\\Users\\kalid\\Downloads")    
        

def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False


# print(uri_validator(url))

try:
    url = str(input("Enter ur url: "))
    video = pytube.YouTube(url)             # url = 'https://www.youtube.com/watch?v=rUWxSEwctFU'
			                                # if we just used import pytube then we should have used video  = pytube.YouTube(url)
except    pytube.exceptions.PytubeError:
    print("\n-------------link error-------------\n")
else:
    
    download(video)
finally:
    print("\n---------------finish---------------")
    

    

 
