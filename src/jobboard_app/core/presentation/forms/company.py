from core.presentation.validators import validate_swear_words_in_company_name, ValidateFileSize, ValidatorFileExtension
from django import forms


class AddCompanyForm(forms.Form):
    name = forms.CharField(label="Company", max_length=30, strip=True, validators=[validate_swear_words_in_company_name])
    employees_number = forms.IntegerField(label="Employees", min_value=1)
    logo = forms.ImageField(
        label="Logo",
        allow_empty_file=False,
        validators=[ValidatorFileExtension(["png", "jpg", "jpeg"]), ValidateFileSize(max_size=5_000_000)]
    )
