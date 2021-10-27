# swagger_client.BilddokuQueryApi

All URIs are relative to *https://virtserver.swaggerhub.com/danduk82/bilddoku/1.0.7*

| Method                                                                     | HTTP request                                   | Description                                        |
| -------------------------------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------- |
| [**add_bilddoku_query**](BilddokuQueryApi.md#add_bilddoku_query)           | **PUT** /bilddoku/query/{bilddoku_query_id}    | Add a new bilddoku query or update an existing one |
| [**delete_bilddoku_by_id**](BilddokuQueryApi.md#delete_bilddoku_by_id)     | **DELETE** /bilddoku/query/{bilddoku_query_id} | delete Bilddoku for given point                    |
| [**get_bilddoku_by_id**](BilddokuQueryApi.md#get_bilddoku_by_id)           | **GET** /bilddoku/query/{bilddoku_query_id}    | get Bilddoku for given point                       |
| [**get_bilddoku_query_next**](BilddokuQueryApi.md#get_bilddoku_query_next) | **GET** /bilddoku/query/next                   | Get next bilddoku_query_id                         |

# **add_bilddoku_query**

> BilddokuQuery add_bilddoku_query(body, bilddoku_query_id)

Add a new bilddoku query or update an existing one

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BilddokuQueryApi(swagger_client.ApiClient(configuration))
body = swagger_client.BilddokuQuery() # BilddokuQuery | Bilddoku query object that needs to be added to the store
bilddoku_query_id = 789 # int | ID of bilddoku

try:
    # Add a new bilddoku query or update an existing one
    api_response = api_instance.add_bilddoku_query(body, bilddoku_query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BilddokuQueryApi->add_bilddoku_query: %s\n" % e)
```

### Parameters

| Name                  | Type                                  | Description                                               | Notes |
| --------------------- | ------------------------------------- | --------------------------------------------------------- | ----- |
| **body**              | [**BilddokuQuery**](BilddokuQuery.md) | Bilddoku query object that needs to be added to the store |
| **bilddoku_query_id** | **int**                               | ID of bilddoku                                            |

### Return type

[**BilddokuQuery**](BilddokuQuery.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bilddoku_by_id**

> delete_bilddoku_by_id(bilddoku_query_id)

delete Bilddoku for given point

delete Bilddoku for a given point

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BilddokuQueryApi(swagger_client.ApiClient(configuration))
bilddoku_query_id = 789 # int | ID of point

try:
    # delete Bilddoku for given point
    api_instance.delete_bilddoku_by_id(bilddoku_query_id)
except ApiException as e:
    print("Exception when calling BilddokuQueryApi->delete_bilddoku_by_id: %s\n" % e)
```

### Parameters

| Name                  | Type    | Description | Notes |
| --------------------- | ------- | ----------- | ----- |
| **bilddoku_query_id** | **int** | ID of point |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bilddoku_by_id**

> BilddokuQuery get_bilddoku_by_id(bilddoku_query_id)

get Bilddoku for given point

Get Bilddoku query if exists for a given point

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BilddokuQueryApi(swagger_client.ApiClient(configuration))
bilddoku_query_id = 789 # int | ID of point

try:
    # get Bilddoku for given point
    api_response = api_instance.get_bilddoku_by_id(bilddoku_query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BilddokuQueryApi->get_bilddoku_by_id: %s\n" % e)
```

### Parameters

| Name                  | Type    | Description | Notes |
| --------------------- | ------- | ----------- | ----- |
| **bilddoku_query_id** | **int** | ID of point |

### Return type

[**BilddokuQuery**](BilddokuQuery.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bilddoku_query_next**

> InlineResponse200 get_bilddoku_query_next(uow_id=uow_id)

Get next bilddoku_query_id

Get the next bilddoku that has been queried and a product is not yet produced

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BilddokuQueryApi(swagger_client.ApiClient(configuration))
uow_id = 789 # int |  (optional)

try:
    # Get next bilddoku_query_id
    api_response = api_instance.get_bilddoku_query_next(uow_id=uow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BilddokuQueryApi->get_bilddoku_query_next: %s\n" % e)
```

### Parameters

| Name       | Type    | Description | Notes      |
| ---------- | ------- | ----------- | ---------- |
| **uow_id** | **int** |             | [optional] |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
