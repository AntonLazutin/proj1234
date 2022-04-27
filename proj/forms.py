from django import forms


class InputName(forms.Form):
    count = 0
    inp_name = forms.CharField(label="Input your name here: ", max_length=50)
