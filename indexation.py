from PIL import Image
from descripteur import Descripteur
from pathlib import Path
import numpy as np

fe = Descripteur()
for img_path in sorted(Path("./static/images_dataset").glob("*.png")):
    print(img_path)
    feature = fe.extract(img=Image.open(img_path))
    feature_path = Path("./static/images_dataset_descripteurs") / (img_path.stem + ".npy")  
    np.save(feature_path, feature)
