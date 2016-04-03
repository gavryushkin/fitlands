# Generate 1000 random fitness profiles from [0,1]:

for (i in 1:1000) {
	x <- runif(8, 0, 1)
	write(x, file = "fitnessValues.txt",
	ncolumns = 8,
	append = TRUE);
}

