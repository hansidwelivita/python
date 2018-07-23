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


class V1beta1PolicyRule(object):
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
        'api_groups': 'list[str]',
        'non_resource_ur_ls': 'list[str]',
        'resource_names': 'list[str]',
        'resources': 'list[str]',
        'verbs': 'list[str]'
    }

    attribute_map = {
        'api_groups': 'apiGroups',
        'non_resource_ur_ls': 'nonResourceURLs',
        'resource_names': 'resourceNames',
        'resources': 'resources',
        'verbs': 'verbs'
    }

    def __init__(self, api_groups=None, non_resource_ur_ls=None, resource_names=None, resources=None, verbs=None):
        """
        V1beta1PolicyRule - a model defined in Swagger
        """

        self._api_groups = None
        self._non_resource_ur_ls = None
        self._resource_names = None
        self._resources = None
        self._verbs = None
        self.discriminator = None

        if api_groups is not None:
          self.api_groups = api_groups
        if non_resource_ur_ls is not None:
          self.non_resource_ur_ls = non_resource_ur_ls
        if resource_names is not None:
          self.resource_names = resource_names
        if resources is not None:
          self.resources = resources
        self.verbs = verbs

    @property
    def api_groups(self):
        """
        Gets the api_groups of this V1beta1PolicyRule.
        APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.

        :return: The api_groups of this V1beta1PolicyRule.
        :rtype: list[str]
        """
        return self._api_groups

    @api_groups.setter
    def api_groups(self, api_groups):
        """
        Sets the api_groups of this V1beta1PolicyRule.
        APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.

        :param api_groups: The api_groups of this V1beta1PolicyRule.
        :type: list[str]
        """

        self._api_groups = api_groups

    @property
    def non_resource_ur_ls(self):
        """
        Gets the non_resource_ur_ls of this V1beta1PolicyRule.
        NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as \"pods\" or \"secrets\") or non-resource URL paths (such as \"/api\"),  but not both.

        :return: The non_resource_ur_ls of this V1beta1PolicyRule.
        :rtype: list[str]
        """
        return self._non_resource_ur_ls

    @non_resource_ur_ls.setter
    def non_resource_ur_ls(self, non_resource_ur_ls):
        """
        Sets the non_resource_ur_ls of this V1beta1PolicyRule.
        NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as \"pods\" or \"secrets\") or non-resource URL paths (such as \"/api\"),  but not both.

        :param non_resource_ur_ls: The non_resource_ur_ls of this V1beta1PolicyRule.
        :type: list[str]
        """

        self._non_resource_ur_ls = non_resource_ur_ls

    @property
    def resource_names(self):
        """
        Gets the resource_names of this V1beta1PolicyRule.
        ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.

        :return: The resource_names of this V1beta1PolicyRule.
        :rtype: list[str]
        """
        return self._resource_names

    @resource_names.setter
    def resource_names(self, resource_names):
        """
        Sets the resource_names of this V1beta1PolicyRule.
        ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.

        :param resource_names: The resource_names of this V1beta1PolicyRule.
        :type: list[str]
        """

        self._resource_names = resource_names

    @property
    def resources(self):
        """
        Gets the resources of this V1beta1PolicyRule.
        Resources is a list of resources this rule applies to.  '*' represents all resources in the specified apiGroups. '*/foo' represents the subresource 'foo' for all resources in the specified apiGroups.

        :return: The resources of this V1beta1PolicyRule.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this V1beta1PolicyRule.
        Resources is a list of resources this rule applies to.  '*' represents all resources in the specified apiGroups. '*/foo' represents the subresource 'foo' for all resources in the specified apiGroups.

        :param resources: The resources of this V1beta1PolicyRule.
        :type: list[str]
        """

        self._resources = resources

    @property
    def verbs(self):
        """
        Gets the verbs of this V1beta1PolicyRule.
        Verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rule.  VerbAll represents all kinds.

        :return: The verbs of this V1beta1PolicyRule.
        :rtype: list[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs):
        """
        Sets the verbs of this V1beta1PolicyRule.
        Verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rule.  VerbAll represents all kinds.

        :param verbs: The verbs of this V1beta1PolicyRule.
        :type: list[str]
        """
        if verbs is None:
            raise ValueError("Invalid value for `verbs`, must not be `None`")

        self._verbs = verbs

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
        if not isinstance(other, V1beta1PolicyRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
