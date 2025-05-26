import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the converted mask
mask_path = 'test1_structured/ann_dir/01b5c101-e53c-4718-a703-df24f62af5cb_151728_5_Component 1 b_rgb.png'  # Change to one of your files
# Read the mask image (ensure it's read in RGB!)
mask = cv2.imread(mask_path)
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)  # <- Important!

# Check unique pixel values (should show class IDs)
unique_values = np.unique(mask)
print("Unique pixel values (class IDs):", unique_values)

# Optional: plot with better contrast
plt.imshow(mask, cmap='nipy_spectral')
plt.title("Class ID mask visualization")
plt.colorbar()
plt.show()
