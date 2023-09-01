import re
import csv
import os
import sys
path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)
file_name = 'inglesss.txt'

# ingles_file = open('inglesss.txt', 'r')
# lines = [line for line in ingles_file]
# print(lines[0])

# with open('inglesss.txt', 'r', newline='') as f:
#     lines = f.readlines()
#     print(lines[0])
#     for line in lines:
#         print(line)

# CSV Approach
file = open(file_name, 'r', newline='')
reader = csv.reader(file)

header = next(reader)  # The first line is the header
data = [row for row in reader]
print('HEADER', data[0])
print('-'*50)
Aprobados = 0
Reprobados = 0
for i in range(4, len(data)):
    print('+'*80)
    line_data = str(data[i]).strip('[]').strip("'").strip(' ').split(',')[0]
    # This RegEx remove extra spaces
    line_data = re.sub(r'\s{2,}', ' ', line_data)
    line_data = line_data.split(' ')
    print(line_data)
    for line in line_data:
        print(line)
        if "Aprobado" in line:
            Aprobados += 1
        elif "Reprobado" in line:
            Reprobados += 1
print('-'*80)
print('Aprobados: ', Aprobados, ' '*20, '|')
print('Reprobados: ', Reprobados, ' '*19, '|')
print('-'*80)
