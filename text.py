import urllib

uf = urllib.request.urlopen('https://stackoverflow.com/questions/33566843/how-to-extract-text-from-html-page')
html = uf.read()