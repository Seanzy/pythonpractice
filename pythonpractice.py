# 11/10/20

import pandas as pd
import numpy as np
import yfinance as yf
import sys 
import functools as ft 
# from functools import reduce

# Simple letter removal kata is not so simple. 
# Let's remember to define precisely what we want this program to do:
# We want to replace every occurrence of every letter in the alphabet with '' up to k letters in the given string. So first replace every 'a' while k > 0, if there are no more 'a's to replace, then start replacing 'b's until k reaches 0, etc. So while k > 0, check the string for the current letter and replace it, each time subtracting 1 from k until there are no more of that letter remaining, and then if k is still > 0, move to the next letter, continuing this until k reaches zero or until there are no letters remaining in the string. 
# Wait a second, 'abracadabra' has 11 letters in it. If k => 11, then does that mean every letter will be replaced? Yes. Because if k is 11, then all 5 a's wll be replaced, all 2 b's, 1 c, 1 d, 2 r's = 11 letters. 
# Whoa wait a second, what if k were 10? Then which letters would remain? 1 letter would remain, and it would be the letter closest to the end of the alphabet, in this case, the letter r, so if k == 10, then output == 'r', but this isn't exactly a shortcut unless k is close to the len of the str. 

# I am having trouble with the string because they are immutable, so I need to convert it into a list of letters. 

# def solve(st,k): 
#   if k >= len(st): 
#     print('')

#   new_st = st    
#   letter = chr(97)

#   while k > 0: 
#     if st.count(letter):
#       new_st = new_st.replace(letter, '', 1)
#       k -= 1
#     else:
#       letter = ord(letter) + 1

#   print(new_st)

# solve('abracadabra', 1)
#  # = 'bracadabra' # remove the leftmost 'a'.
# solve('abracadabra', 2)
#  # = 'brcadabra'  # remove 2 'a' from the left.
# solve('abracadabra', 6)
# #  # = 'rcdbr'      # remove 5 'a', remove 1 'b' 
# solve('abracadabra', 8)
# #  # = 'rdr'
# solve('abracadabra',50)
 # = ''


# what if I used nested functions for this kata? I need a function to remove the current letter, a, b, or c etc, but I also need a function to check the word for the given letter and subtract 1 from k if a letter is removed. THe inner function can take a letter to be removed as input. 

# prac = lambda x,y : x**y

# print(prac(2,3))

# nums = [1, 2, 3, 4]

# double = map(lambda num: num*2, nums)

# print(list(double))

# names = ['sean', 'joe', 'john']
# doublenames = filter(lambda str: len(str)<4, names)
# ldoublenames = list(doublenames)
# print(ldoublenames)

# lis = [1,2,3,4,5,6]
# print ("The maximum element of the list is : ",end="") 
# print (ft.reduce(lambda a,b : a if a > b else b,lis)) 

# f = lambda x,y: x * y

# print(f(3,3))


# class Dog:    
#     def woof(self):
#         return 'woof!'

# t = Dog()
# print(t.woof())


# class Planet():
#     def __init__(self, name):
#         self.name = name
        
# m = Planet('mercury')

# m.name

# s = "animal-horse"

# print(s.split("-"))

# d = {
#     'apple': 1,
#     'banana': 2,
#     'coconut': 3
# }

# d['durian'] = 4

# print(d)

# def add_many(*args):
#     s = 0
#     for n in args:
#         s += n
#     print(s)

# print(add_many(100, 50, 3))


# book = {
#     'title': 'The Giver',
#     'author': 'Lois Lowry',
#     'rating': 4.13,
#     'format': 'paperback'
# }

# del book['format']

# print(book)


print([i for i in range(5) i >=3 ])