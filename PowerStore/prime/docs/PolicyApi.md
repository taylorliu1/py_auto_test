# prime.swagger_client.PolicyApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policy_get**](PolicyApi.md#policy_get) | **GET** /policy | Collection Query
[**policy_id_clone_post**](PolicyApi.md#policy_id_clone_post) | **POST** /policy/{id}/clone | Clone
[**policy_id_delete**](PolicyApi.md#policy_id_delete) | **DELETE** /policy/{id} | Delete
[**policy_id_get**](PolicyApi.md#policy_id_get) | **GET** /policy/{id} | Instance Query
[**policy_id_patch**](PolicyApi.md#policy_id_patch) | **PATCH** /policy/{id} | Modify
[**policy_post**](PolicyApi.md#policy_post) | **POST** /policy | Create


# **policy_get**
> list[PolicyInstance] policy_get()

Collection Query

Query protection and performance policies.  The following REST query is an example of how to retrieve protection policies along with their rules and associated storage resources:  `https://{{cluster_ip}}/api/rest/policy?select=name,id,type,replication_rules(id,name,rpo,remote_system(id,name,management_address)),snapshot_rules(id,name,interval,time_of_day,days_of_week),volume(id,name),volume_group(id,name)&type=eq.Protection`  The following REST query is an example of how to retrieve performance policies along with their associated resources:    `https://{{cluster_ip}}/api/rest/policy?select=name,id,type,volume(id,name),volume_group(id,name)&type=eq.Performance` 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.PolicyApi()

try:
    # Collection Query
    api_response = api_instance.policy_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->policy_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PolicyInstance]**](PolicyInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_id_clone_post**
> PolicyCloneResponse policy_id_clone_post(id, body)

Clone

Clone a protection policy. Creates an identical copy of this protection policy along with cloned copies of this policy's rules. The clone will be a read-write, user-managed protection policy.  Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.PolicyApi()
id = 'id_example' # str | Unique identifier of the protection policy to be cloned. name:{name} can be used instead of {id}.
body = prime.swagger_client.PolicyClone() # PolicyClone | 

try:
    # Clone
    api_response = api_instance.policy_id_clone_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->policy_id_clone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the protection policy to be cloned. name:{name} can be used instead of {id}. | 
 **body** | [**PolicyClone**](PolicyClone.md)|  | 

### Return type

[**PolicyCloneResponse**](PolicyCloneResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_id_delete**
> policy_id_delete(id)

Delete

Delete a protection policy.  Protection policies cannot be deleted if they are assigned to a storage resource. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.PolicyApi()
id = 'id_example' # str | Unique identifier of the protection policy to be deleted. name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.policy_id_delete(id)
except ApiException as e:
    print("Exception when calling PolicyApi->policy_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the protection policy to be deleted. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_id_get**
> PolicyInstance policy_id_get(id)

Instance Query

Query a specific policy.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.PolicyApi()
id = 'id_example' # str | Unique identifier of the policy. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.policy_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->policy_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the policy. name:{name} can be used instead of {id}. | 

### Return type

[**PolicyInstance**](PolicyInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_id_patch**
> policy_id_patch(id, body=body)

Modify

Modify a protection policy. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.PolicyApi()
id = 'id_example' # str | Unique identifier of the protection policy to be modified. name:{name} can be used instead of {id}.
body = prime.swagger_client.PolicyModify() # PolicyModify |  (optional)

try:
    # Modify
    api_instance.policy_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling PolicyApi->policy_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the protection policy to be modified. name:{name} can be used instead of {id}. | 
 **body** | [**PolicyModify**](PolicyModify.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_post**
> CreateResponse policy_post(body)

Create

Create a new protection policy. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.PolicyApi()
body = prime.swagger_client.PolicyCreate() # PolicyCreate | 

try:
    # Create
    api_response = api_instance.policy_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->policy_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyCreate**](PolicyCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

