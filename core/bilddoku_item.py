from PyQt5.QtCore import pyqtSignal
from .. import swagger_client
from ..swagger_client import models
from ..swagger_client.rest import ApiException


class BilddokuItem:
    refreshed = pyqtSignal()

    def __init__(self, configuration):
        self.uow_id = None
        self.setConfiguration(configuration)

    def setupApis(self):
        self.pointApi = swagger_client.PointsApi(
            swagger_client.ApiClient(self._configuration)
        )
        self.bilddokuQueryApi = swagger_client.BilddokuQueryApi(
            swagger_client.ApiClient(self._configuration)
        )
        self.bilddokuProductApi = swagger_client.BilddokuProductApi(
            swagger_client.ApiClient(self._configuration)
        )

    def setConfiguration(self, configuration):
        self._configuration = configuration
        self.setupApis()

    def setBilddokuProduct(self, bilddokuProduct=models.BilddokuProduct()):
        self.bilddokuProduct = bilddokuProduct

    def setBilddokuQuery(self, bilddokuQuery=models.BilddokuQuery()):
        self.bilddokuQuery = bilddokuQuery

    def setPoint(self, point=models.Point()):
        self.point = point

    def next(self):
        try:
            # reset BilddokuProduct
            self.setBilddokuProduct()
            # Get next bilddoku_query_id
            if self.uow_id:
                bilddoku_query_id = self.bilddokuQueryApi.get_bilddoku_query_next(
                    uow_id=self.uow_id
                )
            else:
                bilddoku_query_id = self.bilddokuQueryApi.get_bilddoku_query_next()
            bilddoku_query = self.bilddokuQueryApi.get_bilddoku_by_id(bilddoku_query_id)
            print(bilddoku_query)
            point = self.pointApi.get_point(point_id=bilddoku_query.point_id)
            self.setBilddokuQuery(bilddoku_query)
            print(self.bilddokuQuery)
            self.setPoint(point)
            print(self.point)

        except ApiException as e:
            print(
                "Exception when calling BilddokuQueryApi->get_bilddoku_query_next: %s\n"
                % e
            )

    def requestPoint(self, point_id):
        try:
            # get point
            api_response = self.pointApi.get_point(point_id, with_bilddoku=True)
        except ApiException as e:
            print("Exception when calling PointsApi->get_point: %s\n" % e)
