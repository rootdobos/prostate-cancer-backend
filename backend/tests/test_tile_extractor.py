from pathlib import Path
from django.test import TestCase
import os
import shutil
import tempfile
from PIL import Image

from backend.data_processing_core.preprocessing.tile_extractor import TileExtractor


class TileExtractorTestCase(TestCase):

    def setUp(self):
        self.in_dir = tempfile.mkdtemp()
        self.out_dir = tempfile.mkdtemp()
        self.tiff_path = os.path.join(self.in_dir, "test_slide.tiff")
        image = Image.new('RGB', (2048, 2048), color=(0, 0, 0))
        image.save(self.tiff_path, format='TIFF')
        self.white_tiff_path = os.path.join(self.in_dir, "test_slide_white.tiff")
        image = Image.new('RGB', (2048, 2048), color=(255, 255, 255))
        image.save(self.white_tiff_path, format='TIFF')

    def tearDown(self):
        # Clean up the temp file
        if os.path.exists(self.in_dir):
            shutil.rmtree(self.in_dir)
        if os.path.exists(self.out_dir):
            shutil.rmtree(self.out_dir)
    def test_process_image(self):
        tile_extractor = TileExtractor(
            input_dir=self.in_dir,
            output_dir=self.out_dir,
            tile_size=256,
            inverse_zoom_level=1
        )
        tile_extractor.process_image('test_slide', True)
        out_dir_test = os.path.join(self.out_dir,'test_slide')
        files=os.listdir(out_dir_test)
        number_of_extracted_tiles = len(files)
        self.assertEqual(number_of_extracted_tiles,36)

        for i in range(1,7):
            for j in range(1,7):
                name = f"{i}_{j}.png"
                if not (os.path.exists(os.path.join(out_dir_test,name))):
                    print(os.path.join(out_dir_test,name))
                self.assertTrue(os.path.exists(os.path.join(out_dir_test,name)))

    def test_process_white_image(self):
        tile_extractor = TileExtractor(
            input_dir=self.in_dir,
            output_dir=self.out_dir,
            tile_size=256,
            inverse_zoom_level=1
        )

        tile_extractor.process_image('test_slide_white', True)
        out_dir_test = os.path.join(self.out_dir,'test_slide_white')
        files=os.listdir(out_dir_test)
        number_of_extracted_tiles = len(files)
        self.assertEqual(number_of_extracted_tiles,0)
