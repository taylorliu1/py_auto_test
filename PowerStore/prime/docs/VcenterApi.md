# prime.swagger_client.VcenterApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vcenter_get**](VcenterApi.md#vcenter_get) | **GET** /vcenter | Collection Query
[**vcenter_id_delete**](VcenterApi.md#vcenter_id_delete) | **DELETE** /vcenter/{id} | Delete
[**vcenter_id_get**](VcenterApi.md#vcenter_id_get) | **GET** /vcenter/{id} | Instance Query
[**vcenter_id_patch**](VcenterApi.md#vcenter_id_patch) | **PATCH** /vcenter/{id} | Modify
[**vcenter_post**](VcenterApi.md#vcenter_post) | **POST** /vcenter | Create


# **vcenter_get**
> list[VcenterInstance] vcenter_get()

Collection Query

Query registered vCenters.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VcenterApi()

try:
    # Collection Query
    api_response = api_instance.vcenter_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcenterApi->vcenter_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VcenterInstance]**](VcenterInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vcenter_id_delete**
> vcenter_id_delete(id, body=body)

Delete

Delete a registered vCenter. Deletion of vCenter disables functionality that requires communication with vCenter. Not allowed in Unified+ deployments.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VcenterApi()
id = 'id_example' # str | Unique identifier of the vCenter to delete.
body = prime.swagger_client.VcenterDelete() # VcenterDelete |  Was added in version 2.0.0.0. (optional)

try:
    # Delete
    api_instance.vcenter_id_delete(id, body=body)
except ApiException as e:
    print("Exception when calling VcenterApi->vcenter_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the vCenter to delete. | 
 **body** | [**VcenterDelete**](VcenterDelete.md)|  Was added in version 2.0.0.0. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vcenter_id_get**
> VcenterInstance vcenter_id_get(id)

Instance Query

Query a specific vCenter instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VcenterApi()
id = 'id_example' # str | Unique identifier of the vCenter to query.

try:
    # Instance Query
    api_response = api_instance.vcenter_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcenterApi->vcenter_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the vCenter to query. | 

### Return type

[**VcenterInstance**](VcenterInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vcenter_id_patch**
> vcenter_id_patch(id, body=body)

Modify

Modify a vCenter settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VcenterApi()
id = 'id_example' # str | Unique identifier of the vCenter to modify.
body = prime.swagger_client.VcenterModify() # VcenterModify |  (optional)

try:
    # Modify
    api_instance.vcenter_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling VcenterApi->vcenter_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the vCenter to modify. | 
 **body** | [**VcenterModify**](VcenterModify.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vcenter_post**
> CreateResponse vcenter_post(body)

Create

Add a vCenter. Not allowed in Unified+ deployments.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VcenterApi()
body = prime.swagger_client.VcenterCreate() # VcenterCreate | 

try:
    # Create
    api_response = api_instance.vcenter_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcenterApi->vcenter_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VcenterCreate**](VcenterCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

