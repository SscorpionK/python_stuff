manf = open('mbox-short.txt')

for linea in manf:
   linea = linea.rstrip()
   if not linea.startswith('From '): continue
   palabras = linea.split()
   print palabras[2]

