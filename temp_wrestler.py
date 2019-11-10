import sys

# open file
infile = open('wrestler2.txt', 'r')

# create a class that will be used to create nodes for each wrestler
class Wrestler:
  # data variables for the class
  def __init__(self, name, team = 'none'):
    self.name = name
    self.team = team
    self.rival = []

  # get name of wrestler
  def get_name(self):
    return self.name

  # set team of wrestler
  def set_team(self, team):
    self.team = team

  # get team of wrestler
  def get_team(self):
    return self.team

  # set wrestler's rival
  def set_rival(self, rival):
    self.rival.append(rival)

  # get wrestler's rivals
  def get_rival(self):
    return self.rival


# main()
# receives:         none
# returns:          none
# preconditions:    none
# description:      runs the main program calling various functions
#                   to designate wrestlers as babyfaces and heels and
#                   provide the solution using the BFS algorithm.
def main():
  # dictionary to hold wrestler objects
  graph = {}

  # get total wrestlers
  n = int(infile.readline().strip())

  # set a starting vertex
  start_vertex = None

  # create wrestler nodes and assign alignment to first
  for wrestler in range(n):
    wrestler_name = infile.readline().strip()
    if wrestler == 0:
      # assign the wrestler as a babyface
      p1 = Wrestler(wrestler_name, 'babyface')
      # assignt eh wrestler as the starting vertex
      start_vertex = wrestler_name
    else:
      # assign all other wrestlers team as undefined
      p1 = Wrestler(wrestler_name, 'none')
    #add wrestlers to dictionary
    graph[wrestler_name] = p1

  # get number of rivalries from file
  rivalries = int(infile.readline().strip())

  # assign rivals of each wrestler
  for i in range(rivalries):
    line = infile.readline().strip()
    rivalry = [str(i) for i in line.split()]

    r1 = rivalry[0]
    r2 = rivalry[1]

    # append rival to wrestler
    graph[r1].set_rival(r2)
    graph[r2].set_rival(r1)


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

  print('Babyfaces: ', *team_babyface, end=" ")
  print()
  print('Heels: ', *team_heel, end=" ")


# BFS_Search()
# receives:         a graph dictionary, n, starting vertex
# returns:          boolean
# preconditions:    graph must be popultated, n must be an integer,
#                   and starting vertex must be assigned
# description:      this function performs BFS to traverse a graph in
#                   order to designate wrestlers and babyfaces and
#                   heels. If any rivalries are between wrestlers on
#                   the same team, then it is not possible to perform
#                   such a designation and the function returns false.
#                   If the designations are possible, then true is
#                   return.
def BFS_Search(graph, n, start_vertex):
  # visited vertices
  visited = []

  # create a queue
  queue = []

  # starting node

  #enque neighbors of start vertex
  for i in graph[start_vertex].get_rival():
    queue.append(i)
  visited.append(graph[start_vertex].get_name())

  previous_node = start_vertex


  while len(queue) is not 0:
    # remove node from queue
    node = queue.pop()

    # assign team to node
    if graph[previous_node].get_team() == 'babyface':
      graph[node].set_team('heel')
    else:
      graph[node].set_team('babyface')

    # check if rivals are on the same team, exit
    for i in graph[node].get_rival():
      if graph[i].get_team() == graph[node].get_team():
        exit('Impossible')

    visited.append(node)

    for i in graph[node].get_rival():
      if i not in visited:
        if i not in queue:
          queue.append(i)

    previous_node = node


    total_nodes = get_all_nodes(graph, start_vertex)
    disconnected_nodes = set(total_nodes) - set(visited)
    # add disconnected nodes
    # starting node

    for i in disconnected_nodes:
      starting_node = i

    if len(queue) == 0 and i not in visited:
      # pluck node from disjoint set
      graph[i].set_team('babyface')
      previous_node = graph[i].get_name()
      queue.append(starting_node)

  # return true if possible to designate babyfaces and heels
  return True


# utility function that returns all nodes in graph
def get_all_nodes(graph, start_vertex):
  temp_list = []
  for i in graph:
    temp_list.append(i)
  return temp_list



# call main program
main()
