import tkinter as ttk
import configparser
import logging
import os
import pvleopard
import requests

import mp3download

class captionCreation():
    def __init__(self):
        config = configparser.ConfigParser()
        configFile = os.path.exists('config.ini')
        if configFile == False:
            #if the file does not exist then create one
            logging.error("No config file found")
            captionCreation.configCreation(self, config)
        else:
            pass
    
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
            
        
logging.basicConfig(filename='CaptionGeneration.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

        
    
    
    
if __name__ == "__main__":
    captionCreation()