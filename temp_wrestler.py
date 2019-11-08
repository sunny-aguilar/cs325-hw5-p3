import sys

infile = open('wrestler4.txt', 'r')

class Wrestler:
  def __init__(self, name, team = 'none', rival = 'none'):
    self.name = name
    self.team = team
    self.rival = rival

  def get_name(self):
    return self.name

  def set_rival(self, rival):
    self.rival = rival

  def get_rival(self):
    return self.rival

  def set_team(self, team):
    self.team = team

  def get_team(self):
    return self.team


lineup = {}           # dictionary to hold wrestler objects

# get total wrestlers
n = int(infile.readline().strip())
print('# of wrestlers: ', n)


for wrestler in range(n):
  wrestler_name = infile.readline().strip()
  if wrestler == 0:
    p1 = Wrestler(wrestler_name, 'babyface')
  else:
    p1 = Wrestler(wrestler_name, 'none')

  lineup[wrestler_name] = p1








