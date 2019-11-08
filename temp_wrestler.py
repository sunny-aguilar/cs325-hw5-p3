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

  def get_rival(self, n):
    return self.rival[n]


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
print()

# get number of rivalries
rivalries = int(infile.readline().strip())
print('# of rivalries: ', rivalries)

for i in range(rivalries):
  line = infile.readline().strip()
  rivalry = [str(i) for i in line.split()]
  print(rivalry)

  r1 = rivalry[0]
  r2 = rivalry[1]

  graph[r1].set_rival(r2)
  graph[r2].set_rival(r1)

print(graph['Alice'].get_rival(0))
print(graph['Bob'].get_rival(0))







