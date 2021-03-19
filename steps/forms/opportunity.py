from django import forms

from ..models import OpportunityAvailable


class OpportunityAvailableForm(forms.ModelForm):
    class Meta:
        model = OpportunityAvailable
        fields = ('full_time', "part_time", 'temporary', 'contract',  'internship', 'seasonal',
                  'co_founder', 'freelance', 'per_diem', 'reserve')

        widgets = {
            "full_time": forms.CheckboxInput(attrs={"class": "form-control js-opportunity"}),
            "part_time": forms.CheckboxInput(attrs={"class": "form-control js-opportunity"}),
            "temporary": forms.CheckboxInput(attrs={"class": "form-control js-opportunity"}),
            "contract": forms.CheckboxInput(attrs={"class": "form-control js-opportunity"}),
            "internship": forms.CheckboxInput(attrs={"class": "form-control js-opportunity"}),
            "seasonal": forms.CheckboxInput(attrs={"class": "form-control js-opportunity"}),
            "co_founder": forms.CheckboxInput(attrs={"class": "form-control js-opportunity"}),
            "freelance": forms.CheckboxInput(attrs={"class": "form-control js-opportunity"}),
            "per_diem": forms.CheckboxInput(attrs={"class": "form-control js-opportunity"}),
            "reserve": forms.CheckboxInput(attrs={"class": "form-control js-opportunity"}),
        }
