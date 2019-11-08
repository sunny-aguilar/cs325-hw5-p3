import sys

infile = open('wrestler4.txt', 'r')

graph = {}           # dictionary to hold wrestlers

# get total wrestlers
n = int(infile.readline().strip())
print('# of wrestlers: ', n)


for wrestler in range(n):
  wrestler_name = infile.readline().strip()
  if wrestler == 0:
    lineup[wrestler_name] = 'babyface'
  else:
    lineup[wrestler_name] = 'none'










