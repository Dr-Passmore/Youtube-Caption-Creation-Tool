import tkinter as tk
import tkinter.simpledialog
import configparser
import logging
import os
import pvleopard
import requests
import webbrowser

import mp3download
import createSRTFile

class captionCreation():
    def __init__(self):
        configFile = os.path.exists('config.ini')
        if configFile == False:
            #if the file does not exist then create one
            logging.error("No config file found")
            captionCreation.apiInterface(self)
            
        else:
            pass
        
        #mp3download.downloader.download("https://youtu.be/fRRHDXHSsM0?si=n4nUNUyAVah88UZs")
        userInterface()

    def configCreation(self, config):
        """
        Creates a configuration file 'config.ini' if it doesn't exist.

        Input:
        - config: ConfigParser instance for handling configuration.

        Output:
        - None (Creates or updates the 'config.ini' file.)
        """
        logging.info("Creating 'config.ini' file")
        try:
            apiKey = input("Please enter your API key:\n")
            config.add_section('API Key')
            config.set('API Key', 'Key', apiKey)
            with open(r"config.ini", 'w') as configuration:
                config.write(configuration)
            logging.info('config.ini created successfully')
        except Exception as e:
            logging.error(f"Failed to create config.ini: {e}")

    def apiInterface(self):
        '''
        Function to create the API key setup interface.
        This interface allows the user to enter their API key and save it to a configuration file.
        '''
        self.window = tk.Tk()
        self.window.title("API Key Setup")
        self.window.geometry("300x200") 

        label_instructions = tk.Label(self.window, text="You can acquire your API key from:")
        label_instructions.pack(pady=5)

        # Create a clickable hyperlink
        link_label = tk.Label(self.window, text="https://console.picovoice.ai/", cursor="hand2")
        link_label.pack(pady=5)
        link_label.bind("<Button-1>", self.openLink)

        label = tk.Label(self.window, text="Enter your API key:")
        label.pack(pady=10)

        self.api_key_entry = tk.Entry(self.window)
        self.api_key_entry.pack()

        save_button = tk.Button(self.window, text="Save", command=self.saveAPIKey)
        save_button.pack(pady=10)

    def saveAPIKey(self):
        '''
        Saves the API key and destroys the window once completed
        '''
        api_key = self.api_key_entry.get()
        if api_key:
            config = configparser.ConfigParser()
            config.add_section('API Key')
            config.set('API Key', 'Key', api_key)
            with open(r"config.ini", 'w') as configuration:
                config.write(configuration)
            logging.info('API key saved successfully.')
        else:
            logging.error('API key cannot be empty.')

        self.window.destroy()

    def openLink(self):
        '''
        Opens the picovoice.ai link
        '''
        webbrowser.open("https://console.picovoice.ai/")
            

class userInterface ():
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Subtitle Generator")
        self.window.geometry("500x500") 
        self.window.protocol("WM_DELETE_WINDOW", self.exitProgram)

        exit_button = tk.Button(self.window, text="Exit", command=self.exitProgram)
        exit_button.pack(pady=10)

        userInterface.generateWindow(self)
    
    def generateWindow(self):
        self.window.mainloop()

    def exitProgram(self):
        result = tkinter.simpledialog.messagebox.askquestion("Confirm Close", "Are you sure you want to close the application?")
        if result == "yes":
            self.window.destroy()

logging.basicConfig(filename='CaptionGeneration.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

        
    
    
    
if __name__ == "__main__":
    captionCreation()