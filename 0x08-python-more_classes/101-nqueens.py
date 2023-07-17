#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for i in range(n):
        a.append([i, None])

    def already_exists(w):
        """check that a queen does not already exist in that w value"""
        for m in range(n):
            if w == a[m][1]:
                return True
        return False

    def reject(m, w):
        """determines whether or not to reject the solution"""
        if (already_exists(w)):
            return False
        i = 0
        while(i < m):
            if abs(a[i][1] - w) == abs(i - m):
                return False
            i += 1
        return True

    def clear_a(m):
        """clears the answers from the point of failure on"""
        for i in range(m, n):
            a[i][1] = None

    def nqueens(m):
        """recursive backtracking function to find the solution"""
        for w in range(n):
            clear_a(m)
            if reject(m, w):
                a[m][1] = w
                if (m == r - 1):  # accepts the solution
                    print(b)
                else:
                    nqueens(m + 1)  # moves on to next m value to continue

    # start the recursive process at m = 0
    nqueens(0)