from PyQt5.QtCore import pyqtSignal
from .. import swagger_client
from ..swagger_client import models
from ..swagger_client.rest import ApiException


class BilddokuItem:
    refreshed = pyqtSignal()

    def __init__(self, configuration):
        self.setConfiguration(configuration)
        self.pointApi = swagger_client.PointsApi(
            swagger_client.ApiClient(self._configuration)
        )
        self.bilddokuQueryApi = swagger_client.BilddokuQueryApi(
            swagger_client.ApiClient(self._configuration)
        )
        self.bilddokuProductApi = swagger_client.BilddokuProductApi(
            swagger_client.ApiClient(self._configuration)
        )
        self.setBilddokuProduct()
        self.setBilddokuQuery()
        self.setPoint()

    def setConfiguration(self, configuration):
        self._configuration = configuration

    def setBilddokuProduct(self, bilddokuProduct=models.BilddokuProduct()):
        self.bilddokuProduct = bilddokuProduct

    def setBilddokuQuery(self, bilddokuQuery=models.BilddokuQuery()):
        self.bilddokuQuery = bilddokuQuery

    def setPoint(self, point=models.Point()):
        self.point = point

    def next(self):
        try:
            # Get next bilddoku_query_id
            api_response = api_instance.get_bilddoku_query_list()
            pprint(api_response)
        except ApiException as e:
            print(
                "Exception when calling BilddokuQueryApi->get_bilddoku_query_list: %s\n"
                % e
            )

    def requestPoint(self, point_id):
        try:
            # get point
            api_response = self.pointApi.get_point(point_id, with_bilddoku=True)
        except ApiException as e:
            print("Exception when calling PointsApi->get_point: %s\n" % e)
