import sys

infile = open('wrestler4.txt', 'r')

class Wrestler:
  def __init__(self, name, team = 'none'):
    self.name = name
    self.team = team
    self.rival = []

  def get_name(self):
    return self.name

  def set_team(self, team):
    self.team = team

  def get_team(self):
    return self.team

  def set_rival(self, rival):
    self.rival.append(rival)

  def get_rival(self):
    return self.rival


graph = {}           # dictionary to hold wrestler objects

# get total wrestlers
n = int(infile.readline().strip())
print('# of wrestlers: ', n)


for wrestler in range(n):
  wrestler_name = infile.readline().strip()
  if wrestler == 0:
    p1 = Wrestler(wrestler_name, 'babyface')
  else:
    p1 = Wrestler(wrestler_name, 'none')

  graph[wrestler_name] = p1


# get number of rivalries
rivalries = int(infile.readline().strip())
print('# of rivalries: ', rivalries)

for i in range(rivalries):
  line = infile.readline().strip()
  rivalry = [str(i) for i in line.split()]
  print('--debugging--')
  print(rivalry)
  print('--debugging--\n')

  r1 = rivalry[0]
  r2 = rivalry[1]

  graph[r1].set_rival(r2)
  graph[r2].set_rival(r1)

for i in graph:
  print(graph[i].get_name(), graph[i].get_rival())


def BFS_Search(graph):
  # nodes
  start = graph[0]






