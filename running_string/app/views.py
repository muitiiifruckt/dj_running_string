# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import VideoForm
from .main_func import create_scrolling_text_video
import os
from .models import VideoRequest  # Импортируйте модель

def create_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            output_file = f'scrolling_text_{text}.mp4'

            # Создаем видео
            create_scrolling_text_video(text, output_file=output_file)

            # Сохраняем запрос в базе данных
            video_request = VideoRequest(text=text, output_file=output_file)
            video_request.save()

            # Открываем файл для чтения в бинарном режиме
            with open(output_file, 'rb') as f:
                response = HttpResponse(f.read(), content_type='video/mp4')
                response['Content-Disposition'] = f'attachment; filename="{output_file}"'

            # Удаляем файл с сервера после отправки клиенту
            os.remove(output_file)

            return response
    else:
        form = VideoForm()

    return render(request, 'create_video.html', {'form': form})
