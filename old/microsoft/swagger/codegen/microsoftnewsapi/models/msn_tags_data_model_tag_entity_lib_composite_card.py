# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MsnTagsDataModelTagEntityLibCompositeCard(Model):
    """MsnTagsDataModelTagEntityLibCompositeCard.

    :param next_page_url: Get or set the Fetchable NextPageUrl of the Card
     Content
    :type next_page_url: str
    :param sub_cards:
    :type sub_cards: list[object]
    :param metadata: Get or set the dictionary of Metadata.
    :type metadata: dict[str,
     list[~microsoft.swagger.codegen.microsoftnewsapi.models.MsnTagsDataModelTagEntityLibMetadata]]
    :param title: Get or set the EntityName of the Actionable
    :type title: str
    :param type: Get or set the Type of the Card.
     Please use ContentTypes for this property although we don't use a strong
     name for easier backward compatibilty for future extension.
    :type type: str
    :param url: Get or set the Clickable Url of the Card
    :type url: str
    :param data_url: Get or set the Fetchable Data Url of the Card Content
    :type data_url: str
    :param locale: Gets or sets Locale of the Card (optional) for extra
     information purpose.
    :type locale: str
    :param created_date_time: Get or set the CreateDate of the entity
    :type created_date_time: str
    :param updated_date_time: Get or set the ModifiedDate of the entity
    :type updated_date_time: str
    :param deleted: Get or set whether the entity is Deleted
    :type deleted: bool
    :param _et: Get or set the extended type
    :type _et: str
    :param id:
    :type id: str
    :param _t:
    :type _t: str
    """

    _attribute_map = {
        'next_page_url': {'key': 'nextPageUrl', 'type': 'str'},
        'sub_cards': {'key': 'subCards', 'type': '[object]'},
        'metadata': {'key': 'metadata', 'type': '{[MsnTagsDataModelTagEntityLibMetadata]}'},
        'title': {'key': 'title', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'data_url': {'key': 'dataUrl', 'type': 'str'},
        'locale': {'key': 'locale', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'str'},
        'updated_date_time': {'key': 'updatedDateTime', 'type': 'str'},
        'deleted': {'key': 'deleted', 'type': 'bool'},
        '_et': {'key': '_et', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        '_t': {'key': '_t', 'type': 'str'},
    }

    def __init__(self, next_page_url=None, sub_cards=None, metadata=None, title=None, type=None, url=None, data_url=None, locale=None, created_date_time=None, updated_date_time=None, deleted=None, _et=None, id=None, _t=None):
        super(MsnTagsDataModelTagEntityLibCompositeCard, self).__init__()
        self.next_page_url = next_page_url
        self.sub_cards = sub_cards
        self.metadata = metadata
        self.title = title
        self.type = type
        self.url = url
        self.data_url = data_url
        self.locale = locale
        self.created_date_time = created_date_time
        self.updated_date_time = updated_date_time
        self.deleted = deleted
        self._et = _et
        self.id = id
        self._t = _t
