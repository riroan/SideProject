from abc import ABCMeta, abstractmethod
from typing import Generic, List, TypeVar, Union

from sqlalchemy.orm import Session

T = TypeVar("T")


class Repository(Generic[T], metaclass=ABCMeta):
    def __init__(self, session: Session):
        self.session = session

    @property
    @abstractmethod
    def entity(self) -> T:
        pass

    def get_by_id(self, id: Union[int, str]) -> T:
        return self.session.query(self.entity).filter(self.entity.id == id).first()

    def save(self, **kwargs):
        obj = self.entity(**kwargs)
        self.save_obj(obj)

    def save_obj(self, obj: T):
        self.session.add(obj)

    def delete_by_id(self, id: Union[int, str]):
        self.session.query(self.entity).filter(self.entity.id == id).delete()

    def get_all(self) -> List[T]:
        return self.session.query(self.entity).all()

    def update_by_id(self, id: Union[int, str], **kwargs):
        self.session.query(self.entity).filter(self.entity.id == id).update(kwargs)
