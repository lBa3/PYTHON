
# Crear un programa que solicite tres números al usuario y mediante condiciones `if-elif-else` los imprima de manera ordenada.



#a = input('Dame un primer numero: ')
#b = input('Dame un segundo numero')
#c = input('Dame un tercer numero')

#comparanumeros (a, b, c)


def funumeros (a, b, c):
    print ('Programa que solicite 3 numero ordena de mayor a menor')
    if( a > b and a > c):
       print ('a es mayor que b y c')
       if ( c > b):
            print ('c es mayor que b')
            print ('por lo tanto el orden queda del mayor a menor:' + str(a) + "' , '" + str(c) + "' , '" + str(b))
       else :
            print ('b es mayor que c')
            print ('por lo tanto el orden queda del mayor a menor:' + str(a) + "' , '" + str(b) + "' , '" + str(c))
    if( b > a and  b > c ):
        print ('b es mayor que a y c')
        if ( c > a):
            print ('c es mayor que a')
            print ('por lo tanto el orden queda del mayor a menor:' + str(b) + "' , '" + str(c) + "' , '" + str(a))
        else :
            print ('a es mayor que c')
            print ('por lo tanto el orden queda del mayor a menor:' + str(b) + "' , '" + str(a) + "' , '" + str(c))
    if(c > a and c > b ):
        print ('c es mayor que a y b')
        if ( a > b):
            print ('a es mayor que b')
            print ('por lo tanto el orden queda del mayor a menor:' + str(c) + "' , '" + str(a) + "' , '" + str(b))
        else :
            print ('b es mayor que a')
            print ('por lo tanto el orden queda del mayor a menor:' + str(c) + "' , '" + str(b) + "' , '" + str(a))

#a = input('Dame un primer numero: ')
#b = input('Dame un segundo numero')
#c = input('Dame un tercer numero')
#a = 30
#b = 10
#c = 20
#s = raw_input ("entrada: ")
#aux = s.split(" ")
#a, b, c = int(aux[0], int[1], int[2])
#funumeros (a, b, c)

###########################################################################################################################
#Crear un programa que solicite un texto, 
#luego recorra cada carácter del texto y
#lo guarde en un arreglo. 
#Finalmente mediante un ciclo `for-in` o un ciclo `while` 
#imprima el texto inverso, es decir, primero el último caráter y así sucesivamente hasta llegar al primero.

def recorre (stri):
    print ('Programa que solicite un string y recorrelo')
    ca = len(stri)
    print ('el string ingresado es:' + stri)
    print ('tiene #', ca)
    for aray in stri:
        print ('array:'+ aray)
    inversa (stri)           

def inversa (stri):
    print ('La inversa del string', stri[::-1])


stri = 'Hola_mundo'
#recorre(stri)    

###################################################################################################
#Crear un programa que defina la función `polar` la cual reciba un número `x` 
#y un número `y` 
#y devuelva una tupla `(r, t)` 
#donde `r = √ (x^2 + y^2)` y `t = atan2(y, x)`

def polar(x,y):
    r = 

x = 100
y = 200
#porlar (x, y)    

##################################################################################################################################
import turtle

class Triangle:

    def _init_(self, x0, y0, x1, y1, x2, y2):
        self.ax = x0
        self.ay = y0
        self.bx = x1
        self.by = y1
        self.cx = x2
        self.cy = y2
        self.color = "red"

        self.tur = turtle.Turtle()
        self.tur.ht()

    def contains(self, x, y):
        ax = self.cx - self.ax
        ay = self.cy - self.ay

        bx = self.bx - self.ax
        by = self.by - self.ay

        cx = x - self.ax
        cy = y - self.ay

        daa = ax * ax + ay * ay
        dab = ax * bx + ay * by
        dac = ax * cx + ay * cy

        dbb = bx * bx + by * by
        dbc = bx * cx + by * cy

        d = daa * dbb - dab * dab

        t = (dbb * dac - dab * dbc) / d
        s = (daa * dbc - dab * dac) / d

        #return t >= 0 and s >= 0 and (t + s) <= 1.0

    def draw():
        # self.tur.st()
        self.tur.ht()
        self.tur.color("blue")
        tur.up()
        self.tur.goto(self.ax, self.ay)
        self.tur.down()
        self.tur.goto(self.bx, self.by)
        self.tur.goto(self.cx, self.cy)
        self.tur.goto(self.ax, self.ay)
        self.tur.up()
        self.tur.ht()

tri = new Triangle(0, 0, 100, 50, 0, 100)

tri.draw()

def draw_dot(xo):
    color = "red"

    if tri.contains(xo, yo):
        color = "green"

    tur = turtle.Turtle()
    tur.up()
    tur.goto(xo, yo)
    tur.down()
    tur.dot(5, color)
    tur.ht()

turtle.getscreen().onclick(draw_dot)

turtle.mainloop()