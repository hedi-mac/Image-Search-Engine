import numpy as np
import skimage.feature as feature

class Cooccurrence : 
       def __init__(self, n):
              self.n = n

       def calcule_cooccurrence(self, mat):
            com_mat = feature.graycomatrix(mat, [self.n], [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 6*np.pi/4, 7*np.pi/4, 8*np.pi/4], levels=256)
            diag = np.diag(com_mat[:, :, 0, 0])
            diag = np.append(diag, np.diag(com_mat[:, :, 0, 1]))
            diag = np.append(diag, np.diag(com_mat[:, :, 0, 2]))
            diag = np.append(diag, np.diag(com_mat[:, :, 0, 3]))
            diag = np.append(diag, np.diag(com_mat[:, :, 0, 4]))
            diag = np.append(diag, np.diag(com_mat[:, :, 0, 5]))
            diag = np.append(diag, np.diag(com_mat[:, :, 0, 6]))
            diag = np.append(diag, np.diag(com_mat[:, :, 0, 7]))
            diag = np.append(diag, np.diag(com_mat[:, :, 0, 8]))
            return diag




