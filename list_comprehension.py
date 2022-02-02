"""
Let's learn about list comprehensions! You are given three integers x,y,z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. Please use list comprehensions rather than multiple loops, as a learning exercise.

Example
x =1 
y = 1
z = 2 
n =2
All permutations of [i,j,k] are:

.
Print an array of the elements that do not sum to .


Input Format

Four integers  and , each on a separate line.

Constraints

Print the list in lexicographic increasing order.

Sample Input 0

1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
Explanation 0

Each variable  and  will have values of  or . All permutations of lists in the form .
Remove all arrays that sum to  to leave only the valid permutations.


"""


if __name__ == '__main__':
    x = int(2)
    y = int(2)
    z = int(2)
    n = int(2)

    print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if [a+b+c]!=n ])









