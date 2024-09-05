# swagger_client.NasClustersApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nas_cluster_info_get**](NasClustersApi.md#nas_cluster_info_get) | **GET** /nas-clusters | Collection Query
[**nas_clusters_id_delete**](NasClustersApi.md#nas_clusters_id_delete) | **DELETE** /nas-clusters/{id} | De-register SDNAS cluster from management
[**nas_clusters_id_get**](NasClustersApi.md#nas_clusters_id_get) | **GET** /nas-clusters/{id} | Instance Query
[**nas_clusters_id_patch**](NasClustersApi.md#nas_clusters_id_patch) | **PATCH** /nas-clusters/{id} | Modify
[**nas_clusters_post**](NasClustersApi.md#nas_clusters_post) | **POST** /nas-clusters | Notify new NAS cluster deployment

# **nas_cluster_info_get**
> list[NasClusterInfo] nas_cluster_info_get()

Collection Query

Lists nas cluster info related information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasClustersApi()

try:
    # Collection Query
    api_response = api_instance.nas_cluster_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasClustersApi->nas_cluster_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NasClusterInfo]**](NasClusterInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_clusters_id_delete**
> NasClustersResponse nas_clusters_id_delete(id)

De-register SDNAS cluster from management

Unregister NAS cluster information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasClustersApi()
id = 'id_example' # str | SDNAS cluster id.

try:
    # De-register SDNAS cluster from management
    api_response = api_instance.nas_clusters_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasClustersApi->nas_clusters_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SDNAS cluster id. | 

### Return type

[**NasClustersResponse**](NasClustersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_clusters_id_get**
> NasClusterInfo nas_clusters_id_get(id)

Instance Query

Query a specific SDNAS cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasClustersApi()
id = 'id_example' # str | SDNAS cluster id.

try:
    # Instance Query
    api_response = api_instance.nas_clusters_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasClustersApi->nas_clusters_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SDNAS cluster id. | 

### Return type

[**NasClusterInfo**](NasClusterInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_clusters_id_patch**
> nas_clusters_id_patch(body, id)

Modify

Update newly added NAS node information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasClustersApi()
body = swagger_client.NasClusterModify() # NasClusterModify | 
id = 'id_example' # str | SDNAS cluster id.

try:
    # Modify
    api_instance.nas_clusters_id_patch(body, id)
except ApiException as e:
    print("Exception when calling NasClustersApi->nas_clusters_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NasClusterModify**](NasClusterModify.md)|  | 
 **id** | **str**| SDNAS cluster id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_clusters_post**
> NasClustersCreateResponse nas_clusters_post(body)

Notify new NAS cluster deployment

Register - SDNAS Cluster after successful installation of cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasClustersApi()
body = swagger_client.NasClustersCreate() # NasClustersCreate | 

try:
    # Notify new NAS cluster deployment
    api_response = api_instance.nas_clusters_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasClustersApi->nas_clusters_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NasClustersCreate**](NasClustersCreate.md)|  | 

### Return type

[**NasClustersCreateResponse**](NasClustersCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

