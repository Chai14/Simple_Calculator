from django import forms

operator_choices = [("1", "+"), ("2", "-"), ("3", "*"), ("4", "/")]

class calculator(forms.Form):
    num1 = forms.CharField(label="Value 1", widget=forms.TextInput(attrs={'class': "form-control"}))
    num2 = forms.CharField(label="Value 2", widget=forms.TextInput(attrs={'class': "form-control"}))
    opr = forms.ChoiceField(label="Operation", choices=operator_choices, widget=forms.Select(attrs={'class': "form-control"}))

