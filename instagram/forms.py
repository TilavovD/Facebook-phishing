from django import forms

from instagram.models import InstaUser


class InstaUSerForm(forms.ModelForm):
    class Meta:
        model = InstaUser
        fields = "__all__"