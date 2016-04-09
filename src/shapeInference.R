setwd("~/Documents/fitlands/")

# List of fitland shapes:

SHAPE <- list(

	# Type 1
	c(1, 5, 5, 1, 5, 1, 1, 5),	# 1
	c(5, 1, 1, 5, 1, 5, 5, 1),	# 2

	# Type 2
	c(1, 4, 4, 3, 6, 1, 1, 4),	# 3
	c(1, 4, 6, 1, 4, 3, 1, 4),	# 4
	c(1, 6, 4, 1, 4, 1, 3, 4),	# 5
	c(3, 4, 4, 1, 4, 1, 1, 6),	# 6
	c(4, 1, 1, 6, 3, 4, 4, 1),	# 7
	c(4, 1, 3, 4, 1, 6, 4, 1),	# 8
	c(4, 3, 1, 4, 1, 4, 6, 1),	# 9
	c(6, 1, 1, 4, 1, 4, 4, 3),	# 10

	# Type 3
	c(1, 3, 4, 4, 6, 2, 1, 3),	# 11
	c(1, 3, 6, 2, 4, 4, 1, 3),	# 12
	c(1, 4, 3, 4, 6, 1, 2, 3),	# 13
	c(1, 4, 6, 1, 3, 4, 2, 3),	# 14
	c(1, 6, 3, 2, 4, 1, 4, 3),	# 15
	c(1, 6, 4, 1, 3, 2, 4, 3),	# 16
	c(2, 3, 3, 4, 6, 1, 1, 4),	# 17
	c(2, 3, 6, 1, 3, 4, 1, 4),	# 18
	c(2, 6, 3, 1, 3, 1, 4, 4),	# 19
	c(3, 1, 2, 6, 4, 4, 3, 1),	# 20
	c(3, 1, 4, 4, 2, 6, 3, 1),	# 21
	c(3, 2, 1, 6, 4, 3, 4, 1),	# 22
	c(3, 2, 4, 3, 1, 6, 4, 1),	# 23
	c(3, 4, 1, 4, 2, 3, 6, 1),	# 24
	c(3, 4, 2, 3, 1, 4, 6, 1),	# 25
	c(4, 1, 1, 6, 4, 3, 3, 2),	# 26
	c(4, 1, 4, 3, 1, 6, 3, 2),	# 27
	c(4, 3, 3, 2, 4, 1, 1, 6),	# 28
	c(4, 3, 4, 1, 3, 2, 1, 6),	# 29
	c(4, 4, 1, 3, 1, 3, 6, 2),	# 30
	c(4, 4, 3, 1, 3, 1, 2, 6),	# 31
	c(6, 1, 1, 4, 2, 3, 3, 4),	# 32
	c(6, 1, 2, 3, 1, 4, 3, 4),	# 33
	c(6, 2, 1, 3, 1, 3, 4, 4),	# 34

	# Type 4
	c(1, 3, 3, 5, 5, 3, 3, 1),	# 35
	c(1, 3, 5, 3, 3, 5, 3, 1),	# 36
	c(1, 5, 3, 3, 3, 3, 5, 1),	# 37
	c(3, 1, 3, 5, 5, 3, 1, 3),	# 38
	c(3, 1, 5, 3, 3, 5, 1, 3),	# 39
	c(3, 3, 1, 5, 5, 1, 3, 3),	# 40
	c(3, 3, 5, 1, 1, 5, 3, 3),	# 41
	c(3, 5, 1, 3, 3, 1, 5, 3),	# 42
	c(3, 5, 3, 1, 1, 3, 5, 3),	# 43
	c(5, 1, 3, 3, 3, 3, 1, 5),	# 44
	c(5, 3, 1, 3, 3, 1, 3, 5),	# 45
	c(5, 3, 3, 1, 1, 3, 3, 5),	# 46

	# Type 5
	c(1, 3, 3, 5, 6, 2, 2, 2),	# 47
	c(1, 3, 6, 2, 3, 5, 2, 2),	# 48
	c(1, 6, 3, 2, 3, 2, 5, 2),	# 49
	c(2, 2, 2, 6, 5, 3, 3, 1),	# 50
	c(2, 2, 3, 5, 6, 2, 1, 3),	# 51
	c(2, 2, 5, 3, 2, 6, 3, 1),	# 52
	c(2, 2, 6, 2, 3, 5, 1, 3),	# 53
	c(2, 3, 2, 5, 6, 1, 2, 3),	# 54
	c(2, 3, 6, 1, 2, 5, 2, 3),	# 55
	c(2, 5, 2, 3, 2, 3, 6, 1),	# 56
	c(2, 6, 2, 2, 3, 1, 5, 3),	# 57
	c(2, 6, 3, 1, 2, 2, 5, 3),	# 58
	c(3, 1, 2, 6, 5, 3, 2, 2),	# 59
	c(3, 1, 5, 3, 2, 6, 2, 2),	# 60
	c(3, 2, 1, 6, 5, 2, 3, 2),	# 61
	c(3, 2, 5, 2, 1, 6, 3, 2),	# 62
	c(3, 5, 1, 3, 2, 2, 6, 2),	# 63
	c(3, 5, 2, 2, 1, 3, 6, 2),	# 64
	c(5, 2, 3, 2, 3, 2, 1, 6),	# 65
	c(5, 3, 2, 2, 3, 1, 2, 6),	# 66
	c(5, 3, 3, 1, 2, 2, 2, 6),	# 67
	c(6, 1, 2, 3, 2, 3, 2, 5),	# 68
	c(6, 2, 1, 3, 2, 2, 3, 5),	# 69
	c(6, 2, 2, 2, 1, 3, 3, 5),	# 70

	# Type 6
	c(2, 2, 2, 6, 6, 2, 2, 2),	# 71
	c(2, 2, 6, 2, 2, 6, 2, 2),	# 72
	c(2, 6, 2, 2, 2, 2, 6, 2),	# 73
	c(6, 2, 2, 2, 2, 2, 2, 6)	# 74
)


