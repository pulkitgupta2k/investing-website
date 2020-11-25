# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MsnTagsDataModelTagEntityLibArtifactDataVideoMetadata(Model):
    """MsnTagsDataModelTagEntityLibArtifactDataVideoMetadata.

    :param play_time: Gets or sets the play time.
    :type play_time: int
    :param closed_captions: Gets or sets the closed captions.
    :type closed_captions:
     list[~microsoft.swagger.codegen.microsoftnewsapi.models.MsnTagsDataModelTagEntityLibArtifactDataCloseCaption]
    :param external_video_files: Gets or sets the external video files.
    :type external_video_files:
     list[~microsoft.swagger.codegen.microsoftnewsapi.models.MsnTagsDataModelTagEntityLibArtifactDataExternalVideoFile]
    """

    _attribute_map = {
        'play_time': {'key': 'playTime', 'type': 'int'},
        'closed_captions': {'key': 'closedCaptions', 'type': '[MsnTagsDataModelTagEntityLibArtifactDataCloseCaption]'},
        'external_video_files': {'key': 'externalVideoFiles', 'type': '[MsnTagsDataModelTagEntityLibArtifactDataExternalVideoFile]'},
    }

    def __init__(self, play_time=None, closed_captions=None, external_video_files=None):
        super(MsnTagsDataModelTagEntityLibArtifactDataVideoMetadata, self).__init__()
        self.play_time = play_time
        self.closed_captions = closed_captions
        self.external_video_files = external_video_files
