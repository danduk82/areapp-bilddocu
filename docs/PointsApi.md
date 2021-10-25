# swagger_client.PointsApi

All URIs are relative to *https://virtserver.swaggerhub.com/danduk82/bilddoku/1.0.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_point**](PointsApi.md#get_point) | **GET** /points/{point_id} | get point

# **get_point**
> BilddokuQuery get_point(point_id, with_bilddoku=with_bilddoku)

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
api_instance = swagger_client.PointsApi()
point_id = 789 # int | ID of point
with_bilddoku = true # bool | gives also the bilddoku (optional)

try:
    # get point
    api_response = api_instance.get_point(point_id, with_bilddoku=with_bilddoku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointsApi->get_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point_id** | **int**| ID of point | 
 **with_bilddoku** | **bool**| gives also the bilddoku | [optional] 

### Return type

[**BilddokuQuery**](BilddokuQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

