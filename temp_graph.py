import sys

infile = open('wrestler4.txt', 'r')

graph = {}           # dictionary to hold wrestlers

# get total wrestlers
n = int(infile.readline().strip())
print('# of wrestlers: ', n)


for i in range(n):
  wrestler_name = infile.readline().strip()
  if i == 0:
    graph[wrestler_name] = ['babyface']
  else:
    graph[wrestler_name] = ['none']

print(graph)


# get number of rivalries
rivalries = int(infile.readline().strip())
print('# of rivalries: ', rivalries)

for i in range(rivalries):
  line = infile.readline().strip()
  rivalry = [str(i) for i in line.split()]
  print(rivalry)

  r1 = rivalry[0]
  r2 = rivalry[1]
  graph[r1]

print(r1)








