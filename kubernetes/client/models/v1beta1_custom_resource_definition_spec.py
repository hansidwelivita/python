# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.11.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1CustomResourceDefinitionSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'additional_printer_columns': 'list[V1beta1CustomResourceColumnDefinition]',
        'group': 'str',
        'names': 'V1beta1CustomResourceDefinitionNames',
        'scope': 'str',
        'subresources': 'V1beta1CustomResourceSubresources',
        'validation': 'V1beta1CustomResourceValidation',
        'version': 'str',
        'versions': 'list[V1beta1CustomResourceDefinitionVersion]'
    }

    attribute_map = {
        'additional_printer_columns': 'additionalPrinterColumns',
        'group': 'group',
        'names': 'names',
        'scope': 'scope',
        'subresources': 'subresources',
        'validation': 'validation',
        'version': 'version',
        'versions': 'versions'
    }

    def __init__(self, additional_printer_columns=None, group=None, names=None, scope=None, subresources=None, validation=None, version=None, versions=None):
        """
        V1beta1CustomResourceDefinitionSpec - a model defined in Swagger
        """

        self._additional_printer_columns = None
        self._group = None
        self._names = None
        self._scope = None
        self._subresources = None
        self._validation = None
        self._version = None
        self._versions = None
        self.discriminator = None

        if additional_printer_columns is not None:
          self.additional_printer_columns = additional_printer_columns
        self.group = group
        self.names = names
        self.scope = scope
        if subresources is not None:
          self.subresources = subresources
        if validation is not None:
          self.validation = validation
        if version is not None:
          self.version = version
        if versions is not None:
          self.versions = versions

    @property
    def additional_printer_columns(self):
        """
        Gets the additional_printer_columns of this V1beta1CustomResourceDefinitionSpec.
        AdditionalPrinterColumns are additional columns shown e.g. in kubectl next to the name. Defaults to a created-at column.

        :return: The additional_printer_columns of this V1beta1CustomResourceDefinitionSpec.
        :rtype: list[V1beta1CustomResourceColumnDefinition]
        """
        return self._additional_printer_columns

    @additional_printer_columns.setter
    def additional_printer_columns(self, additional_printer_columns):
        """
        Sets the additional_printer_columns of this V1beta1CustomResourceDefinitionSpec.
        AdditionalPrinterColumns are additional columns shown e.g. in kubectl next to the name. Defaults to a created-at column.

        :param additional_printer_columns: The additional_printer_columns of this V1beta1CustomResourceDefinitionSpec.
        :type: list[V1beta1CustomResourceColumnDefinition]
        """

        self._additional_printer_columns = additional_printer_columns

    @property
    def group(self):
        """
        Gets the group of this V1beta1CustomResourceDefinitionSpec.
        Group is the group this resource belongs in

        :return: The group of this V1beta1CustomResourceDefinitionSpec.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this V1beta1CustomResourceDefinitionSpec.
        Group is the group this resource belongs in

        :param group: The group of this V1beta1CustomResourceDefinitionSpec.
        :type: str
        """
        if group is None:
            raise ValueError("Invalid value for `group`, must not be `None`")

        self._group = group

    @property
    def names(self):
        """
        Gets the names of this V1beta1CustomResourceDefinitionSpec.
        Names are the names used to describe this custom resource

        :return: The names of this V1beta1CustomResourceDefinitionSpec.
        :rtype: V1beta1CustomResourceDefinitionNames
        """
        return self._names

    @names.setter
    def names(self, names):
        """
        Sets the names of this V1beta1CustomResourceDefinitionSpec.
        Names are the names used to describe this custom resource

        :param names: The names of this V1beta1CustomResourceDefinitionSpec.
        :type: V1beta1CustomResourceDefinitionNames
        """
        if names is None:
            raise ValueError("Invalid value for `names`, must not be `None`")

        self._names = names

    @property
    def scope(self):
        """
        Gets the scope of this V1beta1CustomResourceDefinitionSpec.
        Scope indicates whether this resource is cluster or namespace scoped.  Default is namespaced

        :return: The scope of this V1beta1CustomResourceDefinitionSpec.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this V1beta1CustomResourceDefinitionSpec.
        Scope indicates whether this resource is cluster or namespace scoped.  Default is namespaced

        :param scope: The scope of this V1beta1CustomResourceDefinitionSpec.
        :type: str
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")

        self._scope = scope

    @property
    def subresources(self):
        """
        Gets the subresources of this V1beta1CustomResourceDefinitionSpec.
        Subresources describes the subresources for CustomResources

        :return: The subresources of this V1beta1CustomResourceDefinitionSpec.
        :rtype: V1beta1CustomResourceSubresources
        """
        return self._subresources

    @subresources.setter
    def subresources(self, subresources):
        """
        Sets the subresources of this V1beta1CustomResourceDefinitionSpec.
        Subresources describes the subresources for CustomResources

        :param subresources: The subresources of this V1beta1CustomResourceDefinitionSpec.
        :type: V1beta1CustomResourceSubresources
        """

        self._subresources = subresources

    @property
    def validation(self):
        """
        Gets the validation of this V1beta1CustomResourceDefinitionSpec.
        Validation describes the validation methods for CustomResources

        :return: The validation of this V1beta1CustomResourceDefinitionSpec.
        :rtype: V1beta1CustomResourceValidation
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        """
        Sets the validation of this V1beta1CustomResourceDefinitionSpec.
        Validation describes the validation methods for CustomResources

        :param validation: The validation of this V1beta1CustomResourceDefinitionSpec.
        :type: V1beta1CustomResourceValidation
        """

        self._validation = validation

    @property
    def version(self):
        """
        Gets the version of this V1beta1CustomResourceDefinitionSpec.
        Version is the version this resource belongs in Should be always first item in Versions field if provided. Optional, but at least one of Version or Versions must be set. Deprecated: Please use `Versions`.

        :return: The version of this V1beta1CustomResourceDefinitionSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this V1beta1CustomResourceDefinitionSpec.
        Version is the version this resource belongs in Should be always first item in Versions field if provided. Optional, but at least one of Version or Versions must be set. Deprecated: Please use `Versions`.

        :param version: The version of this V1beta1CustomResourceDefinitionSpec.
        :type: str
        """

        self._version = version

    @property
    def versions(self):
        """
        Gets the versions of this V1beta1CustomResourceDefinitionSpec.
        Versions is the list of all supported versions for this resource. If Version field is provided, this field is optional. Validation: All versions must use the same validation schema for now. i.e., top level Validation field is applied to all of these versions. Order: The version name will be used to compute the order. If the version string is \"kube-like\", it will sort above non \"kube-like\" version strings, which are ordered lexicographically. \"Kube-like\" versions start with a \"v\", then are followed by a number (the major version), then optionally the string \"alpha\" or \"beta\" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.

        :return: The versions of this V1beta1CustomResourceDefinitionSpec.
        :rtype: list[V1beta1CustomResourceDefinitionVersion]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """
        Sets the versions of this V1beta1CustomResourceDefinitionSpec.
        Versions is the list of all supported versions for this resource. If Version field is provided, this field is optional. Validation: All versions must use the same validation schema for now. i.e., top level Validation field is applied to all of these versions. Order: The version name will be used to compute the order. If the version string is \"kube-like\", it will sort above non \"kube-like\" version strings, which are ordered lexicographically. \"Kube-like\" versions start with a \"v\", then are followed by a number (the major version), then optionally the string \"alpha\" or \"beta\" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.

        :param versions: The versions of this V1beta1CustomResourceDefinitionSpec.
        :type: list[V1beta1CustomResourceDefinitionVersion]
        """

        self._versions = versions

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
        if not isinstance(other, V1beta1CustomResourceDefinitionSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
