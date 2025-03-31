import os
from django.http import JsonResponse
from dotenv import load_dotenv

load_dotenv()


def list_files(request):
    folder_path = os.getenv("SLIDES_FOLDER")

    if not os.path.exists(folder_path):
        return JsonResponse({"error": "Folder not found"}, status=404)

    files = os.listdir(folder_path)  # Get list of files
    file_names = list(map(lambda x: x.split('.')[0], files))
    return JsonResponse({"wsiList": file_names})
