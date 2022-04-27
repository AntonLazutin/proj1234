from django import forms


class InputName(forms.Form):
    inp_name = forms.CharField(label="Input your name here: ", max_length=50)
