from __future__ import annotations

import logging
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.contrib.auth.models import User
    from core.business_logic.dto import RegistrationDTO

logger = logging.getLogger(__name__)


def create_user(data: RegistrationDTO) -> None:
    logger.info("Get user creation request. ", extra={"user": str(data)})   

    user_model: User = get_user_model()
    created_user = user_model.objects.create_user(
        username=data.username,
        password=data.password,
        email=data.email,
        is_active = False
    )

    group = Group.objects.get(name=data.role)

    created_user.groups.add(group)