# Question 1: Airplanes — 2 points

# There is a bug in this code. the output should print, southwest, delta, american airlines, alaska airlines
# Find the mistake in the problem and correct the Code


airplanes = ["southwest", "American Airlines", "Delta", "Alaska Airlines"]
airplanes.sort()
airplanes[::-1]

print("Sorted airplanes in reverse order:")
for plane in airplanes:
    print(plane)

