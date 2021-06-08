from pytube import YouTube   # importing youtube class from pytube

# url = str(input("Enter ur url: "))
url = 'https://www.youtube.com/watch?v=rUWxSEwctFU'
video = YouTube(url)			# if we just used import pytube then we should have used video  = pytube.YouTube(url)
streams = set()								
print("Your video title is: "+ video.title)

for stream in video.streams.filter(type="video"):  # Only look for video streams to avoid None values
    streams.add(stream.resolution)

print(streams)
video_quality = str(input("Enter qyuality: "))

for stream in video.streams.filter(resolution=video_quality):
    print(stream)
 
itag_input =  input("Give the desired itag from above : ")
stream = video.streams.get_by_itag(int(itag_input))
print("starting download ")
stream.download("C:\\Users\\kalid\\Downloads")
print("finish")

 
