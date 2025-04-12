def initialiseBoard():
     grid=[]
     row=[]
     for i in range(3):
        row.append(" ")
     for i in range(3):
      grid.append(row)
     return(grid)