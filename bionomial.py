from numpy import random
import os
x = random.binomial(n=10, p=0.5, size=10)
print(x)

print("Current working directory:", os.getcwd())

try:
    with open('F:/1bbbbbbbbb/python pratice/numpy/output.txt', 'w') as f:
        f.write(str(x))
    print("Output saved to output.txt")
except Exception as e:
    print(f"An error occurred: {e}")