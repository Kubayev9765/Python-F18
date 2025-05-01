1.
import numpy as np
Original_List=[12.23, 13.32, 100, 36.32]
NumPy_Array=np.array(Original_List)
print(NumPy_Array)
print(type(NumPy_Array))

2.
import numpy as np
arr_matrisa = np.arange(2, 11).reshape(3, 3)
print(arr_matrisa)

3.
import numpy as np
Zero=np.zeros(10)
print(Zero)
Zero[6]=11
print(Zero)

4.
import numpy as np
arr=np.arange(12, 38)
print(arr)

5.
import numpy as np
int_array = np.array([1, 2, 3, 4])
print("Original array:", int_array)
float_array = int_array.astype(float)
print(float_array)

6.
import numpy as np

C = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
print("Values in Centigrade degrees:", C)
F = C * 9/5 + 32
print("Values in Fahrenheit degrees:", F)

7.
import numpy as np
original_array = np.array([10, 20, 30])
print("Original array:", original_array)
values_to_append = [40, 50, 60]
new_array = np.append(original_array, values_to_append)
print("After appending values to the end of the array:", new_array)

8.
import numpy as np

random_array = np.random.rand(10)
print("Random array:", random_array)

mean_val = np.mean(random_array)
median_val = np.median(random_array)
std_dev = np.std(random_array)

print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)

9.
import numpy as np

random_array = np.random.rand(10, 10)
print(random_array)

min_val = np.min(random_array)
max_val = np.max(random_array)

print(min_val)
print( max_val)

10.
import numpy as np

random_array = np.random.rand(3, 3, 3)
print("3x3x3 Random Array:\n", random_array)
