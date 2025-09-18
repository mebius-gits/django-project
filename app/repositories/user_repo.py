from app.models.user import User

class UserRepository:
    @staticmethod
    def get_all_users():
        return User.objects.all()

    @staticmethod
    def create_user(name: str, email: str):
        return User.objects.create(name=name, email=email)

    @staticmethod
    def get_user_by_id(user_id: int):
        return User.objects.get(id=user_id)