# TYPE[i] == epistasis type of fitland shape number i:

TYPE <- c(rep(1, 2), rep(2, 8), rep(3, 24), rep(4, 12), rep(5, 24), rep(6, 4))


# Read fitness values from file:
# Rows are the fitness values ordered according to the genotype:
# 000, 001, 010, 011, 100, 101, 110, 111

fvalues = as.matrix(read.table("fitnessValues.txt"))

 
# Compute filand shape for fitness values f:

fitlandShape <- function(f, SHAPE) {
	F <- vector()
	for (i in 1:length(SHAPE)) {
		F[i] <- f %*% SHAPE[[i]]
	}
	return(which(F == max(F)))
}


# Write pairs (fitlandShape, fitlandType) to fitlandShapes.txt
# The third column has 0 if the fitness values correspond to exactly one shape, otherwise the third column enumerates multiple shapes starting from 1.
# If the working folder contains the file called fitlandShapes.txt, that file will be appended. 

for (i in 1:length(fvalues[,1])) {
	x = fitlandShape(fvalues[i,], SHAPE)
	y <- vector()
	if (length(x) == 1){
		y <- c(x[1], TYPE[x[1]], 0)
		write(y, file = "fitlandShapes.txt",
		ncolumns = 3,
		append = TRUE)
	} else {
		print("Non-triangulation shapes present!")
		for (j in 1:length(x)) {
			y <- c(x[j], TYPE[x[j]], j)
			write(y, file = "fitlandShapes.txt",
			ncolumns = 3,
			append = TRUE)
		}}
}


# Compute probabilities of shapes from fitlandShapes.txt:

shapes = as.matrix(read.table("fitlandShapes.txt"))

shape_probabilities <- vector(mode = "double", length = 74)
N <- length(shapes[,1])
for (i in 1:N) {
	shape_probabilities[shapes[i][1]] <- shape_probabilities[shapes[i][1]] + 1
}
shape_probabilities <- shape_probabilities / N

# Print shape probability histogram into shapeProbaHisto.pdf:

print(shape_probabilities)
pdf("shapeProbaHisto.pdf")
hist(shapes[,1], freq = FALSE, breaks = N)
dev.off()


# Print graph induced by secondary polytope to secondaryPolyGraph.pdf:

library(igraph)

