import scrapy
import time
import parameter
import drivers
import instaloader
def login():
   
        Object = instaloader.Instaloader()
        Object.login(parameter.Instagram_username, parameter.Instagram_password)
        print("Logged in Instagram")
        return Object
       
