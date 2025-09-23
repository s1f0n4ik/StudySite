from django.shortcuts import render, redirect
from .models import Speaker, ProgramModule, SiteSettings  # <-- Добавили
from .forms import ParticipantForm


def main_page(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = ParticipantForm()

    speakers = Speaker.objects.all()
    program_modules = ProgramModule.objects.order_by('order')

    # Получаем первую (и единственную) запись с настройками
    site_settings = SiteSettings.objects.first()

    context = {
        'speakers': speakers,
        'program_modules': program_modules,
        'form': form,
        'settings': site_settings,  # <-- Передаем настройки в контекст
    }

    return render(request, 'core/index.html', context)