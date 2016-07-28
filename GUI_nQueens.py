#Creado por Saenz Barragan Ricardo

#Interfaz Grafica
from tkinter import *
from tkinter import messagebox
#Solucion recursiva del problema
from class_problem import nQueens

#Clase que se encarga de crear la ventana y lo que contiene 
# Ya sea las funciones que se realizan dentro de ella y los graficos que aparecen
class Queen_Frame(Frame):
	#inicialisa creando por predeterminado un tamaño 0 para que 
	#no se cre nada y la pantalla este en blanco
	#y una lista que es el puzzle
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.grid()
		self.size = 0
		self.puzzle = None
		self.create_window()
	#Crea la ventana que se estara actualizando, un diccionario que guarda las casillas para 
	#escribir y el tamaño del tablero
	def create_window(self):
		self.entries = {}

		self.pack(fill=BOTH, expand= 1)
		#Botones que se encargan de empezar las funciones

		#Resuleve lo escrito en el tablero
		solve = Button(self, text= 'Solve', width = 6, height = 2, command=self.SolvePuzzle)
		solve.place(x=100, y=500)
		#Crea el tamaño del tablero que se escribe
		Create_ = Button(self, text= 'Create', width = 6, height = 2, command=self.Create_grid)
		Create_.place(x=155, y=500)
		#Termina el programa
		exit = Button(self, text= 'Exit', width = 6, height = 2, command=self.exitProgram)
		exit.place(x=210, y=500)
		#celda donde se escribe el tamaño del tablero a resolver
		self.input_ = Entry(self, width=10, bg="grey", font=("Helvetica",22))
		self.input_.place(x=265, y=500)

	#Crea el tablero de tamaño que se escribio usando cajones para escribir
	#contador que sera la llave de  diccionario para los cajones
	def crate_grid_UI(self):
		tableheight = self.size
		tablewidth = self.size
		counter = 0
		#chek es lo que crea el patron de uno negro uno blanco (uno si otro no)
		chek = True
		for row in range(tableheight):
			for column in range(tablewidth):

				if chek:
					self.entries[counter] = Text(self, width=2, height=1, bg="grey", font=("Helvetica",22), state=DISABLED)
				else : 
					self.entries[counter] = Text(self, width=2, height=1, font=("Helvetica",22), state=DISABLED)

				self.entries[counter].grid(row=row, column=column)
				
				chek = not chek
				counter += 1

			if self.size % 2 == 0:
				chek = not chek

	#Con la respuesta que se genere rellena los espacios que deben de llevar una reina
	def fill_Queens(self):

		counter = 0
		for rows in range(self.size):
			for columns in range(self.size):
				#Si el numero es igual de la lista en columna
				#Se escribe una R de lo contrario se salta
				if self.puzzle[0][columns] == rows+1 :
					self.entries[counter].config(state = NORMAL)
					self.entries[counter].insert('1.0', 'R')
				counter += 1

	#Crea una lista con la cantidad de reinas que van a ir, esta lsita era unidimencional
	#y solo guarda las posiciones de las reinas
	def create_puzzle(self):

		self.puzzle = [[]]
		for i in range(self.size):
			self.puzzle[0].append(0)
			
	#Solución del problema con ayuda de recursividad
	def SolvePuzzle(self):
		#Si ninca se ingreso un valor valido entonces no se puede resolver y manda un error
		if self.size == 0:
			messagebox.showwarning("Error", "Ingrese el tamaño del tablero.")
			return
		#Crea el puzzle
		self.create_puzzle()
		#Soluciona el problema sgun el tamaño 
		solve = nQueens(self.size, self.puzzle)
		solve.solveQueens()
		#guarda la lista con la solucion
		self.puzzle = solve.puzzle
		#Llena las celdas del tablero
		self.fill_Queens()

	#Verifica el numero que se ingresa para crear el tablero
	def Create_grid(self):
		if self.input_.get().isdigit():
			#Si es menor a 4 es imposible y manda error
			if int(self.input_.get()) < 4:
				messagebox.showwarning("Error", "Este problema es imposible\nsi se tienen menos de 4 espacios.")
				return
			#De lo contrario guarda el tamaño y genera el tablero
			self.size = int(self.input_.get())
			self.crate_grid_UI()

	# Termina el programa y cierra la ventana
	def exitProgram(self):
		exit()

#Funcion que se encarga de crear el tamaño de la ventana, nombre de la misma y
# el loop que actualiza lo que sucede dentro de ella.
def Window_queens():
	root = Tk()
	root.geometry("510x540")
	
	program = Queen_Frame(root)
	
	root.title('N-Queens')
	root.mainloop()

