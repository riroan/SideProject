from model.user import User
from repository.base import Repository


class UserRepository(Repository[User]):
    entity = User
