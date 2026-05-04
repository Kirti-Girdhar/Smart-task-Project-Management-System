from django import forms
from django.utils import timezone
from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date', 'project', 'assigned_to']
    # cleared_data() - means it convert the input from the user into python data types
    #  such as text to string, IntegerField to int, DateField to datetime.date object,etc.
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date < timezone.now():
            raise forms.ValidationError("Due date must be a future date.")
        return due_date