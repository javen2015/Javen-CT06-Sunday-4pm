def initialiseBoard():
   grid=[]
   for i in range(3):
      row=[]
      for i in range(3):
         row.append(" ")
      grid.append(row)
   return(grid)

def printGrid(grid):
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
questions = ["Player 1(X)","Player 2(O)"]
for turn in range(9):
   userChoice = int(input(questions[turn%2]+"Please key in your choice."))
   index=userChoice-1
   row=index//3
   col=index%3
   grid[row][col] = "X"
   printGrid(grid)