def initialiseBoard():
   grid=[]
   row=[]
   for i in range(3):
      row.append(" ")
   for i in range(3):
      grid.append(row)
      grid.append("\n")
   return(grid)
grid=initialiseBoard()
print(grid)