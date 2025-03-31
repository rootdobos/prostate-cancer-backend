from django.http import JsonResponse
from ..data_processing_core.preprocessing.services.tile_service import TileService

import os
from dotenv import load_dotenv

load_dotenv()


def extract_tiles_from_slide(request):
    id = request.GET.get("slideId")  # Get the 'param' value from the URL
    slide_dir=os.getenv("TILES_FOLDER")
    output_dir= os.getenv("")
    if not id:
        return JsonResponse({"error": "Missing slide id"}, status=400)
    
    try:
        TileService.extract_tiles(slide_dir,output_dir)
        return JsonResponse({"message": f"Received parameter: {id}"})
    except Exception:
        return JsonResponse({"error": "Error in extraction"}, status=400)