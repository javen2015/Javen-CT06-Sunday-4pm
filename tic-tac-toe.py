def initialiseBoard():
   grid=[]
   row=[]
   for i in range(3):
      row=[]
      row.append(" ")
   grid.append(row)
   print("%p"%row)
   return(grid)
