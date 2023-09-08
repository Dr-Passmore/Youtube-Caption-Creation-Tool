import logging
from pytube import YouTube
import re
import time

class downloader:
    def __init__(self):
        pass
        

    def download (url):
        '''
        Downloads the MP3 of the provided url

        Input:
        - url: YouTube URL 
        
        Output:
        - filename: generated from video title
        '''
        
        #TODO Find a solution for age restricted content
        try:
            logging.info("Getting URL info")
            yt = YouTube(url)
            time.sleep(5)
            name = yt.title
            logging.info(f"{name} is being downloaded")
            filename = downloader.remove_special_characters(name)
            mp3file = f"{filename}.mp3"
            
            stream = yt.streams.filter(only_audio=True).order_by('bitrate') \
            .last()
            stream.download(filename=f"{filename}.mp3")
            logging.info(f"{name} - Successfully downloaded")
            return mp3file
        
        except Exception as e:
            error_message = str(e)
            if "age restricted" in error_message.lower():
                logging.error("The video is age-restricted and cannot be accessed without logging in.")
            else:
                logging.error(e)

    def remove_special_characters(filename):
        '''
        Removes special characters from the filename

        input: 
        - filename: String

        output:
        - filename: String with special characters removed 
        '''
        pattern = r'[\\/:?"*|<>&%#$!,]'
        
        cleaned_string = re.sub(pattern, '', filename)
        
        return cleaned_string

logging.basicConfig(filename='CaptionGeneration.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    downloader()
    
downloader.download("https://youtu.be/fRRHDXHSsM0?si=n4nUNUyAVah88UZs")