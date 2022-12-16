import time 
start = time.time()

 
# iterative sum
total = 0
# iterating through 1.5 Million numbers
for item in range(0, 1500000):
    total = total + item


print('sum is:' + str(total))
end = time.time()

print(end - start)

# # out Put
# sum is:1124999250000
# 0.28600597381591797


# __________________________________________________

import numpy as np
import time 
start = time.time()

# vectorized sum - using numpy for vectorization
# np.arange create the sequence of numbers from 0 to 1499999
print(np.sum(np.arange(1500000)))

end = time.time()

print(end - start)



#output

# 1124999250000
# 0.017840862274169922

# ___________________________________________________
