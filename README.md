Here we implement all the algorithms designed in the following paper:

## The geometry of partial fitness orders and an efficient method for detecting genetic interactions

Caitlin Lienkaemper, Lisa Lamberti, James Drain, Niko Beerenwinkel, and Alex Gavryushkin

## Abstract

We present an efficient computational approach for detecting genetic interactions from fitness comparison data together with a geometric interpretation using polyhedral cones associated to partial orderings.
Genetic interactions are defined by linear forms with integer coefficients in the fitness variables assigned to genotypes.
These forms generalize several popular approaches to study interactions, including Fourier-Walsh coefficients, interaction coordinates, and circuits.
We assume that fitness measurements come with high uncertainty or are even unavailable, as is the case for many empirical studies, and derive interactions only from comparisons of genotypes with respect to their fitness, i.e.\ from partial fitness orders.
We present a characterization of the class of partial fitness orders that imply interactions, using a graph-theoretic approach.
Our characterization then yields an efficient algorithm for testing the condition when certain genetic interactions, such as sign epistasis, are implied.
This provides an exponential improvement of the best previously known method.
We also present a geometric interpretation of our characterization, which provides the basis for statistical analysis of partial fitness orders and genetic interactions.
