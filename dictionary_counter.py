palabra = 'brontosaurio'

d = {}
for c in palabra:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
print d

a = dict()
for c in palabra:
    a[c] = a.get(c,0) + 1
print a

manf =''

while manf == '':
    nombref = raw_input('Introduzca el nombre del fichero:')
    try:
        manf = open(nombref)
    except:
        if nombref == 'fin!': exit()
        else:
            print 'El fichero %s no esta en el mismo directorio que el script, para salir escriba fin!\n' % nombref
            continue

    contadores = dict()

    for linea in manf:
        palabras = linea.split()
        for pal in palabras:
            if pal not in contadores:
                contadores[pal] = 1
            else:
                contadores[pal] += 1

    print contadores
    print linea

lst = contadores.keys()
print lst
lst.sort()

for clave in lst:
    print clave, contadores[clave]
