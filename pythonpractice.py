# 11/10/20

import pandas as pd
import numpy as np
import yfinance as yf
import sys 
import functools as ft 
import matplotlib as mpl
import matplotlib.pyplot as plt #submodules are not always imported by default
import matplotlib.pylab
# from functools import reduce
matplotlib.pylab.show(block=False)

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


col_names = ['Symbol', 'High', 'Low']
symbols = ['ABC', 'VEEV', 'FIVN']
highs = [106, 275, 146]
lows = [103, 262, 140]
list_cols = [symbols, highs, lows]

# zipped = list(zip(col_names, list_cols))

# # print(zipped)

# data = dict(zipped)
# # print(data)

# table = pd.DataFrame(data)
# print(table)

# data = {'symbols': symbols, 'side': 'buy'}
# data = {'symbols': symbols, 'High': highs, 'Low': lows, 'side': 'buy'}
# df = pd.DataFrame(data)
# print(df)

# print('Changing index labels')
# df.index = symbols
# # df.columns = ['a', 'b', 'c', 'd']
# print(df)

# out_csv = 'stocks233.csv'
# df.to_csv(out_csv)

#not working yet
# out_xlsx = 'stocks233.xlsx'
# ew = 'C:\\Users\\sdgur\\Documents\\Projects\\Python Projects\\pythonpractice'
# df.to_excel(ew, out_xlsx)

stocks = pd.read_csv("prac.csv", index_col='Date', parse_dates=True)
# stocks = pd.read_csv("prac.csv", index_col='Date')
print(stocks)
# lowarr=stocks['Low'].values
# print(type(lowarr))
# print(plt.plot(lowarr))
# plt.show()

# 12/2/20
# Indexing with data frames  
# print(stocks.floordiv(2))
# print(stocks['High'])
# print(type(stocks['High']))
# print(stocks.iloc[:,2])
# print(stocks.loc['2020-11-13','High'])

#Fancy Indexing
stocks = stocks.set_index(['Symbol', 'High'])
print(stocks)
stocks = stocks.sort_index()
print(stocks)
# print(stocks.index.name)
# print(stocks.index.names)

