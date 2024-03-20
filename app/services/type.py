from app.model.repository.type import TypeRepository
from app.utils.utils import createSuccessResponse


class TypeService:

    @classmethod
    def getTypes(cls):
        types = TypeRepository.getTypes()
        return createSuccessResponse([type.toJSON() for type in types])