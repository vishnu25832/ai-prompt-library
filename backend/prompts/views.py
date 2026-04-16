import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Prompt


# GET + POST /prompts/
@csrf_exempt
def prompts(request):
    if request.method == "GET":
        data = list(Prompt.objects.values("id", "title", "complexity"))
        return JsonResponse(data, safe=False)

    if request.method == "POST":
        body = json.loads(request.body)

        if len(body.get("title", "")) < 3:
            return JsonResponse({"error": "Title too short"}, status=400)

        if len(body.get("content", "")) < 20:
            return JsonResponse({"error": "Content too short"}, status=400)

        if not (1 <= int(body.get("complexity", 0)) <= 10):
            return JsonResponse({"error": "Invalid complexity"}, status=400)

        prompt = Prompt.objects.create(
            title=body["title"],
            content=body["content"],
            complexity=body["complexity"]
        )

        return JsonResponse({"id": str(prompt.id)})


# GET /prompts/<id>/
def get_prompt(request, id):
    try:
        prompt = Prompt.objects.get(id=id)

        key = f"prompt:{id}:views"
        view_count = settings.REDIS_CLIENT.incr(key)

        data = {
            "id": str(prompt.id),
            "title": prompt.title,
            "content": prompt.content,
            "complexity": prompt.complexity,
            "view_count": view_count
        }

        return JsonResponse(data)

    except Prompt.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)