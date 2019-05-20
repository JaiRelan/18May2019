"""
This can also be done by the simple code using numpy
import numpy as np
A = np.array([[3, 1, 2], [2, 1, 3], [4, 5, 6]])
print(A.dot(A))


Format for squaring a matices:
[x1, x2  * [x1, x2
 y1 ,y2]    y1, y2]
= {[[x1 * x1] + [x1 * y1]} {[[x2 * x1] + [x2 * y2]} {[[y1 * x1] + [y1 * y1]} {[[y2 * y1] + [y2 * y2]}

"""

#Without numpy
x = [int(i) for i in input("Please enter the matrix> ").strip().split(" ")]
(x1, x2, y1, y2) = (x[0], x[1], x[2], x[3])
elem1 = x1 * x1 + x1 * y1
elem2 = x1 * x2 + x2 * y2
elem3 = x1 * y1 + y1 * y1
elem4 = y1 * y2 + y2 * y2

print(elem1, " ", elem2, "\n", elem3, " ", elem4)
