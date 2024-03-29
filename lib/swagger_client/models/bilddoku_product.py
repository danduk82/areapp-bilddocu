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


class BilddokuProduct(object):
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
        "api_version": "str",
        "id": "int",
        "commune": "str",
        "swissname": "str",
        "creation_date": "datetime",
        "created_by": "int",
        "file_path": "str",
        "scale": "float",
        "bilddoku_query_id": "int",
        "template": "str",
    }

    attribute_map = {
        "api_version": "api_version",
        "id": "id",
        "commune": "commune",
        "swissname": "swissname",
        "creation_date": "creation_date",
        "created_by": "created_by",
        "file_path": "file_path",
        "scale": "scale",
        "bilddoku_query_id": "bilddoku_query_id",
        "template": "template",
    }

    def __init__(
        self,
        api_version=None,
        id=None,
        commune=None,
        swissname=None,
        creation_date=None,
        created_by=None,
        file_path=None,
        scale=None,
        bilddoku_query_id=None,
        template=None,
    ):  # noqa: E501
        """BilddokuProduct - a model defined in Swagger"""  # noqa: E501
        self._api_version = None
        self._id = None
        self._commune = None
        self._swissname = None
        self._creation_date = None
        self._created_by = None
        self._file_path = None
        self._scale = None
        self._bilddoku_query_id = None
        self._template = None
        self.discriminator = None
        if api_version is not None:
            self.api_version = api_version
        if id is not None:
            self.id = id
        if commune is not None:
            self.commune = commune
        if swissname is not None:
            self.swissname = swissname
        if creation_date is not None:
            self.creation_date = creation_date
        if created_by is not None:
            self.created_by = created_by
        if file_path is not None:
            self.file_path = file_path
        if scale is not None:
            self.scale = scale
        if bilddoku_query_id is not None:
            self.bilddoku_query_id = bilddoku_query_id
        if template is not None:
            self.template = template

    @property
    def api_version(self):
        """Gets the api_version of this BilddokuProduct.  # noqa: E501


        :return: The api_version of this BilddokuProduct.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this BilddokuProduct.


        :param api_version: The api_version of this BilddokuProduct.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def id(self):
        """Gets the id of this BilddokuProduct.  # noqa: E501


        :return: The id of this BilddokuProduct.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BilddokuProduct.


        :param id: The id of this BilddokuProduct.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def commune(self):
        """Gets the commune of this BilddokuProduct.  # noqa: E501


        :return: The commune of this BilddokuProduct.  # noqa: E501
        :rtype: str
        """
        return self._commune

    @commune.setter
    def commune(self, commune):
        """Sets the commune of this BilddokuProduct.


        :param commune: The commune of this BilddokuProduct.  # noqa: E501
        :type: str
        """

        self._commune = commune

    @property
    def swissname(self):
        """Gets the swissname of this BilddokuProduct.  # noqa: E501


        :return: The swissname of this BilddokuProduct.  # noqa: E501
        :rtype: str
        """
        return self._swissname

    @swissname.setter
    def swissname(self, swissname):
        """Sets the swissname of this BilddokuProduct.


        :param swissname: The swissname of this BilddokuProduct.  # noqa: E501
        :type: str
        """

        self._swissname = swissname

    @property
    def creation_date(self):
        """Gets the creation_date of this BilddokuProduct.  # noqa: E501


        :return: The creation_date of this BilddokuProduct.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this BilddokuProduct.


        :param creation_date: The creation_date of this BilddokuProduct.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def created_by(self):
        """Gets the created_by of this BilddokuProduct.  # noqa: E501


        :return: The created_by of this BilddokuProduct.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this BilddokuProduct.


        :param created_by: The created_by of this BilddokuProduct.  # noqa: E501
        :type: int
        """

        self._created_by = created_by

    @property
    def file_path(self):
        """Gets the file_path of this BilddokuProduct.  # noqa: E501


        :return: The file_path of this BilddokuProduct.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this BilddokuProduct.


        :param file_path: The file_path of this BilddokuProduct.  # noqa: E501
        :type: str
        """

        self._file_path = file_path

    @property
    def scale(self):
        """Gets the scale of this BilddokuProduct.  # noqa: E501


        :return: The scale of this BilddokuProduct.  # noqa: E501
        :rtype: float
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this BilddokuProduct.


        :param scale: The scale of this BilddokuProduct.  # noqa: E501
        :type: float
        """

        self._scale = scale

    @property
    def bilddoku_query_id(self):
        """Gets the bilddoku_query_id of this BilddokuProduct.  # noqa: E501


        :return: The bilddoku_query_id of this BilddokuProduct.  # noqa: E501
        :rtype: int
        """
        return self._bilddoku_query_id

    @bilddoku_query_id.setter
    def bilddoku_query_id(self, bilddoku_query_id):
        """Sets the bilddoku_query_id of this BilddokuProduct.


        :param bilddoku_query_id: The bilddoku_query_id of this BilddokuProduct.  # noqa: E501
        :type: int
        """

        self._bilddoku_query_id = bilddoku_query_id

    @property
    def template(self):
        """Gets the template of this BilddokuProduct.  # noqa: E501


        :return: The template of this BilddokuProduct.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this BilddokuProduct.


        :param template: The template of this BilddokuProduct.  # noqa: E501
        :type: str
        """

        self._template = template

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
        if issubclass(BilddokuProduct, dict):
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
        if not isinstance(other, BilddokuProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
