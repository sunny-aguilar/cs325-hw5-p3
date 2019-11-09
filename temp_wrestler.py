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


# create wrestler nodes and assign alignment
start_vertex = None
for wrestler in range(n):
  wrestler_name = infile.readline().strip()
  if wrestler == 0:
    p1 = Wrestler(wrestler_name, 'babyface')
    start_vertex = wrestler_name
  else:
    p1 = Wrestler(wrestler_name, 'none')

  graph[wrestler_name] = p1


# get number of rivalries
rivalries = int(infile.readline().strip())
print('# of rivalries: ', rivalries)

for i in range(rivalries):
  line = infile.readline().strip()
  rivalry = [str(i) for i in line.split()]
  # print('--rivalry list--')
  # print(rivalry)

  r1 = rivalry[0]
  r2 = rivalry[1]

  graph[r1].set_rival(r2)
  graph[r2].set_rival(r1)

for vertex in graph:
  print(graph[vertex].get_name(), graph[vertex].get_rival())


def BFS_Search(graph, n, start_vertex):
  # visited vertices
  visited = [0 for x in range(n)]

  # create a queue
  queue = []

  #enque neighbors of start vertex
  for i in graph[start_vertex].get_rival():
    queue.append(i)
    visited[0] = graph[start_vertex].get_name()
  print('Rivals Queue: ', queue[0])
  print('Visited: ', visited)
  print('Team: ', graph[start_vertex].get_team())

  while len(queue) is not 0:
    # remove node from queue
    node = queue.pop()
    print('Node :', node)
    # check rival teams, exit if the same
    for i in graph[node].get_rival():
      print('Rival Name: ', graph[i].get_name())
      if graph[i].get_team == graph[node].get_team:
        print('Same teams!')
        exit('Impossible')

    if 
    graph[node].set_team('')

  # nodes
  # if graph[start_vertex].get_team() is 'babyface':
  #   print('Babyface found!')





BFS_Search(graph, n, start_vertex)



