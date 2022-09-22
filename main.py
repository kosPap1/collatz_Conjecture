from matplotlib import pyplot as plt
import math
from Collatz_calculation import collatzCalc
from digitClass import digitClass
from trendRemoval import trendRemove
from EvenOddNumbers import evenOddNum

# Calculating the sequence and assigning the results into a list
print('Input number to begin sequence')
k = int(input())
x = collatzCalc(k)

# Counting how many numbers are even or odd at the sequence
[even, odd] = evenOddNum(x)

# Classifying sequence numbers according to their first digit
results = digitClass(x)

# Removing trend by differentiation
trendRem = trendRemove(x)


# Visualization
# plotting initial results
plt.plot(x, label="Initial Results")
plt.title("Collatz Conjecture")
plt.legend()
plt.show()

# Plotting trend removed results
plt.plot(trendRem, label = "Trend Removed Results")
plt.title("Collatz Conjecture, Trend Removed")
plt.legend()
plt.show()

# Plotting number of even numbers in sequence
xAxis = ['even', 'odd']
plt.bar(xAxis, [even, odd])
plt.title(" Even and Odd numbers in sequence")
plt.show()

# Plotting number classification according to their first digit to verify benford's law
xAxisNames = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
plt.bar(xAxisNames, results)
plt.title('Sequence digit classification')
plt.show()









