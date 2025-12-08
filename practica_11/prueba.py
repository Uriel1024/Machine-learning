import numpy as np

sample_list = [[23, 22, 24, 25], [13, 14, 15, 19]]
new_array = np.array(sample_list)

# Displaying the array

file = open("sample.txt", "w+")

# Saving the array in a text file
content = str(new_array)
file.write(content)
file.close()

# Displaying the contents of the text file
file = open("sample.txt", "r")
content = file.read()

print("Array contents in sample.txt: ", content)
file.close()