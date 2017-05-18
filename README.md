# K4 

## Problem Description

**Thm:** There is a two-coloring of Kn with at most `nC4*2^-5` monochromatic copies of K4.


## Solution
### Greedy Algorithm
For a typical edge to be colored, we can choose either black or white. However, once we have chosen one color of an edge, the expectation of monochromatic K4 related to it will be changed. 

If a K4 has no colored edge, the expectation to be monochromatic is `2*2^-6=2^-5`. If a K4 has one white edge, the expectation to be monochromatic is `2^-5`. If a K4 has two white edges, the expectation is `2^-4`, etc. And if a black edge is added to a white colored K4, the expectation will be zero.

Since we are going to prove the upper bound, we would like to make the whole expectation decrease. In our algorithm, we compare two expectations between coloring white or black and always select the poorer option. **If the result is under the bound, we can proof that the coloring scheme is existed.** 

### Parameter setting:

```
Point Number: 200
Total Number of K4: 64684950
```
### Parameter Assuming:
```
Black Edge: 1
White Edge: 2
Uncolored Edge: 0
```
### Initialize
A 200*200 matrix M is created to represent the graph. M(i, j) means the edge between vertex i and j. The value of M(i, j) means the color of the edge. 

We use a dictionary to store all the possible K4. The key of dictionary is a string formatted with `a, b, c, d` where `0 ≤ a < b < c < d < 200`. The value corresponding to the key represents the expectation of this K4 to be monochromatic. The inital value is set to be `2^-5`.

The model is initialized as follow:

	pointNum = 200
	dic = {}
	
	edges = [[0 for i in range(pointNum)] for j in range(pointNum)]
	for a in range(pointNum):
	    for b in range(a + 1, pointNum):
	        for c in range(b + 1, pointNum):
	            for d in range(c + 1, pointNum):
	                dic[getKeyFast(a, b, c, d)] = 0.5 ** 5

`getKeyFast` is defined as follow:

	def getKeyFast(a, b, c, d):
	    return '{0},{1},{2},{3}'.format(a, b, c, d)    

### Update Edges
We update edges one by one along rows of the matrix. Every time we choose a smaller expection.

	def updateOneEdge(a, b):
	    blackE = detectAllK4(1, a, b)
	    whiteE = detectAllK4(2, a, b)
	    if blackE > whiteE:
	        color = 2 #white
	    else:
	        color = 1 #black
	    edges[a][b] = color
	    updateAllK4(color, a, b)
	    
`detectAllK4` returns a whole expectation when an edge (a, b) is colored by black or white.
`updateAllK4` updates all K4's expectation and removes those expectation has been zero. 

**You can see more details in source code.**

### Result
Since we remove all the impossible candidates of monochromatic K4, the length of dictionary means our final result.

```
Count: 1890771
Time used: 5661.60205388
```
