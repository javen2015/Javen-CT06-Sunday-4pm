def initialiseBoard():
   grid=[]
   row=[]
   for i in range(3):
      row=[]
      row.append(" ")
      grid.append(row)
   return(grid)
grid=initialiseBoard()
print(grid)