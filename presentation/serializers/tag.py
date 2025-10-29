from domain.models.tag import TagResponseModel

class TagMapper:

    def to_api_response(self, tag):
        return TagResponseModel(
            id=tag.id,
            name=tag.name
        )