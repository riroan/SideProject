from model.user import User
from repository.base import Repository


class UserRepository(Repository[User]):
    entity = User

    def get_by_email(self, email: str) -> User:
        return self.session.query(self.entity).filter(User.email == email).first()
