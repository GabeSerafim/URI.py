entrada=raw_input().split()
entrada.sort()
a,b,c=float(entrada[2]),float(entrada[1]),float(entrada[0])
if a>= b+c:
    print "NAO FORMA TRIANGULO"
else:
    if a**2 == (b**2)+(c**2):
        print "TRIANGULO RETANGULO"
    if a**2> (b**2)+(c**2):
        print "TRIANGULO OBTUSANGULO"
    if a**2< (b**2)+(c**2):
        print "TRIANGULO ACUTANGULO"
    if a==b and b==c:
        print "TRIANGULO EQUILATERO"
    if (a==b and b!=c) or (b==c and a!=b) or (a==c and b!=a):
        print "TRIANGULO ISOSCELES"
