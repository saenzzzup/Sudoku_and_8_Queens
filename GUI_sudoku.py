#Creado por Saenz Barragan Ricardo

#Interfaz Grafica
from tkinter import *
from tkinter import messagebox
#Solucion recursiva del problema
from class_problem import sudoku
import os

#Funcion que recibe el nombre de un archivo para abrir, si el archivo no 
#existe regresa un None, de lo contratio abre el archivo y lo guarda en una lista
def Open_Sudoku(file_name, size):
	if not os.path.isfile(file_name):
		return None

	puzzle_file = open(file_name, "r")
	puzzle_list = puzzle_file.read().splitlines()
	puzzle_file.close()

	puzzle = []
	#Separa cada elemento de la lista en sub listas que luego va añadiendo 
	#Esto para que quede en la forma adecuada para ser solucionado
	for i in range(size):
		puzzle.append([])
		for number in puzzle_list[i]:
			puzzle[i].append(int(number))
	#Regresa una lista de listas con los elemnetos ordenados
	return puzzle

#Clase que se encarga de crear la ventana y lo que contiene 
# Ya sea las funciones que se realizan dentro de ella y los graficos que aparecen
class sudoku_Frame(Frame):
	#inicialisa creando por predeterminado un tamaño 9 que se puede ajustar para que sea
	#de tamaño n, pero por propositos de grafico solo sera de 9 x 9
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.grid()
		self.size = 9
		self.sizePuzzle = self.size * self.size
		self.puzzle = None
		self.create_window()

	#Crea la ventana que se estara actualizando, un diccionario que guarda las casillas para 
	#escribir y el tamaño del tablero
	def create_window(self):
		self.entries = {}
		self.tableheight = self.size
		self.tablewidth = self.size
		#Botones que se encargan de empezar las funciones

		#Resuleve lo escrito en el tablero
		self.pack(fill=BOTH, expand= 1)
		solve = Button(self, text= 'Solve', width = 6, height = 2, command=self.SolvePuzzle)
		solve.place(x=45, y=300)
		#Abre un archivo para solucionar
		read = Button(self, text= 'Open', width = 6, height = 2, command=self.open_sudo)
		read.place(x=100, y=300)
		#Limpia la pantalla y lo que se haya guardado
		restart = Button(self, text= 'Restart', width = 6, height = 2, command=self.clear_text)
		restart.place(x=155, y=300)
		#Termina el programa
		exit = Button(self, text= 'Exit', width = 6, height = 2, command=self.exitProgram)
		exit.place(x=210, y=300)

		#Crea el tablero de 9 x 9 usando cajones para escribir
		#contador que sera la llave de  diccionario para los cajones
		counter = 0
		for row in range(self.tableheight):
			for column in range(self.tablewidth):
				#Nos dicen el sector donde se encuentra para saber que color llevaran
				sectorRow = 3 * (row//3)
				sectorCol = 3 * (column//3)
				#Si se encuentran en los sectores, 2, 4, 6, 8 Seran de color gris
				if (sectorRow == 3 and (sectorCol == 0 or sectorCol == 6)) or ((sectorRow == 0 or sectorRow == 6) and  sectorCol == 3):
					self.entries[counter] = Text(self, width=2, height=1, bg="grey", font=("Helvetica",22))
				else : 
				#De lo contraio seran blancos
					self.entries[counter] = Text(self, width=2, height=1, font=("Helvetica",22))
				#Decimos donde se va a colocar el cajon en las celda 
				self.entries[counter].grid(row=row, column=column)
				counter += 1

	def clear_text(self, type_ = "All"):
		#Limpia los cajones de texto uno por uno
		for counter in range(self.sizePuzzle):
			self.entries[counter].delete(1.0, END)
		#Si se quiere eliminar todo rasto se hara y se sustituira por un None
		if self.puzzle != None and type_ == "All":
			del self.puzzle
			self.puzzle = None

	def open_sudo(self):
		#limpia los cajones por completo junto con la memoria
		self.clear_text()
		#Abre el archivo con el sudoku a resolver
		self.puzzle = Open_Sudoku("sudoku.txt", 9)
		#Si no se abrio nada manda un error y termina
		if self.puzzle == None:
			messagebox.showwarning("Error", "No se encontro el archivo: sudoku.txt")
			return
		#Si encuentra algo rellena el tablero con los numeros
		self.fill_Suoku()

	def fill_Suoku(self):
		#limpia el tablero sin borrar la lista guardada
		self.clear_text("Normal")
		#Comienza a rellenar los espacios de las celdas con los datos de las listas
		counter = 0
		for rows in self.puzzle:
			for number in rows:
				if number != 0 :
					self.entries[counter].insert('1.0', number)
				counter += 1

	def read_Puzzle(self):
		#Si no existe un sudoku crea uno 
		if self.puzzle == None :
			self.puzzle = []
			counter = 0
			#Lee lo que se encuentra en las celdas 
			for i in range(self.size):
				self.puzzle.append([])
				for number in range(self.size):
					#Guarda lo encontrado en listas de listas solo tomando el primer numero
					#E ignorando los saltos de lineas sustituyendo por 0
					if self.entries[counter].get(1.0) != '\n' :
						self.puzzle[i].append(int(self.entries[counter].get(1.0)))
					else :
						self.puzzle[i].append(0)
					counter += 1
		#Si existe un archivo no lee el tablero y soluciona directo

	def SolvePuzzle(self):
		#Crea un sudoku o verifica que algo exista
		self.read_Puzzle()
		#Soluciona el sudoku por recusrividad
		solve = sudoku(self.puzzle)
		solve.solveSudoku()
		#regrea una lista resuelta
		self.puzzle = solve.puzzle
		#Rellena las celdas con la lsita resuleta
		self.fill_Suoku()

	# Termina el programa y cierra la ventana
	def exitProgram(self):
		exit()

#Funcion que se encarga de crear el tamaño de la ventana, nombre de la misma y
# el loop que actualiza lo que sucede dentro de ella.
def Window_sudoku():
	root = Tk()
	root.geometry("310x340")
	
	program = sudoku_Frame(root)
	
	root.title('Sudoku')
	root.mainloop()