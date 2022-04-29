class Ventana:
    __titulo=''
    __valors_x=0
    __valors_y=0
    __valori_x=500
    __valori_y=500
    
    def __init__(self, titulo,valorsx=100,valorsy=100,valorix=100,valoriy=100):
        self.__titulo=titulo
        self.__valors_x=int(valorsx)
        self.__valors_y=int(valorsy)
        self.__valori_x=int(valorix)
        self.__valori_y=int(valoriy)
        
    def mostrar(self):
        print ('\n El titulo es:', format (self.__titulo))
        print ('\n El valor de x en el vertice superior izquierdo:', format (self.__valors_x))
        print ('\n El valor de y en el vertice superior izquierdo:', format (self.__valors_y))
        print ('\n El valor de x en el vertice inferior derecho:', format (self.__valori_x))
        print ('\n El valor de y en el vertice inferior derecho:', format (self.__valori_y))
        
    def getTitulo(self):
        return self.__titulo
    
    def alto(self):
        return (self.__valors_y-self.__valori_y)
    
    def ancho(self):
        return (self.__valors_x-self.__valori_x)
    
    def moverDerecha(self, desplazamiento):
        if desplazamiento+self.__valori_x <=500 and desplazamiento+self.__valors_x<self.__valori_x:
            self.__valori_x+=desplazamiento
            self.__valors_x+=desplazamiento
        else: print('no se cumplio la condicion')
        
    def moverIzquierda(self, desplazamiento):
        if self.__valors_y-desplazamiento>=0 and self.__valori_y-desplazamiento>self.__valors_y:
            self.__valori_y-=desplazamiento
            self.__valorx_y-=desplazamiento
        else: print('no se cumple la condicion')
    
    def bajar(self, desplazamiento):
        if desplazamiento+self.__valori_x<=500 and desplazamiento+self.__valors_x<self.__valori_x:
            self.__valors_x+=desplazamiento
            self.__valori_x+=desplazamiento
    
    def subir(self, desplazamiento):
        if self.__valors_y-desplazamiento>=0 and self.__valori_y-desplazamiento>self.__valors_y:
            self.__valori_y-=desplazamiento
            self.__valorx_y-=desplazamiento
        