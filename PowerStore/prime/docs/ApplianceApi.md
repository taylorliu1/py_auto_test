# prime.swagger_client.ApplianceApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appliance_get**](ApplianceApi.md#appliance_get) | **GET** /appliance | Collection Query
[**appliance_id_delete**](ApplianceApi.md#appliance_id_delete) | **DELETE** /appliance/{id} | Delete
[**appliance_id_forecast_post**](ApplianceApi.md#appliance_id_forecast_post) | **POST** /appliance/{id}/forecast | 
[**appliance_id_get**](ApplianceApi.md#appliance_id_get) | **GET** /appliance/{id} | Instance Query
[**appliance_id_patch**](ApplianceApi.md#appliance_id_patch) | **PATCH** /appliance/{id} | Modify
[**appliance_id_time_to_full_post**](ApplianceApi.md#appliance_id_time_to_full_post) | **POST** /appliance/{id}/time_to_full | 
[**appliance_post**](ApplianceApi.md#appliance_post) | **POST** /appliance | Add Appliance
[**appliance_validate_create_post**](ApplianceApi.md#appliance_validate_create_post) | **POST** /appliance/validate_create | Validate Add Appliance


# **appliance_get**
> list[ApplianceInstance] appliance_get()

Collection Query

Query the appliances in a cluster.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ApplianceApi()

try:
    # Collection Query
    api_response = api_instance.appliance_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->appliance_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApplianceInstance]**](ApplianceInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appliance_id_delete**
> appliance_id_delete(id, body=body)

Delete

Remove an appliance from a cluster. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ApplianceApi()
id = 'id_example' # str | Unique identifier of the appliance. name:{name} can be used instead of {id}.
body = prime.swagger_client.ApplianceDelete() # ApplianceDelete | Delete request arguments. (optional)

try:
    # Delete
    api_instance.appliance_id_delete(id, body=body)
except ApiException as e:
    print("Exception when calling ApplianceApi->appliance_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the appliance. name:{name} can be used instead of {id}. | 
 **body** | [**ApplianceDelete**](ApplianceDelete.md)| Delete request arguments. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appliance_id_forecast_post**
> list[ApplianceForecastResponse] appliance_id_forecast_post(id, body)



Forecast capacity usage for an appliance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ApplianceApi()
id = 'id_example' # str | Unique id of the appliance. name:{name} can be used instead of {id}.
body = prime.swagger_client.ApplianceForecast() # ApplianceForecast | 

try:
    api_response = api_instance.appliance_id_forecast_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->appliance_id_forecast_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique id of the appliance. name:{name} can be used instead of {id}. | 
 **body** | [**ApplianceForecast**](ApplianceForecast.md)|  | 

### Return type

[**list[ApplianceForecastResponse]**](ApplianceForecastResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appliance_id_get**
> ApplianceInstance appliance_id_get(id)

Instance Query

Query a specific appliance in a cluster.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ApplianceApi()
id = 'id_example' # str | Unique identifier of the appliance. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.appliance_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->appliance_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the appliance. name:{name} can be used instead of {id}. | 

### Return type

[**ApplianceInstance**](ApplianceInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appliance_id_patch**
> appliance_id_patch(id, body)

Modify

Modify an appliance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ApplianceApi()
id = 'id_example' # str | Unique identifier of the appliance. name:{name} can be used instead of {id}.
body = prime.swagger_client.ApplianceModify() # ApplianceModify | 

try:
    # Modify
    api_instance.appliance_id_patch(id, body)
except ApiException as e:
    print("Exception when calling ApplianceApi->appliance_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the appliance. name:{name} can be used instead of {id}. | 
 **body** | [**ApplianceModify**](ApplianceModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appliance_id_time_to_full_post**
> ApplianceTimeToFullResponse appliance_id_time_to_full_post(id, body)



Returns information about when an appliance is forecast to reach 100% capacity usage.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ApplianceApi()
id = 'id_example' # str | Unique id of the appliance. name:{name} can be used instead of {id}.
body = prime.swagger_client.ApplianceTimeToFull() # ApplianceTimeToFull | 

try:
    api_response = api_instance.appliance_id_time_to_full_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->appliance_id_time_to_full_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique id of the appliance. name:{name} can be used instead of {id}. | 
 **body** | [**ApplianceTimeToFull**](ApplianceTimeToFull.md)|  | 

### Return type

[**ApplianceTimeToFullResponse**](ApplianceTimeToFullResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appliance_post**
> CreateResponse appliance_post(body)

Add Appliance

Add an appliance to an existing cluster.  The cluster consisting of a single appliance without a 4-Port Card installed cannot be extended.  Before adding an appliance, verify whether the cluster has the appropriate number of unused IP addresses. Unused IP addresses for the Management and Storage Networks are required. In addition, PowerStore X appliances also require IP addresses for the vMotion Network. The required number of IP addresses for each network depends on the appliance model.  PowerStore T requires a minimum of 3 Management Network IPs and 2 Storage Network IPs.  PowerStore X requires a minimum of 5 Management Network IPs, 6 Storage Network IPs and 2 vMotion Network IPs.  The IP addresses are automatically pulled from the pool of unused IPs on the cluster. To add additional IP addresses, use the /api/rest/network REST endpoint.  Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ApplianceApi()
body = prime.swagger_client.ApplianceCreate() # ApplianceCreate | 

try:
    # Add Appliance
    api_response = api_instance.appliance_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->appliance_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplianceCreate**](ApplianceCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appliance_validate_create_post**
> ApplianceValidateCreateResponse appliance_validate_create_post(body)

Validate Add Appliance

Validate the add appliance configuration. Success is returned when all the validations have been run. The response includes any detected issues.  Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ApplianceApi()
body = prime.swagger_client.ApplianceValidateCreate() # ApplianceValidateCreate | 

try:
    # Validate Add Appliance
    api_response = api_instance.appliance_validate_create_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->appliance_validate_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplianceValidateCreate**](ApplianceValidateCreate.md)|  | 

### Return type

[**ApplianceValidateCreateResponse**](ApplianceValidateCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

