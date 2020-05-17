import timeit
from histogram import histogram
import sys 

poem = open('poem.txt', 'r')
poem_lines = poem.read().lower()
poem_words = poem_lines.split()


code_to_test = """
a = range(100000)
b = []
for i in a:
    b.append(i*2)
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100


histogram_to_test = """
histogram(poem_words)
"""
histogram_time = timeit.timeit(histogram_to_test, number = 100)/100

print(elapsed_time)
print(histogram_time)