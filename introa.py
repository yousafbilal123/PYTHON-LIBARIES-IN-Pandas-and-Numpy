from numpy import random
import os


x = random.normal(size=(3,5,7,9))

print(x)
print("Current working directory:", os.getcwd())
try:
    with open('F:/1bbbbbbbbb/python pratice/numpy/random function third file/output.txt', 'w') as f:
        f.write(str(x))
    print("Output saved to output.txt")
except Exception as e:
    print(f"An error occurred: {e}")