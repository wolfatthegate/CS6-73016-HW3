# CS 6-73016 – Waylon Luo
# Homework 3 problem 2). Jaccard Distance example
# Dist(ab) + Dist(bc) >= Dist(ac)

import numpy as np

a = [0, 1, 2, 5, 6, 8, 9]
b = [0, 2, 3, 4, 5, 7, 9]
c = [0, 1, 2, 5, 6, 7, 9]
d = []
#define Jaccard Similarity function
def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

#find Jaccard Similarity between the two sets 
print('Jaccard dist(a,b) - ', jaccard(a, b))
print('Jaccard dist(b,c) - ', jaccard(b, c))
print('Jaccard dist(a,c) - ', jaccard(a, c))
print('Jaccard dist(a,c) - ', jaccard(a, a))
print('Jaccard dist(a,c) - ', jaccard(a, d))
