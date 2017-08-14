import re
import sys

file = sys.argv[1]

def make_cube(file):

	if not re.search('^mat',file):
		raise Exception('Must be a matrix file.')

	fd_r = open(file)

	# Read file into matrix
	M = []
	for line in fd_r:
		strings = line.split()
		M.append(list(map(int,strings)))

	# Make title and determine color for tikz file
	newfile = re.sub('mat(s?)','cube\\1',file)+'.tex'
	if re.search('mats',file):
		color='PureRed'
	else: color='black'

	fd_w = open(newfile,'w')

	fd_w.write('\\begin{tikzpicture}\n\
[very thick, color='+color+',->]\n')
	
	#coordinates
	labels = ['000','001','010','011',
			'100','101','110','111' ]
	coord  = [  '(0,0)',
				'(1.2,1)',
				'(0,1)',
				'(1.2,2)',
				'(-1.2,1)',
				'(0,2)',
				'(-1.2,2)',
				'(0,3)' ]
	
	for i,k in enumerate(labels):
		fd_w.write('\\node (n'+str(i)+\
			') at '+coord[i]+' {'+k+'};\n')

	
	for i in range(len(M)):
		for j in range(len(M)):
			if M[i][j]:
				fd_w.write(
				'\\draw '+
				'(n'+str(i)+') -- (n'+str(j)+');\n')
	
	fd_w.write('\\end{tikzpicture}\n')

	fd_w.close()
	fd_r.close()

	return newfile

print(make_cube(file))
