#Creado por Saenz Barragan Ricardo

#Clase con el sudoku que se encara en resolverlo 
class sudoku:
	#Guarda una lista de listas
	def __init__(self, puzzle):
		self.puzzle = puzzle
		self.size = 3
		self.board_size = self.size*self.size

	#Valida que no se encuentre en la misma columna o fila 
	#al igual verifica el sector
	def isValid(self, search, row, column):
		#los sectores buscan dependiendo de donde empieza en el de 9 x 9
		# los sectores son 0, 3 y 6 ya que son las posiciones donde empieza
		sectorRow = self.size * (row//self.size)
		sectorCol = self.size * (column//self.size)
		#Busca lista y columnas
		for i in range(0,self.board_size):
			if self.puzzle[i][column] == search or self.puzzle[row][i] == search : return False
		#Busca dentro del sector
		for i in range(0, self.size):
			for j in range(0, self.size):
				if self.puzzle[i+sectorRow][j+sectorCol] == search : return False
		#Si pasa por todos es valido el numero
		return True
	#Busca una posicion donde se encuentre un 0 
	#que sera el siguiente lugar a llenar y asi ignorar
	#los que ya tienen un numero escritp
	def findNextCellToFill(self):
		for x in range(0,self.board_size):
			for y in range(0,self.board_size):
				if self.puzzle[x][y] == 0:
					return x,y
		#Si ya todos tienen algo regresa un -1 que representa 
		#que el sudoku esta resuleto
		return -1, -1

	def solveSudoku(self, row = 0, column = 0):
		#Busca las coordenadas para columas y filas
		row, column = self.findNextCellToFill()
		#Si es un -1 entonces el sudoku esta resuelto
		if row == -1:
			return True
		#De un rango del tamaño del tablero busca que numeros son validos
		for nextNum in range(1,self.board_size+1):
			#si el numero es valido intenta con ese y lo coloca
			if self.isValid(nextNum, row, column):
				self.puzzle[row][column] = nextNum
				#Y llama a la misma funcion
				if self.solveSudoku(row, column):
					#el unico caso donde envia esto es si el sudoku esta completamente resuelto
					return True
				#Si la opcion de numero no era valida regresa a 0 e intenta con el siguiente numero
				#de la casilla anterior
				self.puzzle[row][column] = 0
		return False

#Clase con el problema de nQueens que se encara en resolverlo 
class nQueens:
	#Se necesita el tablero y el tamaño del mismo
	def __init__(self, size_of_board, puzzle):

		self.size = size_of_board
		self.puzzle = puzzle


	def isValidDiagonal(x, y):
		#Si una resta de posiciones x Y y en las diagonales es igual entre si significa que se encuentran en 
		#la diagonal de lo contario es valida la posicion
		if x > y:
			return x - y
		else:
			return y - x

	#valida que no se encuentre en la misma columna, o en las diagonales
	def isValid(self, search, column):
		#la posicion de x es igual al numero dentro de la lista y la y es igual al lugar donde se encuentra en la lista
		for i in range(column):
			if self.puzzle[0][i] == search or nQueens.isValidDiagonal(self.puzzle[0][i], search) == nQueens.isValidDiagonal(i, column): 
				return False
		#Si no se encuentra en ninguna de estas entonces es una posicion valida
		return True

	#Funcion que busca ceros para cambiar por numeros
	def findNextCellToFill(self):
		#Busca los ceros para ingresar el siguiente dato
		for y in range(0, self.size):
			if self.puzzle[0][y] == 0:
				#Regresa 
				return y
		#Todos se encuentra lleno, ya no hay ceros
		return -1

	#Funcion que coloca a las reinas en posiciones validas
	def solveQueens(self, column = 0):
		#Busca la posicion donde ingresar el nuevo valor
		column = self.findNextCellToFill()
		#El problema se soluciono 
		if column == -1:
				return True
		#por el tamaño del arreglo busca un numero que cumpla las condiciones
		for nextNum in range(1,self.size+1):
			if self.isValid(nextNum, column):
				self.puzzle[0][column] = nextNum
				if self.solveQueens(column):
					#Solo si el problema se soluciono regresa verdadero
					return True
				#Si no ecnontro una solucion viable cambia a 0 y regresa un paso
				self.puzzle[0][column] = 0
		#reegresa un paso
		return False

