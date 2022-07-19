import numpy as np

a = 42.8
error_a = 7.5
b = 31.2
error_b = 4.3

diff = (a-b)/a


num = a-b
error_num = np.sqrt(error_a**2 + error_b**2)

error_diff = diff * np.sqrt((error_num/num)**2+(error_a/a)**2)

print(f"Difference = {diff*100} \n Error = {error_diff*100}")