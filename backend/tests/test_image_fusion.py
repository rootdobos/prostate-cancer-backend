from django.test import TestCase
import numpy as np

from backend.data_processing_core.image_visualization.image_fusion import ImageFusion
from backend.tests.util import checkAlphaPixels
class TestImageFusion(TestCase):

    def test_add_images(self):
        # Define image size (e.g., 256x256 with 3 color channels for RGB)
        height, width, channels = 50, 50, 3

        # Create two random images (values between 0 and 255, dtype uint8)
        image1 = np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)
        image2 = np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)
        black_image_gray = np.zeros((height, width, channels), dtype=np.uint8)

        output_image = ImageFusion.add_images(image1,black_image_gray,0.5)

        pixelCheck = checkAlphaPixels(output_image,image1, 0.5)
        self.assertTrue(pixelCheck)


