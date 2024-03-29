# swagger_client.ClassesApi

All URIs are relative to *https://virtserver.swaggerhub.com/danduk82/bilddoku/1.0.7*

| Method                                                   | HTTP request            | Description               |
| -------------------------------------------------------- | ----------------------- | ------------------------- |
| [**get_bilddoku_typs**](ClassesApi.md#get_bilddoku_typs) | **GET** /bilddoku/types | Get list of bilddoku typs |

# **get_bilddoku_typs**

> TypeResponse get_bilddoku_typs()

Get list of bilddoku typs

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClassesApi(swagger_client.ApiClient(configuration))

try:
    # Get list of bilddoku typs
    api_response = api_instance.get_bilddoku_typs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassesApi->get_bilddoku_typs: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**TypeResponse**](TypeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
