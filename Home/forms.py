from django.forms import ModelForm
from .models import RegUser


class RegForm(ModelForm):
    class Meta:
        model = RegUser
        fields = ['name', 'branch', 'semester',
                  'course', 'gender', 'email', 'WNumber']