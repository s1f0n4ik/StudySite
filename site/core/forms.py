from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Проходимся по всем полям формы и добавляем им CSS-класс
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Participant
        fields = ['full_name', 'university', 'faculty', 'course', 'email']
        # Указываем, какие подписи должны быть у полей
        labels = {
            'full_name': 'ФИО',
            'university': 'Университет',
            'faculty': 'Факультет',
            'course': 'Курс обучения',
            'email': 'Электронная почта',
        }