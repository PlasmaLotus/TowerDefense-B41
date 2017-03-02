import os

def _print(grille):
	for row in grille:
		for i in row:
			print(i, end=' ')
		print()

def cls():
	os.system('cls' if os.name=='nt' else 'clear')

def main():
	w = 10
	h = 10
	x = 0
	y = 4
	grille = [["*" for _ in range(w)] for _ in range(h)]
	grille[y][x] = 'c'
	rep = ''
	cls()
	while(rep != 'Q'):
		_print(grille)
		rep = input('entrez qqch')
		grille[y][x] = '*'
		x += 1
		grille[y][x] = 'c'
		cls()

class Controlleur:
	def __init

if __name__ == '__main__':
	c = Controlleur()	