"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():
    list = []
    with open("clusters_report.txt", "r") as text:
        list = text.readlines()

    tabla = []
    fila = [0, 0, 0.0, ""]

    #Elimina el nombre de las columnas
    for line in list[4:]:
        #Si la linea empieza con espacios seguidos de un numero
        if (re.match(r"^ +\d", line)):
            numero, cantidad, porcentaje, *palabras = line.split()#Elimina todos los espacios
            palabras.pop(0)#Elimina el %
            fila[0] = int(numero)
            fila[1] = int(cantidad)
            fila[2] = float(porcentaje.replace(",","."))
            fila[3] = " ".join(palabras)
            print(fila)

        #Si la linea empieza con espacios seguidos letras
        elif (re.match(r"^ +[a-z]", line)):
            palabras = line.split()
            fila[3] += " ".join(palabras)
            print(fila)

        #Si la linea solo tiene espaciado
        elif (re.match(r"^\s+$", line)):
            tabla.append(fila.copy())
            fila = [0, 0, 0.0, ""]

    df = pd.DataFrame (tabla, columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    return df

if __name__ == "__main__":
    print(ingest_data())