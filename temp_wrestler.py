import sys

infile = open('wrestler1.txt', 'r')

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

  # append rival to wrestler
  graph[r1].set_rival(r2)
  graph[r2].set_rival(r1)

for vertex in graph:
  print(graph[vertex].get_name(), graph[vertex].get_rival())



def BFS_Search(graph, n, start_vertex):
  # visited vertices
  visited = []

  # create a queue
  queue = []

  #enque neighbors of start vertex
  for i in graph[start_vertex].get_rival():
    queue.append(i)
  visited.append(graph[start_vertex].get_name())
  print('\n------------------')
  print('Initial Rival Queue: ', queue[0])
  print('Visited: ', visited)
  print('Team: ', graph[start_vertex].get_team())
  print('Queue: ', queue)
  print()

  previous_node = start_vertex


  while len(queue) is not 0:
    # remove node from queue
    node = queue.pop()
    print('\n------------------')
    print('Next Node :', node)

    # check rival teams, exit if the same
    # for i in graph[node].get_rival():
    #   print('Rival Name: ', graph[i].get_name())
    #   if graph[i].get_team == graph[node].get_team:
    #     print('Same teams!')
    #     exit('Impossible')
    if graph[previous_node].get_team() == graph[node].get_team:
      print('Same Teams!')
      exit('Impossible')


    if graph[previous_node].get_team() == 'babyface':
      graph[node].set_team('heel')
      print(graph[node].get_name(), ': heel team set')
    else:
      print(graph[node].get_name(), ': babyface team set')
      graph[node].set_team('babyface')

    visited.append(node)
    print('append visited: ', visited)
    print()

    for i in graph[node].get_rival():
      print('Rivals: ', i)
      if i not in visited:
        queue.append(i)
        print(i, ' not in queue')
      else:
        print('Rival ', i, ' already visited')
      print()

      previous_node = node

  return True



if BFS_Search(graph, n, start_vertex):
  print('\nYes Possible')

team_babyface = []
team_heel = []

for key in graph:
  if graph[key].get_team() == 'babyface':
    team_babyface.append(graph[key].get_name())
  else:
    team_heel.append(graph[key].get_name())

print(team_babyface)
print(team_heel)
