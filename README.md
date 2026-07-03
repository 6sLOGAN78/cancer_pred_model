# Chest Cancer Classification (CNN) Project

An end-to-end deep learning project for classifying chest CT scan images into cancer or normal conditions. The model uses the VGG16 CNN architecture as a base, followed by a customized classification head. The project is designed with modular pipelines and integrated with DVC (Data Version Control) for reproducible data ingestion, preparation, training, and model evaluation stages.

---

## 🛠️ Project Structure
Here is an overview of the key directories and files:
```text
├── config/
│   └── config.yaml          # Configures directory paths, source URLs, and output locations
├── docs/                     # Additional detailed documentation (CI/CD, MLflow)
│   ├── CI_CD.md             # Detailed deployment & workflow pipeline integration guide
│   └── MLflow.md            # Detailed experiments mapping & tracking values
├── research/                # Jupyter Notebooks for initial research and prototyping
├── templates/
│   └── index.html           # Simple web client UI for prediction uploads
├── src/cnnClassifier/
│   ├── components/          # Pipeline component implementations
│   ├── config/              # Configuration manager loads settings from config.yaml
│   ├── constants/           # Project level constants
│   ├── entity/              # Python custom types/dataclasses (config entities)
│   ├── pipeline/            # Stage-by-stage pipelines (ingestion -> evaluation -> prediction)
│   └── utils/               # Common helper functions (e.g. image decoding, JSON saving)
├── app.py                   # Flask server wrapper containing prediction and training API routes
├── dvc.yaml                 # DVC pipeline stages and dependencies definition
├── main.py                  # End-to-end pipeline execution entrypoint script
├── params.yaml              # Hyperparameters (learning rate, batch size, image dimensions, epochs)
├── requirements.txt         # Project package dependencies
└── setup.py                 # Project packaging setup
```

---

## 🚀 Setting Up the Project

### Prerequisites
- Python 3.8+ (Note: Tensorflow 2.12.0 is used, which is compatible with Python 3.8 - 3.11).

### Setup Steps
1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd Chest-Cancer-Classification-Project
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows:**
     ```cmd
     venv\Scripts\activate
     ```

4. **Install Python packages:**
   ```bash
   pip install -r requirements.txt
   ```
   *Note: This will also install the package itself in editable mode (`-e .` from requirements.txt).*

---

## ⚙️ Workflows & Pipelines

The application is structured into four main sequential stages:
1. **Data Ingestion:** Downloads the raw Chest CT Scan dataset (ZIP) from Google Drive storage and decompresses it under `artifacts/data_ingestion/`.
2. **Prepare Base Model:** Downloads/loads the pre-trained VGG16 model, freezes its convolutional base, and appends a modified dense classifier layout with two nodes (tumor, normal).
3. **Training:** Trains the base model using input parameters (augmentation toggles, batch sizes, image shape) and saves the trained file under `artifacts/training/model.h5`.
4. **Evaluation:** Computes final loss/accuracy metrics on validation splits and writes summary outputs to a root-level `scores.json`.

---

## 🎯 How to Run the Project

### Option A: Run via DVC (Recommended)
DVC keeps track of pipeline execution dependencies, params, outputs, and intermediate caches. To execute or reproduce the pipeline:
```bash
dvc repro
```
If nothing has changed in raw scripts, configuration, or parameters, DVC will reuse outputs from the cache instead of computing them again. To query the validation metrics via DVC:
```bash
dvc metrics show
```

### Option B: Run via standard Python Entrypoint
If you wish to execute the entire stages in order without DVC tracking/caching:
```bash
python main.py
```
This script imports and triggers each pipeline stage sequentially.

---

## 🌐 Web Server & APIs

The project comes with a Flask web application that serves a browser interface for making predictions and triggering model training.

### Starting the Web Server
Launch the application:
```bash
python app.py
```
By default, the server will bind to `0.0.0.0` on port `8080`. You can access it locally at [http://localhost:8080](http://localhost:8080).

### API Routes
- **`GET /`**: Renders the index user interface to drag-and-drop or select chest CT scan images.
- **`POST /predict`**: Accepts a JSON body containing a base64 encoded image string, decodes it, saves it locally as `inputImage.jpg`, and returns the model classification decision.
  - Request: `{"image": "<base64_encoded_image_string>"}`
  - Response format: `[{"image": "malignant_or_normal"}]`
- **`POST /train` (or `GET /train`)**: Sequentially executes target pipeline code by initiating `python main.py` under the hood. Returns validation status once training is complete.

---

## 🧪 Experiments Tracking & CI/CD Deployment

For more details on advanced workflows integrated into this project:
- Read **[MLflow Tracking Integration Guide](file:///home/logan78/efforts/projects/completed/end_to_End/docs/MLflow.md)** to see how parameter tuning, accuracy/loss metrics, and models are tracked in DagsHub MLflow.
- Read **[CI/CD Production Deployment Guide](file:///home/logan78/efforts/projects/completed/end_to_End/docs/CI_CD.md)** to see how git-pushes to the main branch automatically trigger continuous lint testing, container creation, pushes to Amazon ECR, and deployment onto hosting servers via AWS self-hosted runners.
