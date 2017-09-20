import time
import webbrowser

def sleeping():
    time.sleep(10)

def openBrowser():
   url="https://www.youtube.com/watch?v=ZgewiFcvChw"
   webbrowser.open_new(url)
   print "The url test has been successful"

sleeping()
openBrowser()
