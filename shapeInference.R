setwd("./")

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
);


# TYPE[i] == epistasis type of fitland shape number i:

TYPE <- c(rep(1, 2), rep(2, 8), rep(3, 24), rep(4, 12), rep(5, 24), rep(6, 4));


# Read fitness values from file:
# Rows are the fitness values ordered according to the genotype:
# 000, 001, 010, 011, 100, 101, 110, 111

fvalues = as.matrix(read.table("fitnessValues.txt"));

 
# Compute filand shape for fitness values f:

fitlandShape <- function(f, SHAPE) {
	F <- vector();
	for (i in 1:length(SHAPE)) {
		F[i] <- f %*% SHAPE[[i]];
	}
	return(which(F == max(F)));
}


# Write pairs (fitlandShape, fitlandType) to fitlandShapes.txt
# The third column has 0 if the fitness values correspond to exactly one shape, otherwise the third column enumerates multiple shapes starting from 1.
# If the working folder contains the file called fitlandShapes.txt, that file will be appended. 

for (i in 1:length(fvalues[,1])) {
	x = fitlandShape(fvalues[i,], SHAPE);
	y <- vector();
	if (length(x) == 1){
		y <- c(x[1], TYPE[x[1]], 0);
		print(y);
		write(y, file = "fitlandShapes.txt",
		ncolumns = 3,
		append = TRUE);
	} else {
		print("Non-triangulation shapes present!");
		for (j in 1:length(x)) {
			y <- c(x[j], TYPE[x[j]], j);
			print(y);
			write(y, file = "fitlandShapes.txt",
			ncolumns = 3,
			append = TRUE);
		}}
}

