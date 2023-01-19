for left in range(7):
  for right in range(left,7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print()
  
teams = ['Dragons','Wolves','Pandos','Unicorns']
for home_team in teams:
      for away_team in teams:
            if home_team != away_team:
                  print(home_team + " vs " + away_team)
                  
                  
x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
print("x=" + str(x))