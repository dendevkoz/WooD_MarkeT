from django import forms

class NameForm(forms.Form):
    sender = forms.EmailField(label='E-mail')
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Введите сообщение', widget=forms.Textarea)
    first_name = forms.CharField(label='Ваше имя', max_length=100)
