from __future__ import annotations
from django.http import (
    HttpResponse, 
    HttpResponseBadRequest, 
    HttpResponseRedirect
)
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.urls import reverse

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from django.http import HttpRequest

from .services import (
    CompanyStorage, 
    VacancyStorage,
    Vacancy,
    Company
    )   


company_storage = CompanyStorage()
vacancy_storage = VacancyStorage(company_storage=company_storage)

@require_http_methods(request_method_list=["GET"])
def index_controller(request: HttpRequest) -> HttpResponse:
    vacancies = vacancy_storage.get_all_vacancies()
    context ={"vacancies": vacancies}
    return render(request=request, template_name="index.html", context=context)


@require_http_methods(request_method_list=["GET", "POST"])
def add_company_controller(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request=request, template_name="add_company.html")
    
    elif request.method == "POST":
        name = request.POST["name"]
        employees_number = request.POST["employees_number"]

        company = Company(
            name=name,
            employees_number=employees_number
        )
        company_storage.add_company(company_to_add=company)
        return HttpResponseRedirect(redirect_to=reverse("company-list"))
    

@require_http_methods(request_method_list=["GET"])
def company_list_controller(request: HttpRequest) -> HttpResponse:
    companies=company_storage.get_all_companies()
    print(companies)
    context = {"companies": companies}
    return render(request=request, template_name="company_list.html", context=context)
    
       
def add_vacancy_controller(request:HttpRequest) -> HttpResponse:
    if request.method == "GET":
        
        return render(request=request, template_name="add_vacancy.html")
    elif request.method == "POST":
        name = request.POST["name"]
        company_name = request.POST["company_name"]
        level = request.POST["level"]
        expirience = request.POST["expirience"]
        min_salary = request.POST["min_salary"]
        max_salary = request.POST["max_salary"]

        if min_salary == '':
            min_salary = None
        else:
            min_salary = int(min_salary) 

        if max_salary == '':
            max_salary = None
        else:
            max_salary = int(max_salary)        

        vacancy =Vacancy(
            name=name,
            company_name=company_name,
            level=level,
            expirience=expirience,
            min_salary=min_salary,
            max_salary=max_salary
        )
        vacancy_storage.add_vacancyy(vacancy_to_add=vacancy)
        return HttpResponseRedirect(redirect_to="index")