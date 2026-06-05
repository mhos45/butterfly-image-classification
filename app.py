import pickle
import numpy as np
import os
from flask import Flask, render_template, request
from tensorflow import keras
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.efficientnet import preprocess_input as eff_preprocess
from tensorflow.keras.applications.resnet_v2 import preprocess_input as res_preprocess
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input as mob_preprocess
from tensorflow.keras.applications.densenet import preprocess_input as den_preprocess
from tensorflow.keras.applications.inception_v3 import preprocess_input as inc_preprocess

app = Flask(__name__, template_folder="template")

with open("model/butterfly.pkl", "rb") as f:
    meta = pickle.load(f)

CLASS_NAMES   = meta["class_names"]
IMG_SIZE      = meta["img_size"]
PREPROCESS_KEY = meta["preprocess_key"]

PREPROCESS_FN_MAP = {
    "efficientnet":  eff_preprocess,
    "resnet_v2":     res_preprocess,
    "mobilenet_v3":  mob_preprocess,
    "densenet":      den_preprocess,
    "inception_v3":  inc_preprocess,
}
preprocess_fn = PREPROCESS_FN_MAP[PREPROCESS_KEY]

model = keras.models.load_model("model/butterfly.keras")

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files or request.files["image"].filename == "":
        return render_template("index.html", predicted_text="Please upload an image first!")

    file = request.files["image"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    img = load_img(filepath, target_size=(IMG_SIZE, IMG_SIZE))
    arr = img_to_array(img)
    arr = preprocess_fn(arr)
    arr = np.expand_dims(arr, axis=0)

    # Predict
    probs      = model.predict(arr)[0]
    pred_idx   = int(np.argmax(probs))
    pred_class = CLASS_NAMES[pred_idx]
    confidence = float(probs[pred_idx]) * 100

    result_text = f"🦋 Predicted: {pred_class}  ({confidence:.1f}% confidence)"
    return render_template("index.html",
                           predicted_text=result_text,
                           uploaded_image=filepath)


if __name__ == "__main__":
    app.run(debug=True)
