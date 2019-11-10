import sys

infile = open('wrestler2.txt', 'r')

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


# create wrestler nodes and assign alignment to first
start_vertex = None
for wrestler in range(n):
  wrestler_name = infile.readline().strip()
  if wrestler == 0:
    p1 = Wrestler(wrestler_name, 'babyface')
    start_vertex = wrestler_name
  else:
    p1 = Wrestler(wrestler_name, 'none')
  #add wrestler to dictionary
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

print('\nNodes & their Rivals:')
print('------------------')
for vertex in graph:
  print(graph[vertex].get_name(), graph[vertex].get_rival())



def BFS_Search(graph, n, start_vertex):
  # visited vertices
  visited = []

  # create a queue
  queue = []

  # starting node
  print('\n------------------')
  print('Start Node: ', start_vertex)
  print('Team: ', graph[start_vertex].get_team())

  #enque neighbors of start vertex
  for i in graph[start_vertex].get_rival():
    queue.append(i)
  visited.append(graph[start_vertex].get_name())
  print('Visited: ', visited)
  print('Queue: ', queue)
  print()

  previous_node = start_vertex


  while len(queue) is not 0:
    # remove node from queue
    node = queue.pop()
    print('\n------------------')
    print('Next Node :', node)

    # assign team to node
    if graph[previous_node].get_team() == 'babyface':
      graph[node].set_team('heel')
      print(graph[node].get_name(), ': heel team set')
    else:
      print(graph[node].get_name(), ': babyface team set')
      graph[node].set_team('babyface')

    # check if rivals are on the same team, exit
    for i in graph[node].get_rival():
      if graph[i].get_team() == graph[node].get_team():
        print('Same Teams!')
        exit('Impossible')


    visited.append(node)
    print('append visited: ', visited)
    print('Queue: ', queue)
    print()

    for i in graph[node].get_rival():
      print('Rivals: ', i)
      if i not in visited:
        if i not in queue:
          queue.append(i)
          print(i, ' added to queue')
        else:
          print(i, ' already in queue')
      else:
        print(i, ' already visited!')
      print('Queue: ', queue)
      print()

    previous_node = node


  # utility function
  total_nodes = get_all_nodes(graph, start_vertex)
  # check if any disconnected nodes identified
  if len(visited) < len(total_nodes):
    # run BFS on disconnected nodes
    # get disconnected nodes
    disconnected_nodes = set(total_nodes) - set(visited)
    print('Disconnected Nodes: ', disconnected_nodes)

    # visited tracker
    visited_2 = []

    # queue
    queue_2 = []

    starting_node = None

    # starting node
    print('\nDisconnected Nodes -------')
    for i in disconnected_nodes:
      starting_node = i

    print('Disc: ', graph[starting_node].get_name())
    graph[starting_node].set_team('babyface')
    print('Rival: ', graph[starting_node].get_team())







  return True


# utility function that returns all nodes in graph
def get_all_nodes(graph, start_vertex):
  temp_list = []
  for i in graph:
    temp_list.append(i)
  return temp_list




if BFS_Search(graph, n, start_vertex):
  print('\nYes Possible')

team_babyface = []
team_heel = []
temp_list = []

for key in graph:
  if graph[key].get_team() == 'babyface':
    team_babyface.append(graph[key].get_name())
  elif graph[key].get_team() == 'heel':
    team_heel.append(graph[key].get_name())
  else:
    temp_list.append(graph[key].get_name())

print(team_babyface)
print(team_heel)
print(temp_list)
