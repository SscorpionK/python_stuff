camellos = 43

print "He divisado %d camellos" % camellos

print "En %d anyos solo he visto %g %s" % (10, 0.7, "camellos")

cad = 'X-DSPAM-confidence:  0.8475'

dot_pos = cad.find('.') #dot pos : 22

float_num = cad[dot_pos-1:]

print float(float_num)



