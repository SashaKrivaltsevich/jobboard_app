from core.presentation.validators import validate_swear_words_in_company_name, ValidateMaxTagCount, ValidatorFileExtension, ValidateFileSize
from django import forms
from core.models import Level


LEVELS = [(level.name, level.name) for level in Level.objects.all()]

class AddVacancyForm(forms.Form):
    name = forms.CharField(label="Name", max_length=30, strip=True)
    company_name = forms.CharField(label="Company", max_length=30, strip=True)
    level = forms.ChoiceField(label="Level", choices=LEVELS)
    expirience = forms.CharField(label="Expirience", max_length=30, strip=True)
    min_salary = forms.IntegerField(label="Min Salary", min_value=0, required=False)
    max_salary = forms.IntegerField(label="Max Salary", min_value=0, required=False)
    attachment = forms.FileField(
        label="Attachment", 
        allow_empty_file=False,
        validators=[ValidatorFileExtension(["pdf"]), ValidateFileSize(max_size=5_000_000)]
        )
    tags = forms.CharField(label="Tags", widget=forms.Textarea, validators=[ValidateMaxTagCount(max_count=5)])


class SearchVacancyForm(forms.Form):
    template_name = "search_form_snippet.html"

    name = forms.CharField(label="Position", max_length=30, strip=True, required=False)
    company_name = forms.CharField(label="Company", max_length=30, strip=True, required=False)
    level = forms.ChoiceField(label="Level", choices=[("", "ALL")] + LEVELS, required=False)
    expirience = forms.CharField(label="Expirience", max_length=30, strip=True, required=False)
    min_salary = forms.IntegerField(label="Min Salary", min_value=0, required=False)
    max_salary = forms.IntegerField(label="Max Salary", min_value=0, required=False)
    tag = forms.CharField(label="Tag", required=False)