secondaryPolyEdges <- c(
	1,3, 1,4, 1,5, 1,6,				# Type 1
	2,7, 2,8, 2,9, 2,10,
	3,1, 3,11, 3,13, 3,17,				# Type 2
	4,1, 4,12, 4,14, 4,18,
	5,1, 5,15, 5,16, 5,19,
	6,1, 6,28, 6,29, 6,31,
	7,2, 7,20, 7,22, 7,26,
	8,2, 8,21, 8,23, 8,27,
	9,2, 9,24, 9,25, 9,30,
	10,2, 10,32, 10,33, 10,34,
	11,3, 11,12, 11,47, 11,51,			# Type 3
	12,4, 12,11, 12,48, 12,53,
	13,3, 13,15, 13,47, 13,54,
	14,4, 14,16, 14,48, 14,55,
	15,5, 15,13, 15,49, 15,57,
	16,5, 16,14, 16,49, 16,58,
	17,3, 17,28, 17,51, 17,54,
	18,4, 18,29, 18,53, 18,55,
	19,5, 19,31, 19,57, 19,58,
	20,7, 20,21, 20,50, 20,59,
	21,8, 21,20, 21,52, 21,60,
	22,7, 22,24, 22,50, 22,61,
	23,8, 23,25, 23,52, 23,62,
	24,9, 24,22, 24,56, 24,63,
	25,9, 25,23, 25,56, 25,64,
	26,7, 26,32, 26,59, 26,61,
	27,8, 27,33, 27,60, 27,62,
	28,6, 28,17, 28,65, 28,66,
	29,6, 29,18, 29,65, 29,67,
	30,9, 30,34, 30,63, 30,64,
	31,6, 31,19, 31,66, 31,67,
	32,10, 32,26, 32,68, 32,69,
	33,10, 33,27, 33,68, 33,70,
	34,10, 34,30, 34,69, 34,70,
	35,36, 35,37, 35,47, 35,50,			# Type 4
	36,35, 36,37, 36,48, 36,52,
	37,35, 37,36, 37,49, 37,56,
	38,39, 38,44, 38,51, 38,59,
	39,38, 39,44, 39,53, 39,60,
	40,42, 40,45, 40,54, 40,61,
	41,43, 41,46, 41,55, 41,62,
	42,40, 42,45, 42,57, 42,63,
	43,41, 43,46, 43,58, 43,64,
	44,38, 44,39, 44,65, 44,68,
	45,40, 45,42, 45,66, 45,69,
	46,41, 46,43, 46,67, 46,70,
	47,11, 47,13, 47,35, 47,71,			# Type 5
	48,12, 48,14, 48,36, 48,72,
	49,15, 49,16, 49,37, 49,73,
	50,20, 50,22, 50,35, 50,71,
	51,11, 51,17, 51,38, 51,71,
	52,21, 52,23, 52,36, 52,72,
	53,12, 53,18, 53,39, 53,72,
	54,13, 54,17, 54,40, 54,71,
	55,14, 55,18, 55,41, 55,72,
	56,24, 56,25, 56,37, 56,73,
	57,15, 57,19, 57,43, 57,73,
	58,16, 58,19, 58,43, 58,73,
	59,20, 59,26, 59,38, 59,71,
	60,21, 60,27, 60,39, 60,72,
	61,22, 61,26, 61,40, 61,71,
	62,23, 62,27, 62,41, 62,72,
	63,24, 63,30, 63,42, 63,73,
	64,25, 64,30, 64,32, 64,73,
	65,28, 65,29, 65,44, 65,74,
	66,28, 66,31, 66,45, 66,74,
	67,29, 67,31, 67,46, 67,74,
	68,32, 68,33, 68,44, 68,74,
	69,32, 69,34, 69,45, 69,74,
	70,33, 70,34, 70,46, 70,74,
	71,47, 71,50, 71,51, 71,54, 71,59, 71,61,	# Type 6
	72,48, 72,52, 72,53, 72,55, 72,60, 72,62,
	73,49, 73,56, 73,57, 73,58, 73,63, 73,64,
	74,65, 74,66, 74,67, 74,68, 74,69, 74,70
)

spg <- make_empty_graph(n = 74, directed = FALSE) %>%
	add_edges(secondaryPolyEdges) %>%
	set_edge_attr("color", value = "red")
vertex_sizes <- shape_probabilities * 500
E(spg)[[]]
plot(spg, layout = layout_with_kk, vertex.size = vertex_sizes)
pdf("secondaryPolyGraph.pdf")
plot(spg, layout = layout_with_kk, vertex.size = vertex_sizes)
dev.off()

