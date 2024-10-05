#!/usr/bin/python3
"""
0-main
"""

def pascal_triangle(n):
 if (n <= 0):
  return []
 
 triangle =[[1]] #first row is always 1 

 for i in range(1,n) :
  
  row = [1] # start each row with 1 
  perv_row = triangle[i-1]

  for j in range(1,i):
   row.append(perv_row[j-1]+perv_row[j])

  row.append(1)
  triangle.append(row)

 return triangle
