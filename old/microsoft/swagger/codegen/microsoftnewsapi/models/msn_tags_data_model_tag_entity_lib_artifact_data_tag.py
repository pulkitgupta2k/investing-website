# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MsnTagsDataModelTagEntityLibArtifactDataTag(Model):
    """MsnTagsDataModelTagEntityLibArtifactDataTag.

    :param label: Gets or sets Label
    :type label: str
    :param weight: Gets or sets Weight
    :type weight: float
    :param feed_id: Gets or sets FeedId
    :type feed_id: str
    :param locale: Gets or sets the locale.
    :type locale: str
    """

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'weight': {'key': 'weight', 'type': 'float'},
        'feed_id': {'key': 'feedId', 'type': 'str'},
        'locale': {'key': 'locale', 'type': 'str'},
    }

    def __init__(self, label=None, weight=None, feed_id=None, locale=None):
        super(MsnTagsDataModelTagEntityLibArtifactDataTag, self).__init__()
        self.label = label
        self.weight = weight
        self.feed_id = feed_id
        self.locale = locale