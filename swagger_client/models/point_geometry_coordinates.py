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

class PointGeometryCoordinates(object):
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
        'east': 'float',
        'north': 'float',
        'altitude': 'float'
    }

    attribute_map = {
        'east': 'east',
        'north': 'north',
        'altitude': 'altitude'
    }

    def __init__(self, east=None, north=None, altitude=None):  # noqa: E501
        """PointGeometryCoordinates - a model defined in Swagger"""  # noqa: E501
        self._east = None
        self._north = None
        self._altitude = None
        self.discriminator = None
        if east is not None:
            self.east = east
        if north is not None:
            self.north = north
        if altitude is not None:
            self.altitude = altitude

    @property
    def east(self):
        """Gets the east of this PointGeometryCoordinates.  # noqa: E501


        :return: The east of this PointGeometryCoordinates.  # noqa: E501
        :rtype: float
        """
        return self._east

    @east.setter
    def east(self, east):
        """Sets the east of this PointGeometryCoordinates.


        :param east: The east of this PointGeometryCoordinates.  # noqa: E501
        :type: float
        """

        self._east = east

    @property
    def north(self):
        """Gets the north of this PointGeometryCoordinates.  # noqa: E501


        :return: The north of this PointGeometryCoordinates.  # noqa: E501
        :rtype: float
        """
        return self._north

    @north.setter
    def north(self, north):
        """Sets the north of this PointGeometryCoordinates.


        :param north: The north of this PointGeometryCoordinates.  # noqa: E501
        :type: float
        """

        self._north = north

    @property
    def altitude(self):
        """Gets the altitude of this PointGeometryCoordinates.  # noqa: E501


        :return: The altitude of this PointGeometryCoordinates.  # noqa: E501
        :rtype: float
        """
        return self._altitude

    @altitude.setter
    def altitude(self, altitude):
        """Sets the altitude of this PointGeometryCoordinates.


        :param altitude: The altitude of this PointGeometryCoordinates.  # noqa: E501
        :type: float
        """

        self._altitude = altitude

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
        if issubclass(PointGeometryCoordinates, dict):
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
        if not isinstance(other, PointGeometryCoordinates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
