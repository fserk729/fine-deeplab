from PIL import Image
import numpy as np
import os

# 🎯 Class color map
COLOR_MAP = {
    (0, 0, 0): 0,           # background
    (250, 50, 83): 1,       # Groenten
    (52, 209, 183): 2,      # Samengesteld
    (50, 183, 250): 3,      # Saus
    (250, 250, 55): 4,      # Vlees/Vis
    (102, 255, 102): 5,     # Zetmeel
}

def convert_rgb_to_index(mask_path, save_path):
    rgb = Image.open(mask_path).convert('RGB')
    rgb_np = np.array(rgb)

    index_mask = np.zeros((rgb_np.shape[0], rgb_np.shape[1]), dtype=np.uint8)

    for color, class_idx in COLOR_MAP.items():
        matches = np.all(rgb_np == color, axis=-1)
        index_mask[matches] = class_idx

    Image.fromarray(index_mask).save(save_path)

# 🔁 Batch convert folder
input_folder = 'DeepLabV3+_data\deeplab_preproc\RGBmask'       # Folder with RGB masks from CVAT
output_folder = 'DeepLabV3+_data\deeplab_preproc\gray_mask'  # Where grayscale masks will go

os.makedirs(output_folder, exist_ok=True)

for fname in os.listdir(input_folder):
    if fname.lower().endswith('.png'):
        in_path = os.path.join(input_folder, fname)
        out_path = os.path.join(output_folder, fname)
        convert_rgb_to_index(in_path, out_path)
        print(f"✅ Converted: {fname}")
