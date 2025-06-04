# FINE-DeepLab

DeepLabV3+ for semantic segmentation on the FINE dataset.

---

## Dataset

The FINE dataset is too large to be uploaded to GitHub.  
You can download it from the link below (password: `gitpassfine`):

[Download FINE Dataset](https://ehb-my.sharepoint.com/:f:/g/personal/fabian_serkeyn_student_ehb_be/EiCFpynSZVNLk_RG9hTfAp4BnJBoeQBa95bUoNysPgkQYA?e=idSXo3)

After downloading, extract the dataset into the `dataset/` directory in the project root.

---

## Project Structure

| Name                 | Type    | Description                                                        |
|----------------------|---------|--------------------------------------------------------------------|
| `README.md`          | File    | Project overview and documentation (this file)                     |
| `_scripts/`          | Folder  | Folder including all scripts for data preprocessing                |
| `_data/`             | Folder  | Save dataset here                                                  |
| `../main.py`         | File    | Main script to run the model or pipeline                           |
| `../custom_train.sh` | File    | Shell script to run training; parameters can be adjusted here      |
| `../checkpoints/`    | Folder  | Stores trained model checkpoints                                   |
| `../results/`        | Folder  | Stores visual results (images of predictions, etc.)                |

---

## Training

To run the training command, do this in terminal:
```bash
path/to/custom_train.sh
```

---

## Requirements

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

## Author

**Fabian Serkeyn** (EhB)  
@ **ILVO**

