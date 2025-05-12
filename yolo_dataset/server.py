from flask import Flask, request, jsonify
from PIL import Image, ImageOps, ImageChops
from flask_cors import CORS
import numpy as np
import joblib
import json

# model
model = joblib.load("symbol_classifier.joblib")

# label
with open("symbols_new.json", "r") as f:
    symbol_data = json.load(f)

labels = [item["label"] for item in symbol_data]

# Margin Crop Function
def crop_to_content(img):
    bg = Image.new(img.mode, img.size, 255)  
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    return img.crop(bbox) if bbox else img

app = Flask(__name__)
CORS(app) 

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    img = Image.open(file).convert("L")            
    img = ImageOps.autocontrast(img)               
    img = crop_to_content(img)                     
    img = img.resize((64, 64))                     
    img_arr = np.array(img).flatten().reshape(1, -1)

    prediction = model.predict(img_arr)[0]
    label = prediction  # Because we already learned y = label

    return jsonify({"label": label})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)


