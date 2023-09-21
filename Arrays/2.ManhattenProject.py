# Question: Manhattan Project — 3 points

# The Manhattan Project is a highly classified scientific endeavor. 
# The project is experimenting with a list of critical data representing radioactive isotopes.

# the code below prints and empty array, the code must be fixed to print the copied_data array not empty.

original_data = [1, 2, 3, 4, 5]
copied_data = original_data
experiment_data = original_data

for i in range(len(original_data)):
    if original_data[i]%2==0:
        original_data[i] *= 2

if experiment_data==original_data:
    copied_data.clear()

print(copied_data)
    