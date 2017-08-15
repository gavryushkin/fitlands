## Detecting genetic interactions from partial fitness orders

Here we implement all the algorithms designed in our forthcoming paper

### Efficient method for detecting genetic interactions from partial fitness rankings

*Abstract.* We present an efficient computational approach for statistical inference of genetic interactions from fitness comparison data.
Genetic interactions are defined by linear forms with integer coefficients in the fitness variables assigned to genotypes.
These forms generalize several popular approaches to study interactions, including Fourier-Walsh coefficients, interaction coordinates, and circuits.
We assume that fitness measurements come with high uncertainty or are even unavailable, as is the case for many empirical studies, and derive interactions from comparisons of genotypes with respect to their fitness -- so-called partial fitness orders.
Specifically, we present a characterization of the class of partial fitness orders that imply interactions, relaying on a graph-theoretic approach.
Our characterization then yields an efficient algorithm for testing the condition when certain genetic interactions, such as sign epistasis, are implied.
This provides an exponential improvement of the best previously known method.
We also provide a geometric interpretation of our characterization, useful for statistical analysis of partial fitness orders and genetic interactions.
The empirical data sets which can be analyzed using our method include competition experiments, fitness proxy measurements (measurable traits monotonic with respect to fitness), survival data, and alike.
