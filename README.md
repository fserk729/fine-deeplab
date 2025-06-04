# fine-deeplab

DeepLabV3+ for semantic segmentation on the FINE dataset.

---

## 📁 Dataset

The FINE dataset is too large to be uploaded to GitHub.  
You can download it from the link below (password: `gitpassfine`):

🔗 [Download FINE Dataset](https://ehb-my.sharepoint.com/:f:/g/personal/fabian_serkeyn_student_ehb_be/EiCFpynSZVNLk_RG9hTfAp4BnJBoeQBa95bUoNysPgkQYA?e=idSXo3)

After downloading, extract the dataset into the `dataset/` directory in the project root.

---

## 📦 Project Structure

| Name               | Type    | Description                                                              |
|--------------------|---------|--------------------------------------------------------------------------|
| `README.md`        | File    | Project overview and documentation (this file)                           |
| `train.py`         | File    | Script to train DeepLabV3+ on the FINE dataset                           |
| `predict.py`       | File    | Script to run inference using a trained model                            |
| `utils/`           | Folder  | Helper functions (preprocessing, metrics, visualization, etc.)           |
| `configs/`         | Folder  | YAML/JSON config files for training and inference                        |
| `checkpoints/`     | Folder  | Stores trained model checkpoints                                         |
| `dataset/`         | Folder  | Local directory for the FINE dataset                                     |
| `visuals/`         | Folder  | Outputs like segmented images or training visualizations                 |
| `.gitignore`       | File    | Specifies files/folders ignored by Git                                   |
| `requirements.txt` | File    | Lists Python dependencies                                                |

---

## 🛠️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/fine-deeplab.git
cd fine-deeplab
pip install -r requirements.txt
```

---

## 🚀 Training

To train the model on the FINE dataset:

```bash
python train.py --config configs/train_config.yaml
```

Make sure your dataset is placed inside the `dataset/` folder and the config file paths are correct.

---

## 🔍 Inference

Run inference on images using a trained model:

```bash
python predict.py --config configs/predict_config.yaml --input path/to/image.jpg
```

Outputs will be saved to the `visuals/` directory by default.

---

## ✅ Requirements

Ensure the following Python packages are installed (handled by `requirements.txt`):

- torch
- torchvision
- matplotlib
- opencv-python
- PyYAML
- tqdm
- scikit-learn
- PIL

---

## 👨‍💻 Author

**Fabian Serkeyn** (EhB)  
In collaboration with **ILVO**

---

## 📄 License

This project is for academic and research use only. Contact the author for other licensing inquiries.
