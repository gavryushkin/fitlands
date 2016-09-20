# Fitlands

Software package for gene interaction analysis based on partial orders of genotypes, such as fitness graphs, rank orders, etc.


## Software requirements
The package is still under development but a number of tools are already stable and ready for alpha release.
Prior to the release, the best way to try the software is to have [Python](https://www.python.org/) in the form of [Anaconda](https://www.continuum.io/downloads) installed, clone this repository, and follow the instructions below.
Otherwise, make sure that all imports are installed.
Those include `numpy`, `pandas`, `networkx`, `pylab`.

First install [git](https://git-scm.com/), then clone this repository:
```
git clone https://github.com/gavruskin/fitlands.git
```
then
```
cd fitlands
```
and then run the analysis of interest.

For example, for the analysis of two- and three-way interactions in your data, run
```
python two_and_three_way_interactions.py
```
after putting your data file in the folder `fitlands`.
See [below](https://github.com/gavruskin/fitlands#analysis-of-two--and-three-way-interactions) to learn how to format your data file and other details of this analysis.


## HIV data analysis from [\[1\]](https://github.com/gavruskin/fitlands#references)
To reproduce the analysis of the HIV-1 data from the upcoming paper by Krona, Gavryushkin, Greene, and Beerenwinkel [\[1\]](https://github.com/gavruskin/fitlands#references), run the `data_HIV_2007_circuit_analysis.py` script, for example, by:
```
python data_HIV_2007_circuit_analysis.py
```
The result is the following:
### Analysis of interaction coordinates and circuit interactions
The three-way interaction corresponds to the last interaction coordinate u(111)

Rank order: [000, 100, 011, 110, 101, 001, 010, 111]


#### Interaction coordinates

u(011) = w(000) - w(001) - w(010) + w(100) + w(011) - w(101) - w(110) + w(111) does not imply interaction  
u(101) = w(000) - w(001) + w(010) - w(100) - w(011) + w(101) - w(110) + w(111) does not imply interaction  
u(110) = w(000) + w(001) - w(010) - w(100) - w(011) - w(101) + w(110) + w(111) does not imply interaction  
u(111) = w(000) - w(001) - w(010) - w(100) + w(011) + w(101) + w(110) - w(111) implies positive interaction  


#### Circuits

The number of circuits for which the rank order implies circuit interaction: 11 (55.0%)  
The number of circuits for which the rank order implies *positive* circuit interaction: 6 (30.0%)  
The number of circuits for which the rank order implies *negative* circuit interaction: 5 (25.0%)  


##### List of circuits for which the rank order implies *positive* interaction

a = w(000) - w(010) - w(100) + w(110)  
c = w(000) - w(001) - w(100) + w(101)  
e = w(000) - w(001) - w(010) + w(011)  
h = w(001) - w(010) - w(101) + w(110)  
p = w(000) - 2w(001) + w(011) + w(101) - w(110)  
r = w(000) - 2w(010) + w(011) - w(101) + w(110)  


##### List of circuits for which the rank order implies *negative* interaction

b = w(001) - w(011) - w(101) + w(111)  
d = w(010) - w(011) - w(110) + w(111)  
j = w(001) - w(100) - w(011) + w(110)  
l = w(010) - w(100) - w(011) + w(101)  
t = w(001) + w(010) - w(100) - 2w(011) + w(111)  


##### List of circuits followed by the interaction sign implied by the rank order

Circuit | Interaction sign
--- | ---
a = w(000) - w(010) - w(100) + w(110) | +
b = w(001) - w(011) - w(101) + w(111) | -
c = w(000) - w(001) - w(100) + w(101) | +
d = w(010) - w(011) - w(110) + w(111) | -
e = w(000) - w(001) - w(010) + w(011) | +
f = w(100) - w(101) - w(110) + w(111) | +/-
g = w(000) - w(100) - w(011) + w(111) | +/-
h = w(001) - w(010) - w(101) + w(110) | +
i = w(000) - w(010) - w(101) + w(111) | +/-
j = w(001) - w(100) - w(011) + w(110) | -
k = w(000) - w(001) - w(110) + w(111) | +/-
l = w(010) - w(100) - w(011) + w(101) | -
m = -2w(000) + w(001) + w(010) + w(100) - w(111) | +/-
n = -w(000) + w(011) + w(101) + w(110) - 2w(111) | +/-
o = -w(001) + w(010) + w(100) - 2w(110) + w(111) | +/-
p = w(000) - 2w(001) + w(011) + w(101) - w(110) | +
q = w(001) - w(010) + w(100) - 2w(101) + w(111) | +/-
r = w(000) - 2w(010) + w(011) - w(101) + w(110) | +
s = w(000) - 2w(100) - w(011) + w(101) + w(110) | +/-
t = w(001) + w(010) - w(100) - 2w(011) + w(111) | -


## Analysis of partial orders

A _partial order_ is given by a list of pairs of genotypes such that the first genotype is *less fit* than the second genotype.
An example of a partial order is the fitness graph of mutational neighbors.

This analysis takes a file with partial orders and returns a file with the analysis of three-way interactions implied by those partial orders: the number of total extensions of each of the partial orders with numbers and fractions of total orders that imply the three-way interaction.

To perform the analysis, inside the cloned folder `fitlands`, create a new folder called `outputs`.
Put the file with your partial orders into that folder.
You can choose your favorite name for the file but in what follows I will assume the file with partial orders is called `partial_orders.md`

The file must contain no symbols apart from `0` `1` `[` `]` `,`(comma) ` `(space).
Every partial order must be on its own line.
The balance of parentheses, empty lines, and spaces are not important.
The most important feature of the formatting is the correct number of commas: exactly one comma must separate genotypes in every comparison pair and exactly one comma must separate comparison pairs.
An example of an acceptable file containing four partial orders is the following:
```
[000, 001], [001, 010], [010, 100], [100, 101], [101, 110], [110, 111]

[000, 001], [001, 010], [010, 011], [011, 100], [100, 101], [101, 110], [110, 111]

[000, 001], [011, 010], [101, 100], [110, 111]

[000, 001]

```
The analysis can be run, for example, by:

```
python -c "from partial_order_interaction import analyze_partial_orders; analyze_partial_orders('partial_orders.md')"
```
It is important to run this script inside the cloned folder `fitlands` (and not, for instance, inside its sub-folders such as `outputs`).

The result of the analysis will be written into the file called `partial_orders_analysis.md` inside the `outputs` folder.

If a more detailed output is necessary, you can trigger the option `details` by running:
```
python -c "from partial_order_interaction import analyze_partial_orders; analyze_partial_orders('partial_orders.md', True)"
```
This analysis takes longer, but the result is more detailed: the output contains two files inside the `output` folder.
The first file `partial_orders_analysis.md` is identical to the previous analysis and the second file `partial_orders_analysis_details.md` contains the lists of all total extensions of the partial orders, along with the sign of three-way interactions.


## Analysis of circuit interactions

Does the same thing as `analyze_partial_orders` but with respect to the given circuit instead of the plain `u_111` (three-way interaction), which is the default option.
See [\[2\]](https://github.com/gavruskin/fitlands#references) for details on circuits.
With defaults the analysis is identical to `analyze_partial_orders`.
If `genotype_format == True` (default), positives and negatives are taken in the {0, 11, 101} format, otherwise---in the index format: {1, 5, 6}.

Example of usage:
```
python -c "from partial_order_interaction import analyze_partial_orders_for_circuit; analyze_partial_orders_for_circuit('partial_orders.md', True, {0, 11}, {1, 10})"
```
The reason to keep both `analyze_partial_orders` and `analyze_partial_orders_for_circuit` is that the former should be more efficient, but that has to be tested.


## Analysis of rank orders

A _rank order_ is a ranking of genotypes according to their fitness *from high to low*, for example, the rank order [0, 11, 110, 101, 1, 10, 100, 111] implies that the wild-type is the most fit, the double mutants are fitter than the single mutants, and the triple mutant is the least fit genotype.

The analysis takes a total order as an input in the genotype format, e.g. {0, 11, 101}, if `genotype_format == True` (default), or in the index format, e.g. {1, 5, 6}, otherwise.
Returns a file with the analysis of interactions implied by the rank order `total_order` for all 24 circuits (see [\[2\]](https://github.com/gavruskin/fitlands#references) for the background on circuit interactions).
An example of usage for the rank order above is the following:
```
python -c "from partial_order_interaction import analyze_total_order_for_all_circuits; analyze_total_order_for_all_circuits('[0, 11, 110, 101, 1, 10, 100, 111]')"
```

First few lines of the example output:
```
# Analysis of circuit interactions for all 24 circuits
The three-way interaction corresponds to the last circuit:
w(000) - w(001) - w(010) - w(100) + w(011) + w(101) + w(110) - w(111)

Rank order: [000, 011, 110, 101, 001, 010, 100, 111]

The number of circuits for which the rank order implies circuit interaction: 14 (58.33%)
The number of circuits for which the rank order implies *positive* circuit interaction: 8 (33.33%)
 14 The number of circuits for which the rank order implies *negative* circuit interaction: 6 (25.0%)


## List of circuits for which the rank order implies *positive* interaction

w(000) - w(010) - w(100) + w(110)
w(000) - w(001) - w(100) + w(101)
w(000) - w(001) - w(010) + w(011)
w(001) - w(010) - w(101) + w(110)
w(000) + 2w(001) + w(011) + w(101) - w(110)
w(000) - 2w(010) + w(011) - w(101) + w(110)
w(000) - 2w(100) - w(011) + w(101) + w(110)
w(000) - w(001) - w(010) - w(100) + w(011) + w(101) + w(110) - w(111)

```


## Analysis of two- and three-way interactions

TBA


## References
[1] Crona, Gavryushkin, Greene, and Beerenwinkel. New tools for detecting higher order epistasis. _To appear,_ 2016.

[2] Beerenwinkel, Pachter, and Sturmfels. Epistasis and Shapes of Fitness Landscapes. _Statistica Sinica,_ 17: 1317-42, 2007.

