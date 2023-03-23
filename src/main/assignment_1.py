import numpy as np

# Double Precision
print("Question 1")

j = 0
k = [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
l = [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1]
exp = 0b10000000111 - 1023

index = 0
man = 0.0

while (index <= 11):
    man += 2**(-1 * (index + 1)) * l[index]
    print
    index = index + 1
ans1 = (1 + man) * (2**exp)

print(ans1)
print("\n")

# Three-digit Chopping
print("Question 2")

ans2a = ans1 / 1000
ans2b = ans2a - (0.5 * 10**-3)
print(ans2b)
print("\n")

# Three-digit Rounding
print("Question 3")

ans3a = ans2b + (0.5 * 10**-3)
ans3b = round(ans3a, 3)

print(ans3b)
print("\n")

# Absolute and Relative error
print("Question 4")

ans4a = float(ans1) - float(ans3b) #absolute
print(ans4a)

ans4b = ans4a / float(ans1) #relative
print(ans4b)

print("\n")

# Number of terms
print("Question 5")

error = 1 * 10**-4
k = 1
first = 0
last = 1
while (abs(first - last) > error):
    last = first
    first = first + (-1**k) * (1**k) / (k**3)
    k = k + 1
print(k)
print("\n")

print("Question 6")
