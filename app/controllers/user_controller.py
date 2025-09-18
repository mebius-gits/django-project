from ninja import Router
from app.services.user_service import UserService
from app.dtos.user_dto import UserIn, UserOut
from app.dtos.common_dto import CommonResponse
from app.utils.response import api_response

router = Router(tags=["users"])

@router.get("/", response=CommonResponse)
def list_users(request):
    users = UserService.list_users()
    return api_response(200, True, "Users retrieved", [UserOut.from_orm(u) for u in users])

@router.post("/", response=CommonResponse)
def create_user(request, data: UserIn):
    user = UserService.add_user(data.name, data.email)
    return api_response(201, True, "User created", UserOut.from_orm(user))

@router.get("/{user_id}", response=CommonResponse)
def get_user(request, user_id: int):
    user = UserService.get_user(user_id)
    if not user:
        return api_response(404, False, "User not found")
    return api_response(200, True, "User retrieved", UserOut.from_orm(user))
