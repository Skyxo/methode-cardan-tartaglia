from math import *
from sympy import *
from numpy import *
from fractions import Fraction
from matplotlib.pyplot import *

#fonction renvoyant les racines d'un polynôme de second degré
def racines_2nd_degre(a, b, c):
    delta = (b**2)-4*a*c
    
    if delta > 0:
        return (-b-sqrt(delta))/(2*a), (-b+sqrt(delta))/(2*a)
        
    elif delta == 0:
        return (-b)/(2*a), (-b)/(2*a)
        
    elif delta < 0:
        return complex(((-b)+1j*sqrt(-delta))/2), complex(((-b)-1j*sqrt(-delta))/2)

#initialisation des coefficients
print("Rentrer les coefficients du polynôme du 3ème degré (a,b,c,d) : ")
ini_a = float(Fraction(input("a = ")))
ini_b = float(Fraction(input("b = ")))
ini_c = float(Fraction(input("c = ")))
ini_d = float(Fraction(input("d = ")))

#définition de l'expression
x = Symbol('x')
expression = expand(simplify(ini_a*x**3 + ini_b*x**2 + ini_c*x + ini_d))

#création de la fonction pour le calcul graphique
def f(x):
    return ini_a*x**3 + ini_b*x**2 + ini_c*x + ini_d

#réarangement de l'équation
a, b, c, d = 1, ini_b/ini_a, ini_c/ini_a, ini_d/ini_a

alpha = -b/3

#on définit p et q avec le terme général
p = 3*alpha**2 + 2*b*alpha + c
q = alpha**3 + b*alpha**2 + c*alpha + d

#on cherche U et V dans notre système en résolvant une équation du second degré
b_sys = q
c_sys = (-p**3)/27
U, V = racines_2nd_degre(1, b_sys, c_sys)

#on s'assure que la racine cubique s'applique à un nombre positif (sinon python le converti en nombre complexe)
if type(U) == complex or U > 0:
    u = U**(1/3)
else:
    u = -abs(U)**(1/3)
    
if type(V) == complex or V > 0:
    v = V**(1/3)
else:
    v = -abs(V)**(1/3)

#on en déduit X, puis x1
X = u + v
x1 = X + alpha
x1 = x1.real

#identification des coefficients a', b', c' après factorisation du polynôme de degré 3 par x1 pour trouver les deux autres racines : (x-x1)(a'x**2 + b'x + c')
aprime = a
bprime = aprime*x1 + b
cprime = c + bprime*x1

#résolution de l'équation du second degré après identification des coefficients (a'x**2 + b'x + c')
x2, x3 = racines_2nd_degre(aprime, bprime, cprime)

#conclusion
print("D'après la méthode de Cardan-Tartaglia, le polynôme de degré 3, f(x)= ", expression, "possède ", end = "")

#plaçage des repères et de la racine réelle sur le graphique
axhline(y=0,color='black')
axvline(x=0,color='black')
plot(x1, 0, marker="o", color="red")
annotate('x1', xy = (x1, 0))

#traitement des différents cas de figure
if type(x2) == complex or type(x3) == complex:
    print("une racine réelle et deux racines complexes conjuguées:")
    print("\nx1 =",x1,"\nz1 =", x2,"\nz2 =", x3, "\n")
elif x2 == x3:
    print("deux racines réelles dont une double :")
    print("\nx1 =",x1,"\nx2 =", x2,"\nx3 = x2\n")
    plot(x2, 0, marker="o", color="red")
    annotate('x2 & x3', xy = (x2, 0))
else:
    print("trois racines réelles distinctes :")
    print("\nx1 =",x1,"\nx2 =", x2,"\nx3 =", x3, "\n")
    plot(x2, 0, marker="o", color="red")
    plot(x3, 0, marker="o", color="red")
    annotate('x2', xy = (x2, 0))
    annotate('x3', xy = (x3, 0))

#affichage de la courbe de fonction
x = arange(-10, 10, 0.01)
plot(x, f(x), label = "f(x)")
grid()
legend()
show()