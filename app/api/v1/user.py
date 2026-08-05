from fastapi import APIRouter

from app.models import (
    UserCreateRequest,
    UserCreateResponse,
    UserUpdateRequest,
    UserUpdateResponse,
)

from .utils import create_user, update_user

router = APIRouter()


@router.post("/user/create")
async def user_create(request: UserCreateRequest) -> UserCreateResponse:
    user = create_user(email=request.email, full_name=request.full_name)
    return UserCreateResponse(
        user_id=user.user_id,
        email=user.email,
        full_name=user.full_name,
        created_at=str(user.created_at),
    )


@router.post("/user/update")
async def user_update(request: UserUpdateRequest) -> UserUpdateResponse:
    user = update_user(
        user_id=request.user_id, email=request.email, full_name=request.full_name
    )
    return UserUpdateResponse(
        user_id=user.user_id,
        email=user.email,
        full_name=user.full_name,
        created_at=str(user.created_at),
    )
