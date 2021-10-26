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


class PointProperties(object):
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
    swagger_types = {"point_id": "int", "crs": "PointPropertiesCrs"}

    attribute_map = {"point_id": "point_id", "crs": "crs"}

    def __init__(self, point_id=None, crs=None):  # noqa: E501
        """PointProperties - a model defined in Swagger"""  # noqa: E501
        self._point_id = None
        self._crs = None
        self.discriminator = None
        if point_id is not None:
            self.point_id = point_id
        if crs is not None:
            self.crs = crs

    @property
    def point_id(self):
        """Gets the point_id of this PointProperties.  # noqa: E501


        :return: The point_id of this PointProperties.  # noqa: E501
        :rtype: int
        """
        return self._point_id

    @point_id.setter
    def point_id(self, point_id):
        """Sets the point_id of this PointProperties.


        :param point_id: The point_id of this PointProperties.  # noqa: E501
        :type: int
        """

        self._point_id = point_id

    @property
    def crs(self):
        """Gets the crs of this PointProperties.  # noqa: E501


        :return: The crs of this PointProperties.  # noqa: E501
        :rtype: PointPropertiesCrs
        """
        return self._crs

    @crs.setter
    def crs(self, crs):
        """Sets the crs of this PointProperties.


        :param crs: The crs of this PointProperties.  # noqa: E501
        :type: PointPropertiesCrs
        """

        self._crs = crs

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
        if issubclass(PointProperties, dict):
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
        if not isinstance(other, PointProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
