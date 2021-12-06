import random

randomlist = []

with open('diff_gcc.txt') as diff:
    lines= diff.readlines();
    randomlist = random.sample(lines, 282)
    
with open('discrepancies.txt', 'w') as output:
    for line in randomlist:
        output.write('G ' + line)

with open('diff_include.txt') as diff:
    lines= diff.readlines();
    randomlist = random.sample(lines, 4)

with open('discrepancies.txt', 'a') as output:
    for line in randomlist:
        output.write('I ' + line)

with open('diff_understand.txt') as diff:
    lines= diff.readlines();
    randomlist = random.sample(lines, 96)

with open('discrepancies.txt', 'a') as output:
    for line in randomlist:
        output.write('U ' + line)