# swagger_client.NasSnapshotRulesApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nas_snapshot_rules_get**](NasSnapshotRulesApi.md#nas_snapshot_rules_get) | **GET** /nas-snapshot-rules | Collection Query
[**nas_snapshot_rules_id_get**](NasSnapshotRulesApi.md#nas_snapshot_rules_id_get) | **GET** /nas-snapshot-rules/{id} | Instance Query
[**nas_snapshot_rules_post**](NasSnapshotRulesApi.md#nas_snapshot_rules_post) | **POST** /nas-snapshot-rules | Create

# **nas_snapshot_rules_get**
> list[SnapshotRuleInstance] nas_snapshot_rules_get()

Collection Query

Query snapshot rules.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasSnapshotRulesApi()

try:
    # Collection Query
    api_response = api_instance.nas_snapshot_rules_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSnapshotRulesApi->nas_snapshot_rules_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SnapshotRuleInstance]**](SnapshotRuleInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_snapshot_rules_id_get**
> SnapshotRuleInstance nas_snapshot_rules_id_get(id)

Instance Query

Query a specific snapshot rule.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasSnapshotRulesApi()
id = 'id_example' # str | Unique identifier of the snapshot rule.

try:
    # Instance Query
    api_response = api_instance.nas_snapshot_rules_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSnapshotRulesApi->nas_snapshot_rules_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the snapshot rule. | 

### Return type

[**SnapshotRuleInstance**](SnapshotRuleInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_snapshot_rules_post**
> CreateResponse nas_snapshot_rules_post(body)

Create

Create a new snapshot rule.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasSnapshotRulesApi()
body = swagger_client.SnapshotRuleCreate() # SnapshotRuleCreate | 

try:
    # Create
    api_response = api_instance.nas_snapshot_rules_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSnapshotRulesApi->nas_snapshot_rules_post: %s\n" % e)
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

