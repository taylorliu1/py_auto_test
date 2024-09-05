# prime.swagger_client.ChapConfigApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chap_config_get**](ChapConfigApi.md#chap_config_get) | **GET** /chap_config | Collection Query
[**chap_config_id_get**](ChapConfigApi.md#chap_config_id_get) | **GET** /chap_config/{id} | Instance Query
[**chap_config_id_patch**](ChapConfigApi.md#chap_config_id_patch) | **PATCH** /chap_config/{id} | Modify


# **chap_config_get**
> list[ChapConfigInstance] chap_config_get()

Collection Query

Query the list of (one) CHAP configuration settings objects.  This resource type collection query does not support filtering, sorting or pagination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ChapConfigApi()

try:
    # Collection Query
    api_response = api_instance.chap_config_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChapConfigApi->chap_config_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ChapConfigInstance]**](ChapConfigInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chap_config_id_get**
> ChapConfigInstance chap_config_id_get(id)

Instance Query

Query the CHAP configuration settings object.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ChapConfigApi()
id = 'id_example' # str | The id of the CHAP configuration object (always \"0\").

try:
    # Instance Query
    api_response = api_instance.chap_config_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChapConfigApi->chap_config_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the CHAP configuration object (always \&quot;0\&quot;). | 

### Return type

[**ChapConfigInstance**](ChapConfigInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chap_config_id_patch**
> chap_config_id_patch(id, body)

Modify

Modify the CHAP configuration settings object. To enable either Single or Mutual CHAP modes, the username and password must already be set, or included in the same request as the new mode.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ChapConfigApi()
id = 'id_example' # str | The id of the CHAP configuration object (always \"0\").
body = prime.swagger_client.ChapConfigModify() # ChapConfigModify | 

try:
    # Modify
    api_instance.chap_config_id_patch(id, body)
except ApiException as e:
    print("Exception when calling ChapConfigApi->chap_config_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the CHAP configuration object (always \&quot;0\&quot;). | 
 **body** | [**ChapConfigModify**](ChapConfigModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

