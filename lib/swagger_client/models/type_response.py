# coding: utf-8

"""
    Bilddoku

    Part of the server to support Bilddoku client and plugin.   # noqa: E501

    OpenAPI spec version: 1.0.7
    Contact: nobody@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class TypeResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {"api_version": "str", "types": "list[Type]"}

    attribute_map = {"api_version": "api_version", "types": "types"}

    def __init__(self, api_version=None, types=None):  # noqa: E501
        """TypeResponse - a model defined in Swagger"""  # noqa: E501
        self._api_version = None
        self._types = None
        self.discriminator = None
        if api_version is not None:
            self.api_version = api_version
        if types is not None:
            self.types = types

    @property
    def api_version(self):
        """Gets the api_version of this TypeResponse.  # noqa: E501


        :return: The api_version of this TypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this TypeResponse.


        :param api_version: The api_version of this TypeResponse.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def types(self):
        """Gets the types of this TypeResponse.  # noqa: E501


        :return: The types of this TypeResponse.  # noqa: E501
        :rtype: list[Type]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this TypeResponse.


        :param types: The types of this TypeResponse.  # noqa: E501
        :type: list[Type]
        """

        self._types = types

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(TypeResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
