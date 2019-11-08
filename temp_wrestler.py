import sys

infile = open('wrestler4.txt', 'r')

class Wrestler:
  def __init__(self, name, team = 'none', rival = 'none'):
    self.name = name
    self.team = team
    self.rival = rival

  def set_rival(self, rival):
    self.rival = rival

player = Wrestler('Wendy', 'heel')

print(player.name)

player.set_rival('Babyface')


