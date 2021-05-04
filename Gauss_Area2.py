def polygonArea(X, Y, diagonal_number):
    area = 0.0
    j = diagonal_number - 1
    for i in range(0, diagonal_number):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i
    return int(abs(area/2.0))

# Driver program to test above function
X = [0.0,4.0,4.0,0.0]
Y = [0.0,0.0,4.0,4.0]
diagonal_number = len(X)
print("X:",X,"Y:",Y,"Area:",polygonArea(X, Y, diagonal_number))

