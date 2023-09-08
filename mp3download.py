import logging
from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class downloader:
    def __init__(self):
        pass
        

    def download (url):
        
        try:
            yt = YouTube(
                    url,
            )
            stream = yt.streams.filter(only_audio=True).order_by('bitrate') \
            .last()
            stream.download(filename=f"test3.mp3")
        except Exception as e:
            error_message = str(e)
            if "age restricted" in error_message.lower():
                print("The video is age-restricted and cannot be accessed without logging in.")
                '''
                 # Set up a Selenium WebDriver
                driver = webdriver.Chrome()  # You can use other browsers by specifying the driver.

                # Log in to YouTube
                driver.get("https://www.youtube.com")
                time.sleep(5)
                driver.find_element_by_name("identifier").send_keys(username)
                driver.find_element_by_id("identifierNext").click()
                driver.implicitly_wait(5)
                driver.find_element_by_name("password").send_keys(password)
                driver.find_element_by_id("passwordNext").click()
                driver.implicitly_wait(5)

                # Access the age-restricted content
                driver.get(url)

                # Download the video using PyTube
                yt = YouTube(url)
                stream = yt.streams.filter(only_audio=True).first()
                stream.download(filename="test2.mp3")
                logging.info(f"Downloaded: {url}")

                # Close the browser
                driver.quit()
            else:
                print(f"Error: {e}")
            '''
logging.basicConfig(filename='CaptionGeneration.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    downloader()
    
downloader.download("https://www.youtube.com/watch?v=17Kszzcmfv4")