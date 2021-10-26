# coding: utf-8

"""
    Bilddoku

    Part of the server to support Bilddoku client and plugin.   # noqa: E501

    OpenAPI spec version: 1.0.6
    Contact: nobody@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Image(object):
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
    swagger_types = {"period": "int", "year": "int", "left": "str", "right": "str"}

    attribute_map = {
        "period": "period",
        "year": "year",
        "left": "left",
        "right": "right",
    }

    def __init__(self, period=None, year=None, left=None, right=None):  # noqa: E501
        """Image - a model defined in Swagger"""  # noqa: E501
        self._period = None
        self._year = None
        self._left = None
        self._right = None
        self.discriminator = None
        if period is not None:
            self.period = period
        if year is not None:
            self.year = year
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right

    @property
    def period(self):
        """Gets the period of this Image.  # noqa: E501


        :return: The period of this Image.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Image.


        :param period: The period of this Image.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def year(self):
        """Gets the year of this Image.  # noqa: E501


        :return: The year of this Image.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Image.


        :param year: The year of this Image.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def left(self):
        """Gets the left of this Image.  # noqa: E501


        :return: The left of this Image.  # noqa: E501
        :rtype: str
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this Image.


        :param left: The left of this Image.  # noqa: E501
        :type: str
        """

        self._left = left

    @property
    def right(self):
        """Gets the right of this Image.  # noqa: E501


        :return: The right of this Image.  # noqa: E501
        :rtype: str
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this Image.


        :param right: The right of this Image.  # noqa: E501
        :type: str
        """

        self._right = right

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
        if issubclass(Image, dict):
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
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
