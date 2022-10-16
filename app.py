import numpy as np
from PIL import Image
from descripteur import Descripteur
from datetime import datetime
from flask import Flask, request, render_template
from pathlib import Path
from datetime import datetime

app = Flask(__name__)

fe = Descripteur()
features = []
features_coo = []
img_paths = []
for feature_path in Path("./static/images_dataset_descripteurs").glob("*.npy"):
    print(len(np.load(feature_path)))
    print()
    features.append(np.load(feature_path))
    img_paths.append(Path("./static/images_dataset") / (feature_path.stem + ".png"))
features = np.array(features)
for feature_path in Path("./static/images_dataset_descripteurs_cooccurence").glob("*.npy"):
    features_coo.append(np.load(feature_path))
features_coo = np.array(features_coo)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        option = request.form['options']
        file = request.files['query_img']
        img = Image.open(file.stream)
        uploaded_img_path = "static/images/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(uploaded_img_path)
        if option == 'option1' : 
            stTime = datetime.now()
            query = fe.extract(img)
            dists = np.linalg.norm(features-query, axis=1)
            t = datetime.now() - stTime
            tStr = f"{t}"
            time = f"{tStr[tStr.rindex(':')+1:]} "
            ids = np.argsort(dists)[:10]
            scores = [(dists[id], img_paths[id]) for id in ids]
        else : 
            stTime = datetime.now()
            query = fe.extract_coocurrence(img)
            dists = np.linalg.norm(features_coo-query, axis=1)
            t = datetime.now() - stTime
            tStr = f"{t}"
            time = f"{tStr[tStr.rindex(':')+1:]} "
            ids = np.argsort(dists)[:10]
            scores = [(dists[id], img_paths[id]) for id in ids]
        return render_template('index.html', query_path = uploaded_img_path, scores = scores, time = time)
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run()
