from django import forms
from django.forms import FileInput
    
class UploadFileForm(forms.Form):
    file_field = forms.FileField(widget=FileInput(attrs={'class': 'file_input'}))

        

class dateForm(forms.Form):
    CHOICES = [(1, 'Past Day'), (7, 'Past Week'), (30, 'Past Month'), (365, 'Past Year')]
    date_dropdown = forms.ChoiceField(choices=CHOICES)

class checkForm(forms.Form):
    yearList = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        required=False,
        )

    def __init__(self, userList, *args, **kwargs):
        # self.currList = kwargs.pop('year_list', None)
        super().__init__(*args, **kwargs)
        self.fields['yearList'].choices = [(item, item) for item in userList]

        # if self.currList:
        #     self.fields['yearList'].inital = self.currList

    # choice = []
    # print("Here")
    # print(yearList)

    