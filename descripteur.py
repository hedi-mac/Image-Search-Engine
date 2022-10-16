from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
from PIL import Image
import numpy as np
from correlogramme import Correlogramme
from cooccurrence import Cooccurrence

class Descripteur:

    DIST = 1

    def extract(self, img):
        img = img.resize((100, 100))
        img = np.asarray(img.convert('RGB'))
        print(img)
        print()
        mat_blue = img[:, :, 0]
        calc_corr = Correlogramme(self.DIST)
        corr_blue = calc_corr.calcule_correlogramme(mat_blue)
        res = np.diag(corr_blue)
        #print(res)
        #print()
        mat_green = img[:, :, 1]
        corr_green = calc_corr.calcule_correlogramme(mat_green)
        res = np.append(res, np.diag(corr_green))
        mat_red = img[:, :, 2]
        corr_red = calc_corr.calcule_correlogramme(mat_red)
        return np.append(res, np.diag(corr_red))

    def extract_coocurrence(self, img):
        img = img.resize((100, 100))
        img = np.asarray(img.convert('RGB'))
        print(img)
        print()
        mat_blue = img[:, :, 0]
        calc_co = Cooccurrence(self.DIST)
        co_blue = calc_co.calcule_cooccurrence(mat_blue)
        res = co_blue
        mat_green = img[:, :, 1]
        co_green = calc_co.calcule_cooccurrence(mat_green)
        res = np.append(res, co_green)
        mat_red = img[:, :, 2]
        co_red = calc_co.calcule_cooccurrence(mat_red)
        return np.append(res, co_red)

