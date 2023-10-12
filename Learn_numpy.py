import numpy as np
My_Arr = np.array([[1,2],[8,9]])
My_Arr
My_Matrix = np.matrix([[1,2],[8,9]])
My_Matrix
My_3D_Arr = np.array([[1,2,10],[3,4,11],[7,8,12]])
Result = My_3D_Arr @ My_3D_Arr
Result
# Multiply arrays 
Result2 = np.dot(My_3D_Arr , My_3D_Arr)
Result2
# Multiply arrays 
np.multiply(My_3D_Arr , My_3D_Arr)
# Multiply each value by its corresponding value 
np.prod(My_3D_Arr) 
# * multiply of all members 
My_Result3 = np.array([1,2,3])
My_Result3 = My_Result3 + 5
My_Result3 
# * Broadcasting
c = np.ones((3,3))
c
c + My_Result3
# * Broadcasting
c = np.ones((3,1))
c
np.zeros((2,3))
b = np.array([3,4,5])
b
c + b
# * Broadcasting
np.sum(My_Result3)
# Sum of all members
c + b
np.sum(c + b)
np.cumsum(c + b)
#  Sum of each element with the sum of the elements before it 
np.cumsum((c + b) , axis = 0)
np.cumsum((c + b) , axis = 1)
np.subtract((c + b) , b)
np.divide([8 , 4 , 3.24] , 2)
np.floor_divide([8 , 4 , 3.24] , 2)
np.math.sqrt(16)
np.math.nan
# nan = not a number
np.math.inf
# inf = infinity
np.random.uniform(1 , 5 , (2,3))
# Random Numbers Between 1 and 5
np.random.standard_normal((3,1))
np.arange(1, 10, 3)
# Creat a sequence of numbers from 1 to 10 with step size = 3
np.linspace(1, 10, 3)
np.linspace(1, 10, 3)
# Take 3 numbers from 1 to 10 
a = np.array([[1,2],[3,4]])
a
np.size(a)
np.shape(a)
First_Arr = ([1,2,5,6,1,8,7,4,3,3,2])
Second_Arr = ([9,2,2,2,7,5,3,11,1])
np.unique(First_Arr)
np.union1d(First_Arr , Second_Arr)
np.intersect1d(First_Arr , Second_Arr)
np.mean(First_Arr )
np.mean(Second_Arr)
np.median(First_Arr)
np.std(First_Arr)
# std = standard deviation
np.var(First_Arr)
# var = variance
Polynomials = np.array([1,3,3])
np.polyval(Polynomials , 4)
# x^2 + 3x + 3 with x=4
np.polyder(Polynomials)
# Derivative 
np.polyint(Polynomials)
#  Integral = x^3/3 + 1.5x^2 + 3x 




