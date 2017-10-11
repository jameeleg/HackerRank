import collections

def ransom_note(magazine, ransom):
    map_r = collections.defaultdict(int)
    for i in ransom:
        map_r[i] += 1
        
    for i in magazine:
        if map_r.get(i):
            map_r[i] -= 1

    return not any(map_r.values())
        
    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    
