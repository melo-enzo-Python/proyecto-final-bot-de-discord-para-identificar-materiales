from keras.models import load_model  
from PIL import Image, ImageOps  
import numpy as np

def identificador(imagen):

    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("./keras_model.h5", compile=False)

    # Load the labels
    class_names = open("./labels.txt", "r").readlines()

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(imagen).convert("RGB")

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    if index == 0: 
        return ("Beaker: Recipiente cilíndrico para mezclar o calentar líquidos; no usar para mediciones precisas ni calentar sustancias corrosivas sin protección.")
    if index == 1: 
        return ("Erlenmeyer Flask: Recipiente cónico para mezclar líquidos sin derrames; nunca lo selles al calentar ni lo tomes sin protección térmica.")
    if index== 2: 
        return ("Graduated Cylinder: Tubo graduado para medir volúmenes con precisión; colócalo sobre superficie nivelada y no lo uses para calentar.")
    if index == 3: 
        return ("Test Tube: Tubo pequeño para reacciones químicas; apunta lejos al calentar y manipula con pinzas si está caliente.")
    if index == 4: 
        return ("Pipette: Instrumento delgado para transferir pequeñas cantidades de líquido; no succionar con la boca y usar con perilla.")
    if index == 5: 
        return ("Petri Dish: Placa para cultivos microbiológicos; manipular con guantes y desechar el contenido de forma segura.")
    if index == 6: 
        return ("Spatula: Herramienta para transferir sólidos químicos; evitar contacto con sustancias corrosivas y mantener limpia.")
    elif index == 7: 
        return ("Bunsen Burner: Fuente de llama para calentar sustancias; mantener lejos de inflamables, usar gafas y apagar tras usar.")
   


