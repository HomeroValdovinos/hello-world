#!/usr/bin/python
import time
import webbrowser

def sleeping():
    time.sleep(2.5)

def openBrowser():
   url="http://iwmstoday.webfarm.ms.com/mstoday/"
   webbrowser.open_new(url)

sleeping()
openBrowser()
