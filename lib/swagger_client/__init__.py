# coding: utf-8

# flake8: noqa

"""
    Bilddoku

    Part of the server to support Bilddoku client and plugin.   # noqa: E501

    OpenAPI spec version: 1.0.7
    Contact: nobody@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.bilddoku_product_api import BilddokuProductApi
from swagger_client.api.bilddoku_query_api import BilddokuQueryApi
from swagger_client.api.classes_api import ClassesApi
from swagger_client.api.points_api import PointsApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration

# import models into sdk package
from swagger_client.models.bilddoku_product import BilddokuProduct
from swagger_client.models.bilddoku_query import BilddokuQuery
from swagger_client.models.image import Image
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.point import Point
from swagger_client.models.point_bilddoku import PointBilddoku
from swagger_client.models.point_geometry import PointGeometry
from swagger_client.models.point_geometry_coordinates import PointGeometryCoordinates
from swagger_client.models.point_properties import PointProperties
from swagger_client.models.point_properties_crs import PointPropertiesCrs
from swagger_client.models.type import Type
from swagger_client.models.type_classification import TypeClassification
from swagger_client.models.type_response import TypeResponse
