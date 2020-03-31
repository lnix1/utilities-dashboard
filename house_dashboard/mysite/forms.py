from django import forms
    
class UpdateUtilitiesForm(forms.Form):
    utility_type = forms.CharField(help_text="Enter the relevant utility.")
    date= models.DateField()
    amount= models.FloatField()