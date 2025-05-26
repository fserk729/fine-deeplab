import os
from PIL import Image

# Your custom dataset paths
image_dir = "DeepLabV3+_data\deeplab_struc\images"
ann_dir = "DeepLabV3+_data\deeplab_struc\masks"

# Make sure output folder exists
os.makedirs(ann_dir, exist_ok=True)

# Loop through all images
for img_name in os.listdir(image_dir):
    base_name, _ = os.path.splitext(img_name)
    ann_path = os.path.join(ann_dir, base_name + ".png")

    # Skip if annotation already exists
    if os.path.exists(ann_path):
        continue

    # Load image to get dimensions
    img_path = os.path.join(image_dir, img_name)
    with Image.open(img_path) as img:
        width, height = img.size

    # Create a blank mask with class ID 0 (background)
    blank_mask = Image.new("L", (width, height), color=0)
    blank_mask.save(ann_path)

print("✅ All missing masks in ann_dir filled with blank (background-only) masks.")
