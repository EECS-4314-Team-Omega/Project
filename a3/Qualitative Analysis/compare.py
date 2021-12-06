
  
with open('gcc.txt') as file_3, open('include.txt') as file_2, open('understand.txt') as file_1, open('diff_understand.txt', 'w') as output:
    lines_2 = file_2.readlines()
    lines_3 = file_3.readlines()
    for i in range(len(lines_2)):
        lines_2[i] = lines_2[i].replace('\n','')
    for i in range(len(lines_3)):
        lines_3[i] = lines_3[i].replace('\n','')
  
    for line in file_1.readlines():
        line = line.replace('\n','')
        if line not in lines_3 and line not in lines_2:
            output.write( line + '\n')
  
with open('understand.txt') as file_3, open('include.txt') as file_2, open('gcc.txt') as file_1, open('diff_gcc.txt', 'w') as output:
    lines_2 = file_2.readlines()
    lines_3 = file_3.readlines()
    for i in range(len(lines_2)):
        lines_2[i] = lines_2[i].replace('\n','')
    for i in range(len(lines_3)):
        lines_3[i] = lines_3[i].replace('\n','')
  
    for line in file_1.readlines():
        line = line.replace('\n','')
        if line not in lines_3 and line not in lines_2:
            output.write(line + '\n')


with open('understand.txt') as file_3, open('gcc.txt') as file_2, open('include.txt') as file_1, open('diff_include.txt', 'w') as output:
    lines_2 = file_2.readlines()
    lines_3 = file_3.readlines()
    for i in range(len(lines_2)):
        lines_2[i] = lines_2[i].replace('\n','')
    for i in range(len(lines_3)):
        lines_3[i] = lines_3[i].replace('\n','')
  
    for line in file_1.readlines():
        line = line.replace('\n','')
        if line not in lines_3 and line not in lines_2:
            output.write(line + '\n')
