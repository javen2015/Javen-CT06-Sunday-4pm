cellnumber=1
def initialiseBoard():
   grid=[]
   row=[]
   for i in range(3):
      for i in range(3):
         row=[]
         row.append(" ")
         grid.append(row)
   return(grid)
grid=initialiseBoard()
def printGrid(userAnswer):
   for i in range(3):
      for i in range(3):
         if grid[userAnswer]==" ":
            print(" | X ",end="")
         cellnumber+=1
         print("\n---------------")