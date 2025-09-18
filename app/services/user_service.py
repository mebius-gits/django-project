from app.repositories.user_repo import UserRepository

class UserService:
    @staticmethod
    def list_users():
        return UserRepository.get_all_users()

    @staticmethod
    def add_user(name: str, email: str):
        return UserRepository.create_user(name, email)

    @staticmethod
    def get_user(user_id: int):
        try:
            return UserRepository.get_user_by_id(user_id)
        except:
            return None
