from django.http import JsonResponse
from ..data_processing_core.preprocessing.services.tile_service import TileService
from ..data_processing_core.deep_learning.services.attention_score_service import AttentionScoreService
from ..data_processing_core.image_visualization.attention_visualization_service import AttentionVisualizationService
import os
import shutil
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

load_dotenv()


def extract_tiles_from_slide(request):
    id = request.GET.get("slideId")
    slide_dir = os.getenv("SLIDES_FOLDER")
    output_dir = os.getenv("TILES_FOLDER")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not id:
        return JsonResponse({"error": "Missing slide id"}, status=400)

    try:
        slide_tile_path = os.path.join(output_dir, id)
        if os.path.exists(slide_tile_path):
            shutil.rmtree(slide_tile_path)
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
    Y_prob, scores = AttentionScoreService.get_attention_scores_from_features(
        model_name, weights_path, features_path)
    result = {
        "label": Y_prob.argmax().item(),
        "probabilities": Y_prob.tolist(),
        "attention_scores": scores
    }
    return JsonResponse(result)
    # except Exception:
    #     return JsonResponse({"error": "Error in attention score calculation"}, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def get_attention_tiles(request):
    body = json.loads(request.body)
    label = body.get("label")
    attention_scores = body.get("attention_scores")
    id = body.get("slideId")
    if not id:
        return JsonResponse({"error": "Missing slide id"}, status=400)

    tiles_dir = os.getenv("TILES_FOLDER")
    visualization_dir = os.getenv("VISUALIZATION_DIRECTORY")
    tiles_path = os.path.join(tiles_dir, id)
    AttentionVisualizationService.create_visualization(
        256, tiles_path, visualization_dir, attention_scores, label)

    return JsonResponse({"result": "ok"})
