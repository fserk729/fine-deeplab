import os
import shutil
import random

# Source folders (correct paths based on your information)
src_images = r"C:/Users/fabia/Documents/PGAI/Internship/FINE/_datasets/test1_structured/images"
src_masks = r"C:/Users/fabia/Documents/PGAI/Internship/FINE/_datasets/test1_structured/ann_dir"

# Output split dataset folder (destination)
dst_root = r"C:/Users/fabia/Documents/PGAI/Internship/FINE/_datasets/FoodSAM/dataset/test1_split"
train_ratio = 0.8  # 80% train, 20% validation

# Collect all valid image-mask pairs
all_files = [f for f in os.listdir(src_images) if os.path.splitext(f)[1].lower() in ['.jpg', '.jpeg', '.png', '.bmp']]
print(f"Found {len(all_files)} images in the source image folder.")

# Ensure there is a valid corresponding mask for each image
paired_files = [f for f in all_files if os.path.exists(os.path.join(src_masks, os.path.splitext(f)[0] + '.png'))]
print(f"Found {len(paired_files)} valid image-mask pairs.")

# Shuffle and split into training and validation
random.shuffle(paired_files)
split_idx = int(len(paired_files) * train_ratio)
train_files = paired_files[:split_idx]
val_files = paired_files[split_idx:]

# Helper to copy files
def copy_split(files, split):
    img_out = os.path.join(dst_root, "img_dir", split)
    ann_out = os.path.join(dst_root, "ann_dir", split)
    
    # Ensure output directories exist
    os.makedirs(img_out, exist_ok=True)
    os.makedirs(ann_out, exist_ok=True)
    
    print(f"Copying {len(files)} {split} files.")
    
    for fname in files:
        base = os.path.splitext(fname)[0]
        img_src = os.path.join(src_images, fname)
        mask_src = os.path.join(src_masks, base + ".png")
        
        if os.path.exists(img_src) and os.path.exists(mask_src):
            shutil.copy(img_src, os.path.join(img_out, fname))
            shutil.copy(mask_src, os.path.join(ann_out, base + ".png"))
        else:
            print(f"Missing pair for {fname}!")

# Copy files to training and validation folders
copy_split(train_files, "train")
copy_split(val_files, "val")

print(f"✅ Done! Split {len(train_files)} train / {len(val_files)} val images into {dst_root}")
