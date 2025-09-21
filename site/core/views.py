from django.shortcuts import render, redirect
from .models import Speaker, ProgramModule
from .forms import ParticipantForm


def main_page(request):
    # Логика для обработки отправленной формы
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в базу
            return redirect('main_page')  # Перезагружаем страницу, чтобы очистить форму
    else:
        # Если страница просто открывается (GET-запрос), создаем пустую форму
        form = ParticipantForm()

    # Получаем все данные для отображения на странице
    speakers = Speaker.objects.all()
    program_modules = ProgramModule.objects.order_by('order')  # Сортируем по полю 'order'

    # Собираем все данные в один "контекст" для передачи в шаблон
    context = {
        'speakers': speakers,
        'program_modules': program_modules,
        'form': form,
    }

    # "Рисуем" HTML-страницу, используя шаблон и наши данные
    return render(request, 'core/index.html', context)