import urllib

manf = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for linea in manf:
    print linea.strip()
