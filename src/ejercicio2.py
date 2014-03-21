import mod
n=10
l=3.1415926535897931159979634685441852
#v=(10,100,1000)	  #el numero maximo de elementos es 9 para los que produce error de memoria
v=(1e1,1e2,1e3)  esta es en notacion cientifica
p=[]	#.pyc es el enlace entre el fichero que importo y el que llamo
for i in v:
 y=mod.pi(n)
 p=p+[y]
 print y
print 'la t-upla es %s'  % p
def fun(n):
 print ' valor de la funcion:              numero de veces que se la llama'
 for i in v:
  y=mod.pi(n)
  print '%i     %.10f               %.10f                   %.10f       %i'   % (i,l,y,s-l,v[i])
print fun(n)
#el tiempo de ejecucion lo hallo restando el tiempo entre el ultimo print y el n=0 y lo imprimo por pantalla