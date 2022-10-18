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

    #Elimina el nombre de las columnas
    for line in list[4:]:
        #Si la linea empieza con espacio seguido de un numero
        if (re.match(r"^ +\d", line)):
            pass

        elif (re.match(r"^ +[a-z]", line)):
            print(line)

if __name__ == "__main__":
    ingest_data()