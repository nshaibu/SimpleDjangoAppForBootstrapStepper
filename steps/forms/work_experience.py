from django import forms

from ..models import WorkExperience


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ('title', "company_name", "date_started", "working_here", "date_ended",
                  "skills_used", "describe_accomplishment")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control js-work-experience"}),
            "company_name": forms.TextInput(attrs={"class": "form-control js-work-experience"}),
            "working_here": forms.CheckboxInput(attrs={"class": "form-control js-work-experience"}),
            "date_started": forms.DateInput(attrs={"class": "form-control js-work-experience"}),
            "date_ended": forms.DateInput(attrs={"class": "form-control js-work-experience"}),
            "skills_used": forms.TextInput(attrs={"class": "form-control js-work-experience"}),
            "describe_accomplishment": forms.Textarea(attrs={"class": "form-control js-work-experience"}),
        }

        labels = {
            "working_here": "I currently work here",
            "skills_used": "What skills and technologies did you use?",
            "describe_accomplishment": "Describe your accomplishments",
        }
