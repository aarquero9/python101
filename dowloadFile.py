import urllib.request
data = urllib.request.urlopen("https://raw.githubusercontent.com/itsfoss/text-files/master/sherlock.txt")

for line in data:
    print(line)