from django import forms

class NewTask(forms.Form):
    
    title = forms.CharField(label='Task title', max_length=50, required=True)
    content = forms.CharField(label='Task description', widget=forms.Textarea(), required=False)
    completed = forms.BooleanField(label='Task completed', required=False)