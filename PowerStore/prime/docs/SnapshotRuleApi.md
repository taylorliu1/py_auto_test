# prime.swagger_client.SnapshotRuleApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**snapshot_rule_get**](SnapshotRuleApi.md#snapshot_rule_get) | **GET** /snapshot_rule | Collection Query
[**snapshot_rule_id_clone_post**](SnapshotRuleApi.md#snapshot_rule_id_clone_post) | **POST** /snapshot_rule/{id}/clone | Clone
[**snapshot_rule_id_delete**](SnapshotRuleApi.md#snapshot_rule_id_delete) | **DELETE** /snapshot_rule/{id} | Delete
[**snapshot_rule_id_get**](SnapshotRuleApi.md#snapshot_rule_id_get) | **GET** /snapshot_rule/{id} | Instance Query
[**snapshot_rule_id_patch**](SnapshotRuleApi.md#snapshot_rule_id_patch) | **PATCH** /snapshot_rule/{id} | Modify
[**snapshot_rule_post**](SnapshotRuleApi.md#snapshot_rule_post) | **POST** /snapshot_rule | Create


# **snapshot_rule_get**
> list[SnapshotRuleInstance] snapshot_rule_get()

Collection Query

Query all snapshot rules.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SnapshotRuleApi()

try:
    # Collection Query
    api_response = api_instance.snapshot_rule_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotRuleApi->snapshot_rule_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SnapshotRuleInstance]**](SnapshotRuleInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_rule_id_clone_post**
> SnapshotRuleCloneResponse snapshot_rule_id_clone_post(id, body)

Clone

Clone a snapshot rule, which creates an identical copy of this snapshot rule. The resulting snapshot rule will be read-write and managed by the user.  Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SnapshotRuleApi()
id = 'id_example' # str | Unique identifier of the snapshot rule to be cloned. name:{name} can be used instead of {id}.
body = prime.swagger_client.SnapshotRuleClone() # SnapshotRuleClone | 

try:
    # Clone
    api_response = api_instance.snapshot_rule_id_clone_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotRuleApi->snapshot_rule_id_clone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the snapshot rule to be cloned. name:{name} can be used instead of {id}. | 
 **body** | [**SnapshotRuleClone**](SnapshotRuleClone.md)|  | 

### Return type

[**SnapshotRuleCloneResponse**](SnapshotRuleCloneResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_rule_id_delete**
> snapshot_rule_id_delete(id, body=body)

Delete

Delete a snapshot rule. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SnapshotRuleApi()
id = 'id_example' # str | Unique identifier of the snapshot rule. name:{name} can be used instead of {id}.
body = prime.swagger_client.SnapshotRuleDelete() # SnapshotRuleDelete |  (optional)

try:
    # Delete
    api_instance.snapshot_rule_id_delete(id, body=body)
except ApiException as e:
    print("Exception when calling SnapshotRuleApi->snapshot_rule_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the snapshot rule. name:{name} can be used instead of {id}. | 
 **body** | [**SnapshotRuleDelete**](SnapshotRuleDelete.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_rule_id_get**
> SnapshotRuleInstance snapshot_rule_id_get(id)

Instance Query

Query a specific snapshot rule.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SnapshotRuleApi()
id = 'id_example' # str | Unique identifier of the snapshot rule. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.snapshot_rule_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotRuleApi->snapshot_rule_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the snapshot rule. name:{name} can be used instead of {id}. | 

### Return type

[**SnapshotRuleInstance**](SnapshotRuleInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_rule_id_patch**
> snapshot_rule_id_patch(id, body=body)

Modify

Modify a snapshot rule. If the snapshot rule is associated with a policy that is currently applied to a storage resource, the modified rule is immediately applied to the associated storage resource. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SnapshotRuleApi()
id = 'id_example' # str | Unique identifier of the snapshot rule. name:{name} can be used instead of {id}.
body = prime.swagger_client.SnapshotRuleModify() # SnapshotRuleModify |  (optional)

try:
    # Modify
    api_instance.snapshot_rule_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling SnapshotRuleApi->snapshot_rule_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the snapshot rule. name:{name} can be used instead of {id}. | 
 **body** | [**SnapshotRuleModify**](SnapshotRuleModify.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_rule_post**
> CreateResponse snapshot_rule_post(body)

Create

Create a new snapshot rule. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SnapshotRuleApi()
body = prime.swagger_client.SnapshotRuleCreate() # SnapshotRuleCreate | 

try:
    # Create
    api_response = api_instance.snapshot_rule_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotRuleApi->snapshot_rule_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SnapshotRuleCreate**](SnapshotRuleCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

