from PIL import Image
import os

image_dir = "test1_structured/images"
mask_dir = "test1_structured/masks"
os.makedirs(mask_dir, exist_ok=True)

# Loop over all images
for fname in os.listdir(image_dir):
    base, ext = os.path.splitext(fname)
    mask_path = os.path.join(mask_dir, base + ".png")
    
    # Skip if mask already exists
    if os.path.exists(mask_path):
        continue

    # Load image to get dimensions
    img = Image.open(os.path.join(image_dir, fname))
    width, height = img.size

    # Create a black (background-only) mask
    background_mask = Image.new("RGB", (width, height), color=(0, 0, 0))
    background_mask.save(mask_path)

print("✅ Background masks created for unlabeled images.")
