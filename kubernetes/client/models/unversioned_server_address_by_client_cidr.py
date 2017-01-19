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


class UnversionedServerAddressByClientCIDR(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, client_cidr=None, server_address=None):
        """
        UnversionedServerAddressByClientCIDR - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'client_cidr': 'str',
            'server_address': 'str'
        }

        self.attribute_map = {
            'client_cidr': 'clientCIDR',
            'server_address': 'serverAddress'
        }

        self._client_cidr = client_cidr
        self._server_address = server_address

    @property
    def client_cidr(self):
        """
        Gets the client_cidr of this UnversionedServerAddressByClientCIDR.
        The CIDR with which clients can match their IP to figure out the server address that they should use.

        :return: The client_cidr of this UnversionedServerAddressByClientCIDR.
        :rtype: str
        """
        return self._client_cidr

    @client_cidr.setter
    def client_cidr(self, client_cidr):
        """
        Sets the client_cidr of this UnversionedServerAddressByClientCIDR.
        The CIDR with which clients can match their IP to figure out the server address that they should use.

        :param client_cidr: The client_cidr of this UnversionedServerAddressByClientCIDR.
        :type: str
        """
        if client_cidr is None:
            raise ValueError("Invalid value for `client_cidr`, must not be `None`")

        self._client_cidr = client_cidr

    @property
    def server_address(self):
        """
        Gets the server_address of this UnversionedServerAddressByClientCIDR.
        Address of this server, suitable for a client that matches the above CIDR. This can be a hostname, hostname:port, IP or IP:port.

        :return: The server_address of this UnversionedServerAddressByClientCIDR.
        :rtype: str
        """
        return self._server_address

    @server_address.setter
    def server_address(self, server_address):
        """
        Sets the server_address of this UnversionedServerAddressByClientCIDR.
        Address of this server, suitable for a client that matches the above CIDR. This can be a hostname, hostname:port, IP or IP:port.

        :param server_address: The server_address of this UnversionedServerAddressByClientCIDR.
        :type: str
        """
        if server_address is None:
            raise ValueError("Invalid value for `server_address`, must not be `None`")

        self._server_address = server_address

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
