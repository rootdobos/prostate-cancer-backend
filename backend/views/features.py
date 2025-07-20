from django.http import JsonResponse
from ..data_processing_core.deep_learning.services.feature_extraction_service import FeatureExtractionService
import os
from dotenv import load_dotenv
from ..utils.lock import PerKeyLock


load_dotenv()

per_key_lock = PerKeyLock()
def encode_slide_tiles(request):
    id = request.GET.get("slideId")  # Get the 'param' value from the URL
    if not id:
        return JsonResponse({"error": "Missing slide id"}, status=400)
    with per_key_lock.acquire(id):

        tile_dir = os.getenv("TILES_FOLDER")
        extractor = os.getenv("FEATURE_ENCODING_MODEL_NAME")
        feature_dir = os.getenv("FEATURES_FOLDER")

        if not os.path.exists(feature_dir):
            os.makedirs(feature_dir)

        output_path = os.path.join(
            feature_dir, "{}.pt".format(id))
        
        if os.path.exists(output_path):
            return JsonResponse({"message": f"Features already extracted {id}"})

        FeatureExtractionService.extract_features(
            extractor, id, tile_dir, feature_dir)
        return JsonResponse({"message": f"Extracted features from {id}"})
