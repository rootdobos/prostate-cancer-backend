from django.http import JsonResponse
from ..data_processing_core.preprocessing.services.tile_service import TileService

import os
from dotenv import load_dotenv

load_dotenv()


def extract_tiles_from_slide(request):
    id = request.GET.get("slideId")  # Get the 'param' value from the URL
    slide_dir = os.getenv("SLIDES_FOLDER")
    output_dir = os.getenv("TILES_FOLDER")
    if not id:
        return JsonResponse({"error": "Missing slide id"}, status=400)

    try:
        TileService.extract_tiles(id, slide_dir, output_dir)
        return JsonResponse({"message": f"Extracted tiles from: {id}"})
    except Exception:
        return JsonResponse({"error": "Error in extraction"}, status=400)
