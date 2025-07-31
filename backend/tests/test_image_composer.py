
from django.test import TestCase

from backend.data_processing_core.image_visualization.attention_visualization_service import (ImageComposer,
                                                                                              create_attention_image, interpolate_value, ATTENTION_COLORS)
from backend.tests.util import checkPixels


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

