#!/usr/bin/python
import time
import webbrowser

def sleeping():
    time.sleep(2.5)

def openBrowser():
   b = webbrowser.get('chrome')
   b.open("http://www.google.com.mx/")

sleeping()
openBrowser()

