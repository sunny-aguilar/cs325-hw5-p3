import sys

infile = open('wrestler4.txt', 'r')

class Wrestler:
  def __init__(self, name, team = 'none', rival = 'none'):
    self.name = name
    self.team = team
    self.rival = rival

  def set_rival(self, rival):
    self.rival = rival

  def get_rival(self):
    return self.rival

  def set_team(self):
    self.team = team

  def get_team(self):
    return self.team

player = Wrestler('Sunny', 'Babyface', 'none')
print(player.get_rival())