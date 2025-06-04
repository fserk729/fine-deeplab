# fine-deeplab

DeepLabV3+ for FINE dataset segmentation

---

## Dataset

The dataset is too large to upload to GitHub.  
Download it here (password: `gitpassfine`):  
[Download FINE Dataset](https://ehb-my.sharepoint.com/:f:/g/personal/fabian_serkeyn_student_ehb_be/EiCFpynSZVNLk_RG9hTfAp4BnJBoeQBa95bUoNysPgkQYA?e=idSXo3)

---

## Project Structure

| Name               | Type    | Description                                                              |
|--------------------|---------|--------------------------------------------------------------------------|
| `README.md`        | File    | Project overview and documentation (this file)                           |
| `train.py`         | File    | Script to train DeepLabV3+ on the FINE dataset                           |
| `predict.py`       | File    | Script to run inference using a trained model                            |
| `utils/`           | Folder  | Helper functions for preprocessing, metrics, visualization, etc.         |
| `configs/`         | Folder  | YAML/JSON configuration files for model training/inference               |
| `checkpoints/`     | Folder  | Saved model weights and checkpoints                                      |
| `dataset/`         | Folder  | Local directory where the FINE dataset should be placed                  |
| `visuals/`         | Folder  | Contains output images, segmentation results, or training visualizations |
| `.gitignore`       | File    | Specifies intentionally untracked files to ignore by Git                 |
| `requirements.txt` | File    | Lists Python dependencies for installing required packages               |

---
```markdown
## Installation

```bash
pip install -r requirements.txt
```

```markdown

## Author 

Fabian Serkeyn (EhB) @ ILVO
```
