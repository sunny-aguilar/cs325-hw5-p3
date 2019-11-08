import sys

#infile = open(sys.argv[1], 'r')
infile = open('wrestler4.txt', 'r')

lineup = {}           # dictionary to hold wrestlers

# get total wrestlers
n = int(infile.readline().strip())
print('# of wrestlers: ', n)


for wrestler in range(n):
  wrestler_name = infile.readline().strip()
  if wrestler == 0:
    lineup[wrestler_name] = 'babyface'
  else:
    lineup[wrestler_name] = 'none'


print(lineup)


# get number of rivalries
rivalries = infile.readline().strip()
print('# of rivalries: ', rivalries)


for i in range(n-1):
  line = infile.readline().strip()
  rivalry = [str(i) for i in line.split()]
  print(rivalry)

  r1 = rivalry[0]
  r2 = rivalry[1]


  if (lineup[r1] == 'none' and lineup[r2] == 'none'):
    lineup[r1], lineup[r2] = 'babyface', 'heel'
    continue

  if (lineup[r1] == 'none' and lineup[r2] != 'none'):
    if lineup[r2] == 'heel':
      lineup[r1] == 'babyface'
    else:
      lineup[r1] = 'heel'
    # lineup[r1] = 'babyface' if lineup[r2] == 'heel' else 'heel'
    continue

  if (lineup[r2] == 'none' and lineup[r1] != 'none'):
    # if lineup[r1] == 'babyface':
    #   lineup[r2] == 'heel'
    # else:
    #   lineup[r1] = 'babyface'
    lineup[r2] = 'heel' if lineup[r1] == 'babyface' else 'babyface'
    continue

  if (lineup[r1] == 'babyface' and lineup[r2] == 'none'):
    lineup[r2] = 'heel'
    continue

  if (lineup[r1] == 'heel' and lineup[r2] == 'none'):
    lineup[r2] = 'babyface'
    continue

  if (lineup[r1] == 'babyface' and lineup[r2] == 'babyface'):
    exit('Impossible')

  if (lineup[r1] == 'heel' and lineup[r2] == 'heel'):
    exit('Impossible')

print(lineup)
team_babyface = []
team_heel = []

for wrestler in lineup:
  if lineup[wrestler] == 'babyface':
    team_babyface.append(wrestler)
  else:
    team_heel.append(wrestler)

print('Yes possible')
print('Babyfaces: ', end=" ")
print(*team_babyface, sep=' ')
print('\nHeels: ', end=" ")
print(*team_heel, sep=' ')

