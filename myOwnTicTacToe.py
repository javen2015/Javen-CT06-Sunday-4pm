def initialiseBoard():
   grid=[]
   for i in range(3):
      row=[]
      for i in range(3):
         row.append(" ")
      grid.append(row)
   return(grid)

def printGrid(grid):
   userSymbol=int(input("🤫(1),🚽(2) or 🏳️‍🌈(3)?"))
   if userSymbol==1:
      symbol="🤫"
   elif userSymbol==2:
      symbol="🚽"
   else:
      symbol="🏳️‍🌈"
   cellnumber=1   
   for row in range(3):
      for cell in range(3):
         if grid[row][cell]!=" ":
            print(" | "+grid[row][cell]+ " ",end="")
         else:
            print(" | "+str(cellnumber)+" ",end="")
         cellnumber+=1
      print("\n---------------")

grid=initialiseBoard()
questions = ["Player 1(X)","Player 2(0)"]
for turn in range(9):
   userChoice = input(questions[turn%2]+"Please key in your choice.")
   printGrid(grid)