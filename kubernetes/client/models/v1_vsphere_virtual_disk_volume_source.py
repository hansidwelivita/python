# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1-660c2a2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1VsphereVirtualDiskVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, fs_type=None, volume_path=None):
        """
        V1VsphereVirtualDiskVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'fs_type': 'str',
            'volume_path': 'str'
        }

        self.attribute_map = {
            'fs_type': 'fsType',
            'volume_path': 'volumePath'
        }

        self._fs_type = fs_type
        self._volume_path = volume_path

    @property
    def fs_type(self):
        """
        Gets the fs_type of this V1VsphereVirtualDiskVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.

        :return: The fs_type of this V1VsphereVirtualDiskVolumeSource.
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """
        Sets the fs_type of this V1VsphereVirtualDiskVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.

        :param fs_type: The fs_type of this V1VsphereVirtualDiskVolumeSource.
        :type: str
        """

        self._fs_type = fs_type

    @property
    def volume_path(self):
        """
        Gets the volume_path of this V1VsphereVirtualDiskVolumeSource.
        Path that identifies vSphere volume vmdk

        :return: The volume_path of this V1VsphereVirtualDiskVolumeSource.
        :rtype: str
        """
        return self._volume_path

    @volume_path.setter
    def volume_path(self, volume_path):
        """
        Sets the volume_path of this V1VsphereVirtualDiskVolumeSource.
        Path that identifies vSphere volume vmdk

        :param volume_path: The volume_path of this V1VsphereVirtualDiskVolumeSource.
        :type: str
        """
        if volume_path is None:
            raise ValueError("Invalid value for `volume_path`, must not be `None`")

        self._volume_path = volume_path

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
