# swagger_client.NasProtectionPoliciesApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nas_protection_policies_get**](NasProtectionPoliciesApi.md#nas_protection_policies_get) | **GET** /nas-protection-policies | Collection Query
[**nas_protection_policies_id_get**](NasProtectionPoliciesApi.md#nas_protection_policies_id_get) | **GET** /nas-protection-policies/{id} | Instance Query
[**nas_protection_policies_post**](NasProtectionPoliciesApi.md#nas_protection_policies_post) | **POST** /nas-protection-policies | Create

# **nas_protection_policies_get**
> list[ProtectionPolicyInstance] nas_protection_policies_get()

Collection Query

Query protection policies.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasProtectionPoliciesApi()

try:
    # Collection Query
    api_response = api_instance.nas_protection_policies_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasProtectionPoliciesApi->nas_protection_policies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProtectionPolicyInstance]**](ProtectionPolicyInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_protection_policies_id_get**
> ProtectionPolicyInstance nas_protection_policies_id_get(id)

Instance Query

Query a specific protection policy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasProtectionPoliciesApi()
id = 'id_example' # str | Unique identifier of the protection policy.

try:
    # Instance Query
    api_response = api_instance.nas_protection_policies_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasProtectionPoliciesApi->nas_protection_policies_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the protection policy. | 

### Return type

[**ProtectionPolicyInstance**](ProtectionPolicyInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_protection_policies_post**
> CreateResponse nas_protection_policies_post(body)

Create

Create a new protection policy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasProtectionPoliciesApi()
body = swagger_client.ProtectionPolicyInstance() # ProtectionPolicyInstance | 

try:
    # Create
    api_response = api_instance.nas_protection_policies_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasProtectionPoliciesApi->nas_protection_policies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtectionPolicyInstance**](ProtectionPolicyInstance.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

