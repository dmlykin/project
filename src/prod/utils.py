import io

import numpy as np
import cv2
from PIL import Image


def read_image(bytestring):
    image = np.fromstring(bytestring, np.uint8)
    if image is None or image.size == 0:
        return None

    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    if image is None:
        return None

    return image


def jpeg_bytes_io(image: np.ndarray, quality=80):
    bytes_ = io.BytesIO()
    Image.fromarray(image).save(bytes_, "JPEG", quality=quality, optimize=True)
    bytes_.seek(0)
    return bytes_
