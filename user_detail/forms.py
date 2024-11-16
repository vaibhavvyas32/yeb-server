from django import forms
from .models import UserDetail

class MarksForm(forms.ModelForm):
    marks_8th = forms.FloatField(label="8th Grade Marks")
    marks_9th = forms.FloatField(label="9th Grade Marks")
    marks_10th = forms.FloatField(label="10th Grade Marks")
    marks_11th = forms.FloatField(label="11th Grade Marks")

    class Meta:
        model = UserDetail
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        # Collect marks and convert them to JSON format
        marks = {
            "8th": cleaned_data.get('marks_8th'),
            "9th": cleaned_data.get('marks_9th'),
            "10th": cleaned_data.get('marks_10th'),
            "11th": cleaned_data.get('marks_11th')
        }
        # Set the 'marks' field in the model
        self.instance.marks = marks
        return cleaned_data