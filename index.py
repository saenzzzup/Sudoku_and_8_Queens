# Protyecto 3; Creado por Saenz Barragan Ricardo

#Para agregar los argumentos de que programa se correra
import argparse
#Impementacion Grafica de Sudoku
from GUI_sudoku import Window_sudoku
#Impementacion Grafica de n-Reinas
from GUI_nQueens import Window_queens

#Usamos parametros antes de la ejecucion para saber que problema vamos a correr, y estos los hacemos obligatorios
ap = argparse.ArgumentParser(description="Tipo de solucionario que busca: sudoku o NReinas")
ap.add_argument("-t", required=True, help="sudoku o NReinas")

#Guardamos el elemento que se recive en la ejecución
args = vars(ap.parse_args())
type_= str(args["t"])

#elejimos el problema si se ingreso correctamente, de lo contraio el programa no corre
def main(type_Problem):
	if type_Problem == "sudoku" :
		Window_sudoku()
	elif type_Problem == "NReinas" :
		Window_queens()
	else :
		print("No es una opción valida, intente con: sudoku o NReinas")

main(type_)
