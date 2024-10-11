pila=[]
max_size=8
tope=0

def dibujar_pila():
    print("Estado actual de la pila")
    for i in range(max_size-1,-1,-1):
        if i >= tope:
         print(f"|       |")
        else:
           print(f"|   {pila[i]}   |")
        
    print(f"---------")
    print(f"Tope={tope}\n")


def insertar(elemento):
   global tope
   if tope < max_size:
      pila.append(elemento)
      tope += 1
      print(f"Insertar elemento({elemento})")
      dibujar_pila()
   else:
      print(f"Error: la pila esta llena. Nose puede isertar {elemento}")
      

def eliminar():
   global tope 
   if tope > 0:
      elemento=pila.pop()
      tope -= 1
      print(f"Eliminar {elemento}")
      dibujar_pila()
   else:
     print(f"Error: pila vacia. No hay elemento que eliminar")
     dibujar_pila() 

insertar("x")
insertar("y")
eliminar()
eliminar()
eliminar()
insertar("v")
insertar("w")
eliminar()
insertar("r")
