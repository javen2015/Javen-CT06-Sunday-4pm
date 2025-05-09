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
def getPlayerMove(grid,current_player):
   questions = ["Player 1(X)","Player 2(O)"]
   while True:
      userChoice = input("Player "+current_player+" please key in your choice.")
      if (userChoice.isdigit()==False or int(userChoice)<1 or int(userChoice)>9):
         print("Please key in a valid number.")
      else:
         index=int(userChoice)-1
         row=index//3
         col=index%3
         if(grid[row][col]==" "):
            grid[row][col] = current_player
            break
         else:
            print("Please key in your choice again as this spot is taken.")

def checkWin(grid):
   winningConditions=[[grid[0][0],grid[0][1],grid[0][2]],[grid[1][0],grid[1][1],grid[1][2]],[grid[2][0],grid[2][1],grid[2][2]],[grid[0][0],grid[1][0],grid[2][0]],[grid[0][1],grid[1][1],grid[2][1]],[grid[0][2],grid[1][2],grid[2][2]],[grid[0][2],grid[1][1],grid[2][0]],[grid[0][0],grid[1][1],grid[2][2]]]
   for condition in winningConditions:
      if(condition[0]==condition[1]==condition[2]):
         if(condition[0]!=" "):
            return True       
   return False
def check_full():
   for row in range(3):
      for col in range(3):
         if(grid[row][col]==" "):
            return False
   return True


grid=initialiseBoard()
current_number=0
current_player="X"
while True:
   if current_number%2==0:
      current_player="X"
   else:
      current_player="O"
   current_number+=1
   printGrid(grid)
   getPlayerMove(grid,current_player)
   if checkWin(grid):
      print("Win")
      printGrid(grid)
      break
   if check_full():
      print("Draw")
      printGrid(grid)
      break