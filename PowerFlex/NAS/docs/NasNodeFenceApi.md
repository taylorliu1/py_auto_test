# swagger_client.NasNodeFenceApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nas_clusters_id_fence_node_post**](NasNodeFenceApi.md#nas_clusters_id_fence_node_post) | **POST** /nas-clusters/{id}/fence-node | Mark Node for fencing

# **nas_clusters_id_fence_node_post**
> NasClustersFenceNodeResponse nas_clusters_id_fence_node_post(body, id)

Mark Node for fencing

Mark NAS Node for either suicide or hard fencing

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasNodeFenceApi()
body = swagger_client.NasNodesFenceCreate() # NasNodesFenceCreate | 
id = 'id_example' # str | Unique identifier of SDNAS cluster.

try:
    # Mark Node for fencing
    api_response = api_instance.nas_clusters_id_fence_node_post(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasNodeFenceApi->nas_clusters_id_fence_node_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NasNodesFenceCreate**](NasNodesFenceCreate.md)|  | 
 **id** | **str**| Unique identifier of SDNAS cluster. | 

### Return type

[**NasClustersFenceNodeResponse**](NasClustersFenceNodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

