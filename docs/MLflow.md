# 📊 MLflow Tracking with DagsHub

This project integrates **MLflow** for experiment tracking and model registry, linked with a remote **DagsHub** repository.

The configuration and metrics submission codebase is implemented in [model_evaluation_mlflow.py](file:///home/logan78/efforts/projects/completed/end_to_End/src/cnnClassifier/components/model_evaluation_mlflow.py).

---

## 🎯 Tracked Parameters and Metrics

When running the evaluation pipeline, MLflow logs the following details of the experiment:

### 1. Parameters (Loaded from `params.yaml`)
- `AUGMENTATION`: Data augmentation boolean toggle
- `IMAGE_SIZE`: Target height, width, and channels
- `BATCH_SIZE`: Minibatch configuration for training
- `INCLUDE_TOP`: Toggle base model final layer inclusion
- `EPOCHS`: Training cycles limit
- `CLASSES`: Number of classification output labels
- `WEIGHTS`: Network starting state (e.g. `imagenet`)
- `LEARNING_RATE`: Optimizer step weight

### 2. Metrics (Computed during Evaluation)
- `loss`: Final validation cost value
- `accuracy`: Validation categorical classification score

### 3. Model Artifacts
- The model structure and parameters are packaged as a Keras/Tensorflow artifact under `model/`.
- If tracking remotely, the model is logged and added to the MLflow Model Registry under the name `VGG16Model`.

---

## ⚙️ Configuration Setup

Evaluation parameters are managed programmatically via [configuration.py](file:///home/logan78/efforts/projects/completed/end_to_End/src/cnnClassifier/components/config/configuration.py):
```python
mlflow_uri="https://dagshub.com/6sLOGAN78/cancer_pred_model.mlflow"
```

### Authentication Credentials
Because the tracking server is remote on DagsHub, the Python environment requires authentication credentials to push metric logs successfully. Export the following variables in your execution environment before running the evaluation:

```bash
# Set DagsHub Tracking Endpoint Credentials
export MLFLOW_TRACKING_URI="https://dagshub.com/6sLOGAN78/cancer_pred_model.mlflow"
export MLFLOW_TRACKING_USERNAME="<your_dagshub_username>"
export MLFLOW_TRACKING_PASSWORD="<your_dagshub_token_or_password>"
```

Once tracking environment variables are set:
1. Running `dvc repro` will automatically trigger evaluation logging into MLflow.
2. Training and evaluation logs can be reviewed directly in your DagsHub project dashboard under the **Experiments** tab.
