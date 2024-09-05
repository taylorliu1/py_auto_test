# prime.swagger_client.ClusterApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_get**](ClusterApi.md#cluster_get) | **GET** /cluster | Collection Query
[**cluster_id_forecast_post**](ClusterApi.md#cluster_id_forecast_post) | **POST** /cluster/{id}/forecast | 
[**cluster_id_get**](ClusterApi.md#cluster_id_get) | **GET** /cluster/{id} | Instance Query
[**cluster_id_patch**](ClusterApi.md#cluster_id_patch) | **PATCH** /cluster/{id} | Modify
[**cluster_id_time_to_full_post**](ClusterApi.md#cluster_id_time_to_full_post) | **POST** /cluster/{id}/time_to_full | 
[**cluster_post**](ClusterApi.md#cluster_post) | **POST** /cluster | Create
[**cluster_validate_create_post**](ClusterApi.md#cluster_validate_create_post) | **POST** /cluster/validate_create | Validate Create


# **cluster_get**
> list[ClusterInstance] cluster_get()

Collection Query

Query the details about the cluster.  This resource type collection query does not support filtering, sorting or pagination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ClusterApi()

try:
    # Collection Query
    api_response = api_instance.cluster_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ClusterInstance]**](ClusterInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_forecast_post**
> list[ClusterForecastResponse] cluster_id_forecast_post(id, body)



Forecast capacity usage for the cluster.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ClusterApi()
id = 'id_example' # str | Unique id of the cluster.
body = prime.swagger_client.ClusterForecast() # ClusterForecast | 

try:
    api_response = api_instance.cluster_id_forecast_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_id_forecast_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique id of the cluster. | 
 **body** | [**ClusterForecast**](ClusterForecast.md)|  | 

### Return type

[**list[ClusterForecastResponse]**](ClusterForecastResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_get**
> ClusterInstance cluster_id_get(id)

Instance Query

Query details about the cluster.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ClusterApi()
id = 'id_example' # str | Unique identifier of the cluster.

try:
    # Instance Query
    api_response = api_instance.cluster_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the cluster. | 

### Return type

[**ClusterInstance**](ClusterInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_patch**
> cluster_id_patch(id, body=body)

Modify

Update properties of the cluster.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ClusterApi()
id = 'id_example' # str | Unique identifier of the cluster.
body = prime.swagger_client.ClusterModify() # ClusterModify |  (optional)

try:
    # Modify
    api_instance.cluster_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the cluster. | 
 **body** | [**ClusterModify**](ClusterModify.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_time_to_full_post**
> ClusterTimeToFullResponse cluster_id_time_to_full_post(id, body)



Returns information about when the cluster is forecast to reach 100% capacity usage.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ClusterApi()
id = 'id_example' # str | Unique id of the cluster
body = prime.swagger_client.ClusterTimeToFull() # ClusterTimeToFull | 

try:
    api_response = api_instance.cluster_id_time_to_full_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_id_time_to_full_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique id of the cluster | 
 **body** | [**ClusterTimeToFull**](ClusterTimeToFull.md)|  | 

### Return type

[**ClusterTimeToFullResponse**](ClusterTimeToFullResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_post**
> CreateResponse cluster_post(body)

Create

Create a Power Store or Power Store X Cluster of one or more appliances.  * You can create a cluster of up to 4 appliances.  * Except where explicitly noted, all parameters in **vcenters** object are mandatory when creating a PowerStoreX cluster.  * When creating a multi-appliance cluster, the most capable appliance is chosen as the Primary appliance based on the appliance configuration type.  * All of the appliances must have the 4-Port Card installed to be added into a multi-appliance cluster.  * When creating a multi-appliance cluster, best effort is made to successfully create the cluster. The create operation:     * Fails, if the Primary appliance is not configured successfully.     * Succeeds, if one or more secondary appliances fail to configure.       * Any secondary appliance that is configured successfully will be added to the cluster.       * An alert is generated for any failed secondary appliance. Look for these alerts in the PowerStore Manager. Resolve issues on failed appliances before  adding the appliances to the cluster.  * When creating a cluster asynchronously, wait for ~10 minutes until Job Service is initialized before querying the status of the running job. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ClusterApi()
body = prime.swagger_client.ClusterCreate() # ClusterCreate | 

try:
    # Create
    api_response = api_instance.cluster_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterCreate**](ClusterCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_validate_create_post**
> ClusterValidateCreateResponse cluster_validate_create_post(body)

Validate Create

Validate the create cluster configuration for a PowerStore or PowerStore X Cluster of one or more appliances. Success is returned when all the validations have been run. The response shows whether any of the validations detected any issues. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ClusterApi()
body = prime.swagger_client.ClusterValidateCreate() # ClusterValidateCreate | 

try:
    # Validate Create
    api_response = api_instance.cluster_validate_create_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_validate_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterValidateCreate**](ClusterValidateCreate.md)|  | 

### Return type

[**ClusterValidateCreateResponse**](ClusterValidateCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

