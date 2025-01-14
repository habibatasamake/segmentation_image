import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance
import numpy as np

def plot_img_and_mask(img, mask):
    classes = mask.shape[0] if len(mask.shape) > 2 else 1
    fig, ax = plt.subplots(1, classes)
    ax[0].set_title('Input image')
    enhancer = ImageEnhance.Contrast(img.convert('RGB'))
    ax[0].imshow(enhancer.enhance(1))
    # if classes > 1:
    #     for i in range(classes):
    #         ax[i + 1].set_title(f'Output mask (class {i + 1})')
    #         ax[i + 1].imshow(mask[:, :, i])
    # else:
    #     ax[1].set_title(f'Output mask')
    #     ax[1].imshow(mask)
    ax[1].set_title('Mask')
    mask = Image.fromarray(np.array(mask[1]*255).astype(np.uint8))
    ax[1].imshow(mask)
    plt.xticks([]), plt.yticks([])
    plt.show()
