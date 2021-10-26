# swagger_client.BilddokuProductApi

All URIs are relative to *https://virtserver.swaggerhub.com/danduk82/bilddoku/1.0.6*

| Method                                                                       | HTTP request                                       | Description                                |
| ---------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------ |
| [**delete_bilddoku_product**](BilddokuProductApi.md#delete_bilddoku_product) | **DELETE** /bilddoku/product/{bilddoku_product_id} | delete Bilddoku produkt                    |
| [**get_bilddoku_product**](BilddokuProductApi.md#get_bilddoku_product)       | **GET** /bilddoku/product/{bilddoku_product_id}    | add new product for a given bilddoku query |
| [**post_bilddoku_product**](BilddokuProductApi.md#post_bilddoku_product)     | **POST** /bilddoku/product/                        | add new product for a given bilddoku query |
| [**put_bilddoku_product**](BilddokuProductApi.md#put_bilddoku_product)       | **PUT** /bilddoku/product/{bilddoku_product_id}    | add new product for a given bilddoku query |

# **delete_bilddoku_product**

> delete_bilddoku_product(bilddoku_product_id)

delete Bilddoku produkt

delete Bilddoku product for a id

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BilddokuProductApi(swagger_client.ApiClient(configuration))
bilddoku_product_id = 789 # int | ID of bilddoku

try:
    # delete Bilddoku produkt
    api_instance.delete_bilddoku_product(bilddoku_product_id)
except ApiException as e:
    print("Exception when calling BilddokuProductApi->delete_bilddoku_product: %s\n" % e)
```

### Parameters

| Name                    | Type    | Description    | Notes |
| ----------------------- | ------- | -------------- | ----- |
| **bilddoku_product_id** | **int** | ID of bilddoku |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bilddoku_product**

> ComponentsrequestBodiesBilddokuProduct get_bilddoku_product(bilddoku_product_id)

add new product for a given bilddoku query

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BilddokuProductApi(swagger_client.ApiClient(configuration))
bilddoku_product_id = 789 # int | ID of bilddoku

try:
    # add new product for a given bilddoku query
    api_response = api_instance.get_bilddoku_product(bilddoku_product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BilddokuProductApi->get_bilddoku_product: %s\n" % e)
```

### Parameters

| Name                    | Type    | Description    | Notes |
| ----------------------- | ------- | -------------- | ----- |
| **bilddoku_product_id** | **int** | ID of bilddoku |

### Return type

[**ComponentsrequestBodiesBilddokuProduct**](ComponentsrequestBodiesBilddokuProduct.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_bilddoku_product**

> post_bilddoku_product(body)

add new product for a given bilddoku query

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BilddokuProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.BilddokuProduct() # BilddokuProduct |

try:
    # add new product for a given bilddoku query
    api_instance.post_bilddoku_product(body)
except ApiException as e:
    print("Exception when calling BilddokuProductApi->post_bilddoku_product: %s\n" % e)
```

### Parameters

| Name     | Type                                      | Description | Notes |
| -------- | ----------------------------------------- | ----------- | ----- |
| **body** | [**BilddokuProduct**](BilddokuProduct.md) |             |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_bilddoku_product**

> put_bilddoku_product(body, bilddoku_product_id)

add new product for a given bilddoku query

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BilddokuProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.BilddokuProduct() # BilddokuProduct |
bilddoku_product_id = 789 # int | ID of bilddoku

try:
    # add new product for a given bilddoku query
    api_instance.put_bilddoku_product(body, bilddoku_product_id)
except ApiException as e:
    print("Exception when calling BilddokuProductApi->put_bilddoku_product: %s\n" % e)
```

### Parameters

| Name                    | Type                                      | Description    | Notes |
| ----------------------- | ----------------------------------------- | -------------- | ----- |
| **body**                | [**BilddokuProduct**](BilddokuProduct.md) |                |
| **bilddoku_product_id** | **int**                                   | ID of bilddoku |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
