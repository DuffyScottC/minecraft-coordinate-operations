# Goal:
Find the minimum number of points that are 15.5 blocks away from at least 1 spawner. 

Find the minimum set of points, P, such that each spawner in set S is within 15.5 blocks of at least one points in P. 

Find the minimum set of points P such that each spawner in set S is within 15.5 blocks of the maximum number of points (at least one) in P, and the points in P are the closest together possible.  

# Steps:

1. Given S - the set of all spawners
2. Find M - the set of all midpoints involving two or more of the points in S
3. Find N - the subset of M such that all midpoints are the within 15.5 blocks of their associated spawners
4. Find J - the subset of N such that no midpoint's set of spawners is a subset of another midpoint's set of spanwers
5. Find E - the set of spawners in S that have no associated midpoint in J
6. Find C - the set of points that are between each point in E and the ultimate midpoint, such that each point is 15.5 blocks away from its respective point in E (this is to fill in any points that were missed. could also find the nearest points on the polygon formed by the other set)

# Example:

## Original:
CSS 1: -235 14 -689
CSS 2: -254 13 -678
CSS 3: -274 8 -672
CSS 4: -207 8 -685

CSS 1: {-235, 14, -689}
CSS 2: {-254, 13, -678}
CSS 3: {-274, 8, -672}
CSS 4: {-207, 8, -685}
Center: {-242.5, 10.75, -681}

## If CSS 1 were 000:
CSS 1: 0 0 0
CSS 2: -19 -1 11
CSS 3: -39 -6 17
CSS 4: 28 -6 4

CSS 1: {0, 0, 0}
CSS 2: {-19, -1, 11}
CSS 3: {-39, -6, 17}
CSS 4: {28, -6, 4}
Center: {-7.5, -3.25, 8}