# swagger_client.PointsApi

All URIs are relative to *https://virtserver.swaggerhub.com/danduk82/bilddoku/1.0.7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_point**](PointsApi.md#get_point) | **GET** /bilddoku/points/{point_id} | get point

# **get_point**
> Point get_point(point_id)

get point

Get point

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PointsApi(swagger_client.ApiClient(configuration))
point_id = 789 # int | ID of point

try:
    # get point
    api_response = api_instance.get_point(point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointsApi->get_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point_id** | **int**| ID of point | 

### Return type

[**Point**](Point.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

