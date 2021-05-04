#Gauss Area
diagonal_number = int(input("Enter the number of diagonals:"))
diagonal_list_x = []
diagonal_list_y = []
for i in range(1,diagonal_number+1):
    diagonal_list_x.append(int(input("x:")))
    diagonal_list_y.append(int(input("y:")))
area = 0
x_list = diagonal_list_x
y_list = diagonal_list_y

for i in range(1,diagonal_number):
    if i == 0:
        area += (y_list[i]*(x_list[-1]-x_list[i+1]))
    elif (i != 0) and (i != diagonal_number-1):
        area += (y_list[i]*(x_list[i-1]-x_list[i+1]))
    else:
        area += (y_list[i]*(x_list[i-1]-x_list[0]))
print("X:",x_list,"Y:",y_list)
print("Area:",abs(area/2))
