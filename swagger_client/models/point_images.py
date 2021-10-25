# coding: utf-8

"""
    Bilddoku

    Part of the server to support Bilddoku client and plugin.   # noqa: E501

    OpenAPI spec version: 1.0.4
    Contact: nobody@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PointImages(object):
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
    swagger_types = {
        '_1': 'Image',
        '_2': 'Image',
        '_3': 'Image',
        '_4': 'Image',
        '_5': 'Image'
    }

    attribute_map = {
        '_1': '1',
        '_2': '2',
        '_3': '3',
        '_4': '4',
        '_5': '5'
    }

    def __init__(self, _1=None, _2=None, _3=None, _4=None, _5=None):  # noqa: E501
        """PointImages - a model defined in Swagger"""  # noqa: E501
        self.__1 = None
        self.__2 = None
        self.__3 = None
        self.__4 = None
        self.__5 = None
        self.discriminator = None
        if _1 is not None:
            self._1 = _1
        if _2 is not None:
            self._2 = _2
        if _3 is not None:
            self._3 = _3
        if _4 is not None:
            self._4 = _4
        if _5 is not None:
            self._5 = _5

    @property
    def _1(self):
        """Gets the _1 of this PointImages.  # noqa: E501


        :return: The _1 of this PointImages.  # noqa: E501
        :rtype: Image
        """
        return self.__1

    @_1.setter
    def _1(self, _1):
        """Sets the _1 of this PointImages.


        :param _1: The _1 of this PointImages.  # noqa: E501
        :type: Image
        """

        self.__1 = _1

    @property
    def _2(self):
        """Gets the _2 of this PointImages.  # noqa: E501


        :return: The _2 of this PointImages.  # noqa: E501
        :rtype: Image
        """
        return self.__2

    @_2.setter
    def _2(self, _2):
        """Sets the _2 of this PointImages.


        :param _2: The _2 of this PointImages.  # noqa: E501
        :type: Image
        """

        self.__2 = _2

    @property
    def _3(self):
        """Gets the _3 of this PointImages.  # noqa: E501


        :return: The _3 of this PointImages.  # noqa: E501
        :rtype: Image
        """
        return self.__3

    @_3.setter
    def _3(self, _3):
        """Sets the _3 of this PointImages.


        :param _3: The _3 of this PointImages.  # noqa: E501
        :type: Image
        """

        self.__3 = _3

    @property
    def _4(self):
        """Gets the _4 of this PointImages.  # noqa: E501


        :return: The _4 of this PointImages.  # noqa: E501
        :rtype: Image
        """
        return self.__4

    @_4.setter
    def _4(self, _4):
        """Sets the _4 of this PointImages.


        :param _4: The _4 of this PointImages.  # noqa: E501
        :type: Image
        """

        self.__4 = _4

    @property
    def _5(self):
        """Gets the _5 of this PointImages.  # noqa: E501


        :return: The _5 of this PointImages.  # noqa: E501
        :rtype: Image
        """
        return self.__5

    @_5.setter
    def _5(self, _5):
        """Sets the _5 of this PointImages.


        :param _5: The _5 of this PointImages.  # noqa: E501
        :type: Image
        """

        self.__5 = _5

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PointImages, dict):
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
        if not isinstance(other, PointImages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
