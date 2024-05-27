from django import forms


class DateForm(forms.Form):
        date = forms.DateTimeField(validators="%Y-%m-%d")


class TimeForm(forms.Form):
        days = forms.CharField(label="Enter date")
        holidays = forms.CharField()
        outputWorship = forms.CharField()
        month = forms.CharField()
        year = forms.CharField()


