from __future__ import annotations

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.http import HttpRequest

from core.presentation.forms import RegistrationForm
from core.business_logic.dto import RegistrationDTO
from core.presentation.converters import convert_data_from_form_to_dto
from core.business_logic.services import create_user

@require_http_methods(["GET", "POST"])
def registration_controller(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = RegistrationForm()
        context = {"form": form}
        return render(request=request, template_name="signin.html", context=context)
    
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = convert_data_from_form_to_dto(dto=RegistrationDTO, data_from_form=form.cleaned_data)
            create_user(data=data)
            return redirect(to="index")

