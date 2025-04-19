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
def getPlayerMove(grid):
   # questions = ["Player 1(X)","Player 2(O)"]
   while True:
      userChoice = int(input("Player 1 please key in your choice."))
      if (userChoice.isdigit()==False or int(userChoice)<1 or int(userChoice)>9):
         print("Please key in a valid number.")
      else:
         index=userChoice-1
         row=index//3
         col=index%3
         if(grid[row][col]==" "):
            grid[row][col] = "X"
            break
         else:
            print("Please key i your choice again as this spot is taken.")
   printGrid(grid)
checkWin()

grid=initialiseBoard()
while True:
   printGrid(grid)
   getPlayerMove(grid)