import matplotlib.pyplot as plt

# Show the easiest graph (y = x)
x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.plot(x, y)
plt.show()

# Add the formatting one by one
plt.plot(x, y, 'ro') # Replace the 'ro' by g^, r--, b--, b- and explain differnce
plt.show()

# Show how to limit the numbers on each axis
plt.plot(x, y)
plt.axis([0, 10, 0, 200])
plt.show()

# Add the labels, title, linewidth and legend. Explain the use of each one of them

plt.plot(x, y, 'r--', label = "Y = X", linewidth = 4)
plt.axis([0, 10, 0, 50])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Graph")
plt.legend()
plt.show()

#multiple plots
import numpy as np

x = np.arange(0, 10, 0.2)
print(x)

y1 = x**2 
y2 = x**3

plt.plot(x, y1, 'g--', x, y2, 'b--')
plt.show()



#Task 1 - plot the line y = mx + c using matplotlib 

# Define the slope (m) and y-intercept (c) of the line
m = 2  # slope
c = 1  # y-intercept

# Generate x values for the line
x = np.linspace(-5, 5, 100)  # generate 100 points between -5 and 5

# Calculate corresponding y values
y = m * x + c

# Plot the line
plt.figure(figsize=(8, 6))  # optional, adjust figure size

plt.plot(x, y, label=f'y = {m}x + {c}')  # plot the line
plt.title('Plot of y = mx + c')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()  # show the legend with equation
plt.show()

#Bar Graph
# x cordinate = position of bar
# y cordiante = length of bar

plt.bar([1,3,5,7], [2,6,4,9], color = 'b')
plt.show()

# Showing multiple bars in a single plot
plt.bar([1,3,5,7], [2,6,4,9], color = 'b')
plt.bar([2,4,6,8], [3,5,7,9], color = "g")
plt.show()

# Showing the categorical data using bar plot
plt.bar(["Male Literacy", "Female Literacy"], [90, 95])
plt.show()

# Task2 - Plot the graph of count of passengers in different Pclass on a bar plot

plt.bar(['first class', 'business class', 'economy class'], [12, 30, 53])
plt.show()

#Task 3 - Take Input from user and plot graph 

xVals = []
yVals = []
for i in range(5):
    x = int(input("enter an x value for the equation: "))
    xVals.append(x)

print(xVals)

for i in range(5):
    y = (xVals[i] * 4) + 10
    yVals.append(y)

plt.plot(xVals, yVals, 'g-')
plt.title("custom equation")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()






