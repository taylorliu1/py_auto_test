# prime.swagger_client.ReplicationRuleApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replication_rule_get**](ReplicationRuleApi.md#replication_rule_get) | **GET** /replication_rule | Collection Query
[**replication_rule_id_clone_post**](ReplicationRuleApi.md#replication_rule_id_clone_post) | **POST** /replication_rule/{id}/clone | Clone
[**replication_rule_id_delete**](ReplicationRuleApi.md#replication_rule_id_delete) | **DELETE** /replication_rule/{id} | Delete
[**replication_rule_id_get**](ReplicationRuleApi.md#replication_rule_id_get) | **GET** /replication_rule/{id} | Instance Query
[**replication_rule_id_patch**](ReplicationRuleApi.md#replication_rule_id_patch) | **PATCH** /replication_rule/{id} | Modify
[**replication_rule_post**](ReplicationRuleApi.md#replication_rule_post) | **POST** /replication_rule | Create


# **replication_rule_get**
> list[ReplicationRuleInstance] replication_rule_get()

Collection Query

Query all replication rules.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationRuleApi()

try:
    # Collection Query
    api_response = api_instance.replication_rule_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationRuleApi->replication_rule_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ReplicationRuleInstance]**](ReplicationRuleInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_rule_id_clone_post**
> ReplicationRuleCloneResponse replication_rule_id_clone_post(id, body)

Clone

Clone a replication rule. Creates an identical copy of the specified replication rule. The newly created replication rule will be a read-write, user-managed replication rule.  Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationRuleApi()
id = 'id_example' # str | Unique identifier of the replication rule to be cloned. name:{name} can be used instead of {id}.
body = prime.swagger_client.ReplicationRuleClone() # ReplicationRuleClone | 

try:
    # Clone
    api_response = api_instance.replication_rule_id_clone_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationRuleApi->replication_rule_id_clone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication rule to be cloned. name:{name} can be used instead of {id}. | 
 **body** | [**ReplicationRuleClone**](ReplicationRuleClone.md)|  | 

### Return type

[**ReplicationRuleCloneResponse**](ReplicationRuleCloneResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_rule_id_delete**
> replication_rule_id_delete(id)

Delete

Delete a replication rule. Deleting a replication rule is not allowed if the replication rule is associated with a protection policy that is currently assigned to one or more storage resources. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationRuleApi()
id = 'id_example' # str | Unique identifier of the replication rule. name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.replication_rule_id_delete(id)
except ApiException as e:
    print("Exception when calling ReplicationRuleApi->replication_rule_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication rule. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_rule_id_get**
> ReplicationRuleInstance replication_rule_id_get(id)

Instance Query

Query a specific replication rule.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationRuleApi()
id = 'id_example' # str | Unique identifier of the replication rule. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.replication_rule_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationRuleApi->replication_rule_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication rule. name:{name} can be used instead of {id}. | 

### Return type

[**ReplicationRuleInstance**](ReplicationRuleInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_rule_id_patch**
> replication_rule_id_patch(id, body=body)

Modify

Modify a replication rule. If the replication rule is associated with a policy that is currently applied to a storage resource, the modified rule is immediately applied to the associated storage resource. However, changing the remote_system_id is not allowed if the replication rule is included in a policy that is currently applied to a storage resource. To change the remote_system_id in this case, please follow one of the following procedures:   - Unassign the protection policy from the relevant storage resources, modify the replication rule, and then re-assign the protection policy to the relevant storage resources.   - Remove the replication rule from the protection policies that use it, modify the replication rule, and then add it back to the relevant protection policies. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationRuleApi()
id = 'id_example' # str | Unique identifier of the replication rule. name:{name} can be used instead of {id}.
body = prime.swagger_client.ReplicationRuleModify() # ReplicationRuleModify |  (optional)

try:
    # Modify
    api_instance.replication_rule_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling ReplicationRuleApi->replication_rule_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication rule. name:{name} can be used instead of {id}. | 
 **body** | [**ReplicationRuleModify**](ReplicationRuleModify.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_rule_post**
> CreateResponse replication_rule_post(body)

Create

Create a new replication rule. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationRuleApi()
body = prime.swagger_client.ReplicationRuleCreate() # ReplicationRuleCreate | 

try:
    # Create
    api_response = api_instance.replication_rule_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationRuleApi->replication_rule_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplicationRuleCreate**](ReplicationRuleCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

