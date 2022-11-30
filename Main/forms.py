from django import forms

from django.forms import ModelForm

from .models import Task, CompletedTask


class FromTask(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'home', 'problem', 'comment', 'phone', 'email']
        labels = {
            'name': 'Введите имя',
            'home': 'Выбрать дом',
            'problem': 'Выбрать проблему',
            'comment': 'Добавьте описание',
            'phone': 'Введите телефон',
            'email': 'Введите email'
        }


class FormCompletedTask(ModelForm):
    class Meta:
        model = CompletedTask
        fields = ['video', 'comment']
        labels = {
            'video': 'Загрузить видео',
            'comment': 'Оставьте коментарий'
        }