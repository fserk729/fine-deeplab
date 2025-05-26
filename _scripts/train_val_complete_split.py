import os
import shutil
import random
from pathlib import Path
from PIL import Image

from collections import defaultdict

def collect_image_mask_pairs_grouped(image_root, mask_root):
    image_paths = list(Path(image_root).rglob('RGB/*.bmp'))
    grouped_pairs = defaultdict(list)

    for img_path in image_paths:
        relative_path = img_path.relative_to(image_root)
        date_folder = relative_path.parts[0]
        file_name = img_path.stem + '.png'
        mask_path = Path(mask_root) / date_folder / 'RGB' / file_name

        # Safety check: match date folders
        img_parent = img_path.parent.parent.name
        mask_parent = mask_path.parent.parent.name
        if img_parent == mask_parent:
            grouped_pairs[date_folder].append((img_path, mask_path))

    return grouped_pairs

def split_and_copy_grouped(grouped_pairs, out_root, train_ratio=0.8):
    date_folders = list(grouped_pairs.keys())
    random.shuffle(date_folders)

    split_idx = int(len(date_folders) * train_ratio)
    train_folders = date_folders[:split_idx]
    val_folders = date_folders[split_idx:]

    for subset, folder_list in [('train', train_folders), ('val', val_folders)]:
        for folder in folder_list:
            for img_path, mask_path in grouped_pairs[folder]:
                out_img = Path(out_root) / 'images' / subset / img_path.name
                out_mask = Path(out_root) / 'masks' / subset / img_path.with_suffix('.png').name

                shutil.copy(img_path, out_img)
                copy_or_create_mask(mask_path, out_mask)

def create_blank_mask(path, size=(2048, 2048)):
    blank = Image.new('RGB', size, color=(0, 0, 0))
    blank.save(path)

def collect_image_mask_pairs(image_root, mask_root):
    image_paths = list(Path(image_root).rglob('RGB/*.bmp'))
    pairs = []

    for img_path in image_paths:
        relative_path = img_path.relative_to(image_root)
        date_folder = relative_path.parts[0]
        file_name = img_path.stem + '.png'
        mask_path = Path(mask_root) / date_folder / 'RGB' / file_name

        # Safety check: compare parent folder two levels up
        img_parent = img_path.parent.parent.name
        mask_parent = mask_path.parent.parent.name
        if img_parent == mask_parent:
            pairs.append((img_path, mask_path))

    return pairs

def prepare_output_dirs(base_out_path):
    for subset in ['train', 'val']:
        for subfolder in ['images', 'masks']:
            dir_path = Path(base_out_path) / subfolder / subset
            dir_path.mkdir(parents=True, exist_ok=True)

def copy_or_create_mask(mask_src, mask_dest):
    if mask_src.exists():
        shutil.copy(mask_src, mask_dest)
    else:
        create_blank_mask(mask_dest)

def split_and_copy(pairs, out_root, train_ratio=0.8):
    random.shuffle(pairs)
    split_idx = int(len(pairs) * train_ratio)
    train_pairs = pairs[:split_idx]
    val_pairs = pairs[split_idx:]

    for subset, subset_pairs in [('train', train_pairs), ('val', val_pairs)]:
        for img_path, mask_path in subset_pairs:
            out_img = Path(out_root) / 'images' / subset / img_path.name
            out_mask = (Path(out_root) / 'masks' / subset / img_path.name).with_suffix('.png')
            shutil.copy(img_path, out_img)
            copy_or_create_mask(mask_path, out_mask)


def main():
    image_root = 'C:/Users/fabia/Documents/PGAI/Internship/FINE/deeplabv3_fine_git/_data/complete_FINE_data/images'
    mask_root = 'C:/Users/fabia/Documents/PGAI/Internship/FINE/deeplabv3_fine_git/_data/complete_FINE_data/masks'
    out_root = 'C:/Users/fabia/Documents/PGAI/Internship/FINE/deeplabv3_fine_git/_data/deeplab_struc_complete'
    train_ratio = 0.8  # Change this value to adjust split ratio

    print("Collecting image-mask pairs...")
    grouped_pairs = collect_image_mask_pairs_grouped(image_root, mask_root)
    print(f"Total folders found: {len(grouped_pairs)}")

    print("Preparing output directories...")
    prepare_output_dirs(out_root)

    print("Copying and splitting dataset...")
    split_and_copy_grouped(grouped_pairs, out_root, train_ratio)

    print("Done!")

if __name__ == '__main__':
    main()
