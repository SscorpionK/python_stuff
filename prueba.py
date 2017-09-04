datos = "From stephen.maqrquard@uct.ac.za Sat Jan 7"
pos_arroba = datos.find('@')
print pos_arroba

pos_esp = datos.find(' ', pos_arroba)
print pos_esp

host = datos[pos_arroba+1:pos_esp]
print host
