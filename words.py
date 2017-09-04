nombre = raw_input('Introduzca fichero: ')
manejador = open(nombre, 'r')
texto = manejador.read()
palabras = texto.split()
contadores = dict()

for palabra in palabras:
   contadores[palabra] = contadores.get(palabra,0) + 1

mayor_cantidad = None
mayor_palabra = None

for palabra, contador in contadores.items():
   if mayor_cantidad is None or contador > mayor_cantidad:
      mayor_palabra = palabra
      mayor_cantidad = contador

print mayor_palabra, mayor_cantidad
