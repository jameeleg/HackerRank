import collections
import math

def number_needed(a, b):
    map_letters = collections.defaultdict(int)
    
    for l in a:
        map_letters[l] = map_letters[l] +1
        
    for l in b:
        map_letters[l] = map_letters[l] -1
    sum = 0
    for v in map_letters.itervalues():
        sum += int(math.fabs(v))
    
    return sum
        
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)