from pathlib import Path
from django.test import TestCase
import os
import shutil
import tempfile
from PIL import Image

from backend.data_processing_core.image_visualization.attention_visualization_service import (ImageComposer,
                                                                                              create_attention_image, interpolate_value, ATTENTION_COLORS)


class TestImageComposer(TestCase):

    def setUp(self):
        pass

    def test_create_attention_image(self):
        for i in range(6):
            label = str(i)
            image = create_attention_image(label, 1, 50, 50)
            pixelCheck = checkPixels(image, ATTENTION_COLORS[label])
            self.assertTrue(pixelCheck)

    def test_interpolate_value(self):
        interval = (0,1)
        self.assertEqual(interpolate_value(interval,-1),0)
        self.assertEqual(interpolate_value(interval,2),1)
        self.assertEqual(interpolate_value(interval,0.5),0.5)

        interval = (0,2)
        self.assertEqual(interpolate_value(interval,1),0.5)
        self.assertEqual(interpolate_value(interval,1.5),0.75)
        self.assertEqual(interpolate_value(interval,.5),0.25)

def checkPixels(image, expected_color):
    width, height, channels = image.shape
    for x in range(width):
        for y in range(height):
            for c in range(channels):
                if image[x][y][c] != expected_color[c]:
                    return False
    return True
