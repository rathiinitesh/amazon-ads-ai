from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    email: str
    full_name: str


class UserCreateResponse(BaseModel):
    user_id: int
    email: str
    full_name: str
    created_at: str


class UserUpdateRequest(BaseModel):
    user_id: int = None
    email: str = None
    full_name: str = None


class UserUpdateResponse(BaseModel):
    user_id: int
    email: str
    full_name: str
    created_at: str
