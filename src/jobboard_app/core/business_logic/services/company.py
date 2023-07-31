from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from django.db.models import Count

if TYPE_CHECKING:
    from core.business_logic.dto import AddCompanyDTO

from core.models import Company
from core.business_logic.services.common import replace_file_name_to_uuid, change_file_size

logger = logging.getLogger(__name__)


def create_company(data: AddCompanyDTO) -> None:
    data.logo = replace_file_name_to_uuid(file=data.logo)
    data.logo = change_file_size(file=data.logo)
    Company.objects.create(name=data.name, employees_number=data.employees_number, logo=data.logo)
    logger.info(f"Created file with filename {data.logo.name}")


def get_companies() -> list[Company]:
    companies = Company.objects.annotate(vacancy__count=Count("vacancy__id")).order_by("vacancy__count")
    return list(companies)


def get_company_by_id(company_id: int) -> Company:
    company = Company.objects.annotate(vacancy__count=Count("vacancy__id")).get(pk=company_id)
    logger.info("Succsesfully got company.", extra={"company_id": str(company.id), "company_name": company.name})
    return company

