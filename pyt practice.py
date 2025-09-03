# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 08:52:18 2025

@author: Loh Jiang Joe
"""

import sys
print(sys.version)

"""
hii
hiiiii
hiiiiii
"""
#Use a multiline string to make the a multiline comment:

"""
This is a multiline string.
It can have 3 lines,
4 lines,
or more.
"""
print("Hello, World!")

x = 5
y = "John"
print(type(x))
print(type(y))

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
# x will be overwrite with new varible

x = "awesome"  # 1️⃣ Global variable

def myfunc():
    print("Python is " + x)  # 2️⃣ Using the global variable

myfunc()  # 3️⃣ Function call， This runs the function, so it prints:

# eg
x = "awesome"

def myfunc():
    x = "fantastic"  # local variable, shadows the global x
    print("Python is " + x)

myfunc()     # Python is fantastic
print(x)     # awesome (global x is unchanged)

# next: (可以chatgpt解释)
x = 'awesome'   # 1️⃣ global variable

def myfunc():
    x = 'fantastic'   # 2️⃣ local variable (only inside myfunc)

myfunc()  # 3️⃣ run the function
print('Python is ' + x)  # 4️⃣ print using the global x

# list
fruits = ["apple", "banana", "cherry"]
print(fruits[0])     # apple (indexing starts at 0)

# Lists are mutable:
fruits[1] = "mango"   # change banana → mango
fruits.append("orange")   # add item at the end
print(fruits)  # ['apple', 'mango', 'cherry', 'orange']


#tuple
colors = ("red", "green", "blue")
print(colors[1])   # green

# Tuples are immutable:
# colors[1] = "yellow"  ❌ ERROR (cannot modify)

# dictionary (dict)
student = {
    "name": "JJ",
    "age": 21,
    "course": "Physics"
}

print(student["name"])   # JJ
print(student["age"])    # 21

# data type
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


# string in multiple line
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Text vs Bytes

#Text = human-readable characters ("A", "你", "😊")

#Bytes = raw numbers that computers actually store (e.g., 01000001 for "A")

#Computers don’t understand characters directly. They only understand bytes (numbers).

#What is Unicode?

#Unicode is a universal standard that assigns a unique number (code point) to every character in every language, symbol, or emoji.
#Examples:

#"A" → U+0041

#Example:  bytes in python
s = "Hello 😊"

b = s.encode("utf-8")  # str → bytes
print(b)               # b'Hello \xf0\x9f\x98\x8a'
print(len(b))          # 10 bytes

t = b.decode("utf-8")  # bytes → str
print(t)               # Hello 😊

# "😊" looks like 1 character, but in UTF-8 encoding it takes 4 bytes (\xf0\x9f\x98\x8a).
# Strings (str) = for working with text (human-readable).
# Bytes (bytes) = for working with raw data (files, images, network packets).
# Encoding = convert text → bytes.
# Decoding = convert bytes → text.

# position
a = "Hello, World!"
print(a[1])

# Loop (repeats a block of code multiple times,until a condition is no longer true.)
# 1. for (iterate over sequece, go through one by one)
for x in "banana":
  print(x)
  
#2. while ( repeat as long as condition is true)
count = 1          # 1️⃣ initialization
while count <= 3:  # 2️⃣ condition check
    print("Count:", count)  
    count += 1     # 3️⃣ update step
    
# 3. special loop
# 3.1 break → stop the loop immediately
for i in range(5):
    if i == 3:
        break
    print(i)   # prints 0,1,2

# 3,2 continue→ skip the current iteration, go to the next.
for i in range(5):
    if i == 2:
        continue
    print(i)   # prints 0,1,3,4

# 3.3 else with loop → runs if the loop finishes normally (not broken).
for i in range(3):
    print(i)
else:
    print("Loop finished!") 
    
# Check string (check "free" is present in the text or not)
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

# slicing
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[-5:-2])

# upper case
a = "Hello, World!"
print(a.upper())

# remove whitespace
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# replace string
# The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

# split string
# The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']