import os
from PIL import Image
import numpy as np
import torch.utils.data as data

class MyDataset(data.Dataset):
    def __init__(self, root, split='train', transform=None):
        self.root = root
        self.split = split
        self.transform = transform
        self.images = sorted(os.listdir(os.path.join(root, 'images')))
        self.masks = sorted(os.listdir(os.path.join(root, 'masks')))

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):
        img_path = os.path.join(self.root, 'images', self.images[index])
        mask_path = os.path.join(self.root, 'masks', self.masks[index])

        image = Image.open(img_path).convert('RGB')
        mask = Image.open(mask_path)

        if self.transform:
            image, mask = self.transform(image, mask)

        return image, mask

    @classmethod
    def decode_target(cls, mask):
        cmap = np.array([
            [0, 0, 0],         # background
            [250, 50, 83],     # Groenten
            [52, 209, 183],    # Samengesteld
            [50, 183, 250],    # Saus
            [250, 250, 55],    # Vlees/Vis
            [102, 255, 102],   # Zetmeel
        ], dtype=np.uint8)

        if isinstance(mask, Image.Image):
            mask = np.array(mask)

        if mask.ndim != 2:
            raise ValueError("Mask must be a 2D array")

        if mask.max() >= len(cmap):
            raise ValueError(f"Mask contains invalid class index {mask.max()}")

        return cmap[mask]
