# Nguyen Quoc Huy
# 20127518

def swapRow(A, i, j):
    k = A[i]
    A[i] = A[j]
    A[j] = k


def nulScalar(A, r, k):
    size = len(A[r])
    for m in range(0, size):
        A[r][m] *= k


def addRow(A, r1, k, r2):
    size = len(A[0])
    for i in range(0, size):
        A[r1][i] += k * A[r2][i]

def printMatrix(A):
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            if A[i][j] == 0.0:
                print(abs(A[i][j]), end=" ")
            else:
                print(A[i][j], end=" ")

        print("")
    print("")


def pivoting(A, pRow, pCol):
    n = len(A)
    for i in range(pRow, n):
        if A[i][pCol] != 0:
            nulScalar(A, i, 1 / A[i][pCol])
            swapRow(A, pRow, i)

            #find remaining rows to perform addRow
            for j in range(0, n):
                if pRow == j:
                    continue
                addRow(A, j, -A[j][pCol], pRow)

            return 1
    return 0


def Gauss_elimination(A):
    i, j = 0, 0
    n = len(A)
    m = len(A[0])
    while i < n:
        if pivoting(A, i, j):
            i += 1
        j += 1
        if j == m - 1:
            return


def checkNoSolution(A):
    n = len(A)
    m = len(A[0])
    for i in range(n - 1, -1, -1):
        isZero = 1
        for j in range(m - 2, -1, -1):
            if A[i][j] != 0:
                isZero = 0
                break

        # check right side is not equal to zero and the coefficient is equal to zero, then
        # the system of equations is no solution
        if A[i][m - 1] != 0 and isZero == 1:
            return 1

    return 0


def backSubstitution(A):
    if checkNoSolution(A):
        print("He phuong trinh vo nghiem")
        return

    n = len(A)
    m = len(A[0])
    for i in range (n):
        for j in range (m - 1):
            if A[i][j] == 1:
                outputString = ""
                outputString += 'x{} = '.format(j + 1)

                #check next right elements
                for k in range (j + 1, m - 1):
                    if A[i][k] != 0:
                        sign = ""
                        # switch side => change sign
                        if -A[i][k] > 0:
                            sign = "+"
                        outputString += '{}{}*x{}'.format(sign, -A[i][k], k + 1)

                    j = k

                #if right side is not equal to zero then plus them
                if A[i][j + 1] != 0:
                    sign = "+"
                    if A[i][j + 1] < 0:
                        sign = ""
                    outputString += "{}{}".format(sign, A[i][j + 1])

                print(outputString)
                break

            #free Coefficient
            elif i == j and A[i - 1][j] != 1:
                print('x{} thuoc R'.format(j + 1))

    for i in range (i + 1, m - 1):
        print('x{} thuoc R'.format(i + 1))

def solve(A):
    Gauss_elimination(A)
    printMatrix(A)
    backSubstitution(A)


# Solve problem in lab:

print("Ex1: ")
e1 = [[1, 2, -1, -1], [2, 2, 1, 1], [3, 5, -2, -1]]
solve(e1)

print("Ex2: ")
e2 = [[1, -2, -1, 1], [2, -3, 1, 6], [3, -5, 0, 7], [1, 0, 5, 9]]
solve(e2)

print("Ex3: ")
e3 = [[1, 2, 0, 2, 6], [3, 5, -1, 6, 17], [2, 4, 1, 2, 12], [2, 0, -7, 11, 7]]
solve(e3)

print("Ex4: ")
e4 = [[2, -4, -1, 1], [1, -3, 1, 1], [3, -5, -3, 2], [1, -3, 1, 1]]
solve(e4)

print("Ex5: ")
e5 = [[1, 2, -2, 3], [3, -1, 1, 1], [-1, 5, -5, 5]]
solve(e5)

print("Ex6: ")
e6 = [[2, -4, 6, 8], [1, -1, 1, -1], [1, -3, 4, 0]]
solve(e6)

print("Ex7: ")
e7 = [[4, -2, -4, 2, 1], [6, -3, 0, -5, 3], [8, -4, 28, -44, 11], [-8, 4, -4, 12, -5]]
solve(e7)

print("Ex8: ")
e8 = [[1, -2, 3, -3], [2, 2, 0, 0], [0, -3, 4, 1], [1, 0, 1, -1]]
solve(e8)

print("Ex9: ")
e9 = [[3, -3, 3, -3], [-1, -5, 2, 4], [0, -4, 2, 2], [3, -1, 2, -4]]
solve(e9)

print("Ex10: ")
e10 = [[1, -1, 1, -3, 0], [2, -1, 4, -2, 0]]
solve(e10)

print("Ex11: ")
e11 = [[2, -3, 4, -1, 0], [6, 1, -8, 9, 0], [2, 6, 1, -1, 0]]
solve(e11)

print("Ex12: ")
e12 = [[1, 6, 4, 0], [2, 4, -1, 0], [-1, 2, 5, 0]]
solve(e12)

