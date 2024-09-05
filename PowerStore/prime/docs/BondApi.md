# prime.swagger_client.BondApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bond_get**](BondApi.md#bond_get) | **GET** /bond | Collection Query
[**bond_id_delete**](BondApi.md#bond_id_delete) | **DELETE** /bond/{id} | Delete
[**bond_id_get**](BondApi.md#bond_id_get) | **GET** /bond/{id} | Collection Query
[**bond_id_patch**](BondApi.md#bond_id_patch) | **PATCH** /bond/{id} | Modify
[**bond_post**](BondApi.md#bond_post) | **POST** /bond | Create


# **bond_get**
> list[BondInstance] bond_get()

Collection Query

Query bonds.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.BondApi()

try:
    # Collection Query
    api_response = api_instance.bond_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->bond_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BondInstance]**](BondInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bond_id_delete**
> bond_id_delete(id)

Delete

Delete a user bond. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.BondApi()
id = 'id_example' # str | Unique identifier of the bond. name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.bond_id_delete(id)
except ApiException as e:
    print("Exception when calling BondApi->bond_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the bond. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bond_id_get**
> BondInstance bond_id_get(id)

Collection Query

Query bonds.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.BondApi()
id = 'id_example' # str | Unique identifier of the bond. name:{name} can be used instead of {id}.

try:
    # Collection Query
    api_response = api_instance.bond_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->bond_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the bond. name:{name} can be used instead of {id}. | 

### Return type

[**BondInstance**](BondInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bond_id_patch**
> bond_id_patch(id, body)

Modify

Modify user bond. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.BondApi()
id = 'id_example' # str | Unique identifier of the bond. name:{name} can be used instead of {id}.
body = prime.swagger_client.BondModify() # BondModify | 

try:
    # Modify
    api_instance.bond_id_patch(id, body)
except ApiException as e:
    print("Exception when calling BondApi->bond_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the bond. name:{name} can be used instead of {id}. | 
 **body** | [**BondModify**](BondModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bond_post**
> CreateResponse bond_post(body)

Create

Create a user bond. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.BondApi()
body = prime.swagger_client.BondCreate() # BondCreate | 

try:
    # Create
    api_response = api_instance.bond_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BondApi->bond_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BondCreate**](BondCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

