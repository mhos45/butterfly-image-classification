<div align="center">

# 🦋 Butterfly Image Classification

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=A855F7&center=true&vCenter=true&width=600&lines=Deep+Learning+%7C+Transfer+Learning;5+CNN+Models+Compared;Flask+Web+App+Deployment" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)

<br/>

> **Upload a butterfly photo → Get the species name + confidence instantly.**
> Built with 5 pretrained CNN models, fine-tuned on real butterfly data, and deployed as a Flask web app.

</div>

---

## 📸 App Preview

<div align="center">

| Upload Screen | Prediction Result |
|:---:|:---:|
| 📷 Drag & drop any butterfly image | 🦋 **DANAID EGGFLY** — 86.3% confidence |

</div>

---

## 🗂️ Project Structure

```
🦋 butterfly_app/
│
├── 📓 butterfly-image-classification.ipynb   ← Training notebook (run on Kaggle)
├── 🐍 app.py                                 ← Flask web server
│
├── 📁 template/
│   └── 🌐 index.html                         ← Web UI (drag & drop, preview, result)
│
├── 📁 model/
│   ├── 🧠 butterfly.keras                    ← Best trained model
│   └── 🗃️  butterfly.pkl                     ← Class names + metadata
│
└── 📁 static/
    └── 📁 uploads/                           ← Temporarily stores uploaded images
```

---

## 🧠 Models Trained & Compared

Five state-of-the-art CNN architectures were trained using a **two-phase transfer learning** strategy and compared head-to-head on validation accuracy:

<div align="center">

| # | Model | Input Size | Fine-tuned Layers | Strength |
|:---:|:---|:---:|:---:|:---|
| 1 | ⚡ EfficientNetB3 | 224 × 224 | Top 40 | Best accuracy / efficiency balance |
| 2 | 🔷 ResNet50V2 | 224 × 224 | Top 40 | Strong residual feature extraction |
| 3 | 📱 MobileNetV3Large | 224 × 224 | Top 30 | Lightweight and fast |
| 4 | 🌿 DenseNet121 | 224 × 224 | Top 50 | Dense connections, less overfitting |
| 5 | 🎯 InceptionV3 | 299 × 299 | Top 60 | Multi-scale feature extraction |

</div>

The model with the **highest validation accuracy** is automatically saved and used in the web app.

---

## 🔁 Training Strategy

```
Phase 1 — Head Training                    Phase 2 — Fine Tuning
─────────────────────────────              ──────────────────────────────
  Backbone weights → FROZEN                  Top N layers → UNFROZEN
  LR = 1e-3 (Adam)                           LR = 1e-5 (Adam)
  Train custom head only:                    Backbone adapts to butterflies
    GlobalAveragePooling2D                   EarlyStopping (patience=5)
    BatchNormalization                       ReduceLROnPlateau
    Dropout (0.4)
    Dense (512, ReLU)
    BatchNormalization
    Dropout (0.3)
    Dense (NUM_CLASSES, Softmax)
```

### 🔄 Data Augmentation Applied
```
rotation ±20°  |  width/height shift 10%  |  shear 10%  |  zoom 20%  |  horizontal flip
```

---

## 📊 Evaluation Metrics

After training, each model was evaluated on a **held-out validation set (15%)** using:

<div align="center">

| Metric | What It Measures |
|:---|:---|
| ✅ Accuracy | Overall correct predictions out of all predictions |
| 🎯 Precision | Of everything predicted as class X, how many truly were X |
| 🔍 Recall | Of everything that was truly X, how many did we catch |
| ⚖️ F1 Score | Harmonic mean of precision & recall — best single metric |
| 📈 ROC-AUC | Area under ROC curve (macro one-vs-rest across all classes) |

</div>

A **confusion matrix** and **per-class precision/recall/F1 bar chart** are generated for the best model.

---

## 🚀 How to Run Locally

### ① Prerequisites

> Python **3.11** is required — TensorFlow does not support Python 3.12 or newer.

```bash
py -3.11 -m pip install flask tensorflow pillow numpy
```

### ② Train the Model (Kaggle)

1. Go to [kaggle.com](https://kaggle.com) → **Create → New Notebook**
2. Upload `butterfly-image-classification.ipynb`
3. Add dataset: search `phucthaiv02/butterfly-image-classification`
4. Set accelerator to **GPU T4 x2**
5. Click **Run All** — wait ~1–2 hours
6. Download `model/butterfly.keras` and `model/butterfly.pkl` from the Output tab

### ③ Set Up Project Folder

```
D:\project\
├── app.py
├── template\index.html
├── model\butterfly.keras      ← paste here
├── model\butterfly.pkl        ← paste here
└── static\uploads\
```

### ④ Launch the App

```bash
D:
cd D:\project
py -3.11 app.py
```

Then open your browser at:
```
http://127.0.0.1:5000
```

---

## 🌐 Web App Features

- 🖱️ **Drag & drop** or click-to-upload image input
- 👁️ **Live preview** of image before submitting
- 🖼️ **Image stays visible** after prediction
- 🦋 **Species name + confidence %** shown clearly
- 🌙 Clean dark-gradient themed UI

---

## 🛠️ Tech Stack

<div align="center">

![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=flat-square&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=flat-square&logo=Keras&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat-square&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat-square&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=flat-square&logo=Matplotlib&logoColor=black)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat-square&logo=flask&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-%2320BEFF.svg?style=flat-square&logo=kaggle&logoColor=white)

</div>

---

## ⚠️ Common Notes

- The warnings about `oneDNN` and GPU when running `app.py` are **completely harmless** — ignore them
- TensorFlow dropped native Windows GPU support after v2.10 — the app runs fine on **CPU**
- First prediction after launch takes a few extra seconds while the model loads into memory
- Always use `py -3.11` explicitly — running with Python 3.14 will fail

---

<div align="center">

Made with 🦋 and deep learning

</div>
