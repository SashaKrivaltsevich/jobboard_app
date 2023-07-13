from django.urls import path

from .views import (
    index_controller,
    add_company_controller,
    company_list_controller,
    add_vacancy_controller,
)
   


urlpatterns = {
    path("", index_controller, name="index"),
    path("company/add/", add_company_controller, name="add-company"),
    path("company/", company_list_controller, name="company-list"),
    path("vacancy/add/", add_vacancy_controller, name="add-vacancy"),
}