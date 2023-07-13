from dataclasses import dataclass


@dataclass
class Vacancy:
    name: str
    compony: str
    level: str
    expirience: str
    min_salary: int | None
    max_salary: int | None
    id: int | None = None


@dataclass
class Company:
    name: str
    employees_number: int
    vacancies_counter: int = 0
    id: int | None = None


class CompanyDuplicateNameError(Exception):
    ...


class CompanyNotExistError(Exception):
    ...

class BaseStorage:
    ID_COUNT = 0

    def update_couner(self) -> int:
        self.ID_COUNT += 1
        return self.ID_COUNT


class CompanyStorage(BaseStorage):
    def __init__(self) -> None:
        self._companies: list[Company] = [] 


    def _validate_company(self, company_to_add:Company) -> None:
        for company in self._companies:
            if company.name.lower() == company_to_add.lower():
                raise CompanyDuplicateNameError

    def add_company(self, company_to_add: Company) -> None:
        self._validate_company(company_to_add=company_to_add)
        primary_key =self.update_couner()
        company_to_add.id = primary_key
        self._companies.append(company_to_add)

    def get_all_companies(self) -> list[Company]:
        return self._companies
    
    def  get_company_by_name(self, company_name) -> Company | None:
        for company in self._companies:
            if company.name.lower() == company_name.lower():
                return company


class VacancyStorage(BaseStorage):
    def __init__(self, company_storage: CompanyStorage) -> None:
        self._vacancies: list[Company] = []   
        self._company_storage = company_storage

    
    def add_vacancyy(self, vacancy_to_add: Vacancy) -> None:
        company = self._company_storage.get_company_by_name(company_name=vacancy_to_add.company)
        if not company:
            raise CompanyNotExistError
        
        primary_key = self.update_couner()
        vacancy_to_add.id = primary_key
        self._vacancies.append(vacancy_to_add)
        company.vacancies_counter += 1

    def get_all_companies(self) -> list[Company]:
        return self._vacancies