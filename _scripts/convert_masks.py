import os
import cv2
import numpy as np
from tqdm import tqdm

# Define your input/output folders
input_dir = "test1_structured/masks"
output_dir = "test1_structured/ann_dir"
os.makedirs(output_dir, exist_ok=True)

# Define your color-to-class-ID mapping
color_to_id = {
    (250, 50, 83): 0,     # Groenten
    (50, 183, 250): 1,    # Saus
    (250, 250, 55): 2,    # Vlees/Vis
    (0, 0, 0): 255        # background
}

# Find closest color in RGB space
def closest_class(color):
    min_dist = float('inf')
    class_id = 255  # default to background
    for rgb, cid in color_to_id.items():
        dist = np.linalg.norm(np.array(color) - np.array(rgb))
        if dist < min_dist:
            min_dist = dist
            class_id = cid
    return class_id

# Convert one mask
def convert_mask(mask_path, output_path):
    mask = cv2.imread(mask_path)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)
    h, w, _ = mask.shape
    output = np.zeros((h, w), dtype=np.uint8)

    for y in range(h):
        for x in range(w):
            rgb = mask[y, x]
            class_id = closest_class(rgb)
            output[y, x] = class_id

    cv2.imwrite(output_path, output)

# Loop through all mask files
print("Found", len(os.listdir(input_dir)), "files in input_dir.")
for fname in tqdm(os.listdir(input_dir)):
    if fname.lower().endswith(".png"):
        in_path = os.path.join(input_dir, fname)
        out_path = os.path.join(output_dir, fname)
        convert_mask(in_path, out_path)
