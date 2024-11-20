import cv2
import numpy as np


def processing(image, gamma=2.2):
    gamma_inv = 1.0 / gamma
    table = np.array([(i / 255.0) ** gamma_inv * 255 for i in range(256)]).astype("uint8")

    return cv2.LUT(image, table)
