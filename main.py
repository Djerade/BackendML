from fastapi import FastAPI, File, UploadFile
# from ultralytics import YOLO
# import cv2
# import numpy as np
# import shutil


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



# # Charger le modèle YOLOv8 pré-entraîné
# model = YOLO("yolov8n.pt")  # 'n' pour nano (léger), sinon 's', 'm', 'l'

# @app.post("/detect")
# async d       ef detect_objects(image: UploadFile = File(...)):
#     # Sauvegarder temporairement l'image
#     image_path = f"temp_{image.filename}"
#     with open(image_path, "wb") as buffer:
#         shutil.copyfileobj(image.file, buffer)

#     # Lire l'image avec OpenCV
#     img = cv2.imread(image_path)

#     # Détection d'objets avec YOLO
#     results = model(img)[0]  # On récupère uniquement le premier résultat

#     # Convertir les résultats en format JSON
#     detections = []
#     for box in results.boxes:
#         detections.append({
#             "class": int(box.cls),
#             "confidence": float(box.conf),
#             "bbox": [float(coord) for coord in box.xyxy[0]]
#         })

#     return {"objects": detections}
