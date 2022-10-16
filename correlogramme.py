import numpy as np

class Correlogramme : 
       def __init__(self, n):
              self.n = n

       def calcule_correlogramme(self, mat):
              #print("\nLe maximum est : {}".format(mat.max()))
              corr = np.zeros((256, 256))
              for i in range(self.n, len(mat)-self.n):
                 for j in range(self.n, len(mat[0])-self.n):
                    res = ""
                    for k in range(i-self.n, i+self.n+1):
                       for r in range(j-self.n, j+self.n+1):
                          if k==i and r ==j :
                             res = res+"    "
                          else :          
                             #res = res+" {}".format(mat[k][r])
                             corr[mat[i][j], mat[k][r]] = corr[mat[i][j], mat[k][r]] + 1
                       #res = res + "\n"
                    #print(res)
              print()
              #print(corr)
              return corr




