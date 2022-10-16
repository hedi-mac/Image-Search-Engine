from PIL import Image
from pathlib import Path
import os.path


for img_path in sorted(Path("D:\monDossier\ING\ING320212022\s1\projets\indexation\moteurDeRecherche\moteur_recherche\jpg").glob("*.jpg")):
        print(img_path)
        (name, extension) = os.path.splitext(img_path)
        image = Image.open(img_path)
        image.save(name+"_thumb.png")
