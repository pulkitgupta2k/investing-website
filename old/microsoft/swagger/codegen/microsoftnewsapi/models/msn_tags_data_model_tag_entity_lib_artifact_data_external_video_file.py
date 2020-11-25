# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MsnTagsDataModelTagEntityLibArtifactDataExternalVideoFile(Model):
    """MsnTagsDataModelTagEntityLibArtifactDataExternalVideoFile.

    :param url: Gets or sets Url
    :type url: str
    :param width: Gets or sets the width.
    :type width: int
    :param height: Gets or sets the height.
    :type height: int
    :param content_type: Gets or sets the content type.
    :type content_type: str
    :param file_size: Gets or sets the file size.
    :type file_size: int
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'width': {'key': 'width', 'type': 'int'},
        'height': {'key': 'height', 'type': 'int'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'file_size': {'key': 'fileSize', 'type': 'int'},
    }

    def __init__(self, url=None, width=None, height=None, content_type=None, file_size=None):
        super(MsnTagsDataModelTagEntityLibArtifactDataExternalVideoFile, self).__init__()
        self.url = url
        self.width = width
        self.height = height
        self.content_type = content_type
        self.file_size = file_size