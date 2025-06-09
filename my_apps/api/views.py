from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings

import datetime
import json
import os


@csrf_exempt
def login_view(request):
    """
    A simple view to handle login.
    """
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            version = body.get("version")
            # 处理 version
            return JsonResponse({"msg": "OK", "version": version})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)


@csrf_exempt
def about_required(request):

    data = {
        'info': 'This is the About API endpoint.',
        'method': request.method,
    }

    return JsonResponse(data)


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')

        if not uploaded_file:
            return JsonResponse({'error': 'No file provided'}, status=400)

        # 保存文件到 MEDIA_ROOT/uploads/
        upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, uploaded_file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        return JsonResponse({
            'message': 'File uploaded successfully',
            'filename': uploaded_file.name,
            'size': uploaded_file.size
        })

    return JsonResponse({'error': 'Only POST method allowed'}, status=405)
