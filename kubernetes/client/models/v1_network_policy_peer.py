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


class V1NetworkPolicyPeer(object):
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
        'ip_block': 'V1IPBlock',
        'namespace_selector': 'V1LabelSelector',
        'pod_selector': 'V1LabelSelector'
    }

    attribute_map = {
        'ip_block': 'ipBlock',
        'namespace_selector': 'namespaceSelector',
        'pod_selector': 'podSelector'
    }

    def __init__(self, ip_block=None, namespace_selector=None, pod_selector=None):
        """
        V1NetworkPolicyPeer - a model defined in Swagger
        """

        self._ip_block = None
        self._namespace_selector = None
        self._pod_selector = None
        self.discriminator = None

        if ip_block is not None:
          self.ip_block = ip_block
        if namespace_selector is not None:
          self.namespace_selector = namespace_selector
        if pod_selector is not None:
          self.pod_selector = pod_selector

    @property
    def ip_block(self):
        """
        Gets the ip_block of this V1NetworkPolicyPeer.
        IPBlock defines policy on a particular IPBlock. If this field is set then neither of the other fields can be.

        :return: The ip_block of this V1NetworkPolicyPeer.
        :rtype: V1IPBlock
        """
        return self._ip_block

    @ip_block.setter
    def ip_block(self, ip_block):
        """
        Sets the ip_block of this V1NetworkPolicyPeer.
        IPBlock defines policy on a particular IPBlock. If this field is set then neither of the other fields can be.

        :param ip_block: The ip_block of this V1NetworkPolicyPeer.
        :type: V1IPBlock
        """

        self._ip_block = ip_block

    @property
    def namespace_selector(self):
        """
        Gets the namespace_selector of this V1NetworkPolicyPeer.
        Selects Namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.  If PodSelector is also set, then the NetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects all Pods in the Namespaces selected by NamespaceSelector.

        :return: The namespace_selector of this V1NetworkPolicyPeer.
        :rtype: V1LabelSelector
        """
        return self._namespace_selector

    @namespace_selector.setter
    def namespace_selector(self, namespace_selector):
        """
        Sets the namespace_selector of this V1NetworkPolicyPeer.
        Selects Namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.  If PodSelector is also set, then the NetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects all Pods in the Namespaces selected by NamespaceSelector.

        :param namespace_selector: The namespace_selector of this V1NetworkPolicyPeer.
        :type: V1LabelSelector
        """

        self._namespace_selector = namespace_selector

    @property
    def pod_selector(self):
        """
        Gets the pod_selector of this V1NetworkPolicyPeer.
        This is a label selector which selects Pods. This field follows standard label selector semantics; if present but empty, it selects all pods.  If NamespaceSelector is also set, then the NetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the Pods matching PodSelector in the policy's own Namespace.

        :return: The pod_selector of this V1NetworkPolicyPeer.
        :rtype: V1LabelSelector
        """
        return self._pod_selector

    @pod_selector.setter
    def pod_selector(self, pod_selector):
        """
        Sets the pod_selector of this V1NetworkPolicyPeer.
        This is a label selector which selects Pods. This field follows standard label selector semantics; if present but empty, it selects all pods.  If NamespaceSelector is also set, then the NetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the Pods matching PodSelector in the policy's own Namespace.

        :param pod_selector: The pod_selector of this V1NetworkPolicyPeer.
        :type: V1LabelSelector
        """

        self._pod_selector = pod_selector

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
        if not isinstance(other, V1NetworkPolicyPeer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
