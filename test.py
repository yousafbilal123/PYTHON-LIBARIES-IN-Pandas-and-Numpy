from numpy import random
import os
x = random.normal(size=(1000))
print(x)
print("Current working directory:", os.getcwd())
output_directory = 'F:/1bbbbbbbbb/python pratice/numpy/random function third file/'
num_files = 17
for i in range(num_files):
    file_name = f'output_{i + 1}.txt'  
    file_path = os.path.join(output_directory, file_name)  
    try:
        with open(file_path, 'w') as f:
            f.write(str(x))  
        print(f"Output saved to {file_name}")
    except Exception as e:
        print(f"An error occurred while saving {file_name}: {e}")
