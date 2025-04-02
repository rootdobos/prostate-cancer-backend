from django.http import JsonResponse
from ..data_processing_core.deep_learning.services.feature_extraction_service import FeatureExtractionService
import os
from dotenv import load_dotenv

load_dotenv()


def encode_slide_tiles(request):
    id = request.GET.get("slideId")  # Get the 'param' value from the URL
    if not id:
        return JsonResponse({"error": "Missing slide id"}, status=400)

    tile_dir = os.getenv("TILES_FOLDER")
    extractor = os.getenv("FEATURE_ENCODING_MODEL_NAME")
    feature_dir = os.getenv("FEATURES_FOLDER")

    FeatureExtractionService.extract_features(
        extractor, id, tile_dir, feature_dir)
    return JsonResponse({"message": f"Extracted features from {id}"})
