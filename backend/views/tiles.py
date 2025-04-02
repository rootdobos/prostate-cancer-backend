from django.http import JsonResponse
from ..data_processing_core.preprocessing.services.tile_service import TileService
from ..data_processing_core.deep_learning.services.attention_score_service import AttentionScoreService
import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv

load_dotenv()


def extract_tiles_from_slide(request):
    id = request.GET.get("slideId")
    slide_dir = os.getenv("SLIDES_FOLDER")
    output_dir = os.getenv("TILES_FOLDER")
    if not id:
        return JsonResponse({"error": "Missing slide id"}, status=400)

    try:
        TileService.extract_tiles(id, slide_dir, output_dir)
        return JsonResponse({"message": f"Extracted tiles from: {id}"})
    except Exception:
        return JsonResponse({"error": "Error in extraction"}, status=400)


def get_attention_scores(request):
    id = request.GET.get("slideId")
    if not id:
        return JsonResponse({"error": "Missing slide id"}, status=400)

    model_name = os.getenv("ATTENTION_MODEL_NAME")
    weights_path = os.getenv("ATTENTION_MODEL_WEIGHTS_PATH")

    features_dir = os.getenv("FEATURES_FOLDER")
    features_path = os.path.join(features_dir, f"{id}.pt")
    # try:
    Y_prob, A = AttentionScoreService.get_attention_scores_from_features(
        model_name, weights_path, features_path)
    result = {
        "label": Y_prob.argmax().item(),
        "probabilities": Y_prob.tolist(),
        "attention_scores": A.tolist()
    }
    return JsonResponse(result)
    # except Exception:
    #     return JsonResponse({"error": "Error in attention score calculation"}, status=400)
