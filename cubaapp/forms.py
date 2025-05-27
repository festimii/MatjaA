from django import forms

class UploadExcelForm(forms.Form):
    file = forms.FileField(
        label="Select an Excel file",
        help_text="Max. 10 MB",
        widget=forms.ClearableFileInput(attrs={'accept': '.xls,.xlsx'})
    )

