import os
from PIL import Image
import numpy as np
import torch
import torch.utils.data as data
import torchvision.transforms

class MyDataset(data.Dataset):
    def __init__(self, root, split='train', transform=None):
        self.root = root
        self.split = split
        self.transform = transform

        self.image_dir = os.path.join(root, 'images', split)
        self.mask_dir = os.path.join(root, 'masks', split)

        self.images = sorted(os.listdir(self.image_dir))
        self.masks = sorted(os.listdir(self.mask_dir))

        assert len(self.images) == len(self.masks), "Number of images and masks must match"

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):
        img_path = os.path.join(self.root, 'images', self.split, self.images[index])
        mask_path = os.path.join(self.root, 'masks', self.split, self.masks[index])

        image = Image.open(img_path).convert('RGB')
        mask = Image.open(mask_path).convert('RGB')

        if self.transform:
            image, mask = self.transform(image, mask)
        else:
            image = torchvision.transforms.ToTensor()(image)

        mask = self.rgb_to_class(mask)
        mask = torch.from_numpy(mask).long()

        return image, mask

    def rgb_to_class(self, mask):
        """
        Converts an RGB mask (H x W x 3) to class indices (H x W).
        """
        cmap = np.array([
            [0, 0, 0],         # background
            [250, 50, 83],     # Groenten
            [52, 209, 183],    # Samengesteld
            [50, 183, 250],    # Saus
            [250, 250, 55],    # Vlees/Vis
            [102, 255, 102],   # Zetmeel
        ], dtype=np.uint8)

        mask_np = np.array(mask)
        h, w, _ = mask_np.shape
        class_mask = np.zeros((h, w), dtype=np.int64)  # to store class indices

        for i, color in enumerate(cmap):
            matches = np.all(mask_np == color, axis=-1)
            class_mask[matches] = i

        return class_mask

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
