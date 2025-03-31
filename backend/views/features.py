from django.http import JsonResponse

def encode_slide_tiles(request):
    id = request.GET.get("slideId")  # Get the 'param' value from the URL
    if not id:
        return JsonResponse({"error": "Missing slide id"}, status=400)

    return JsonResponse({"message": f"Received parameter: {id}"})
#TODO: call encoding
