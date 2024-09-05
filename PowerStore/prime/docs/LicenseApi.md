# prime.swagger_client.LicenseApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**license_extend_trial_post**](LicenseApi.md#license_extend_trial_post) | **POST** /license/extend_trial | License trial period extension
[**license_get**](LicenseApi.md#license_get) | **GET** /license | Collection Query
[**license_id_get**](LicenseApi.md#license_id_get) | **GET** /license/{id} | Instance Query
[**license_retrieve_post**](LicenseApi.md#license_retrieve_post) | **POST** /license/retrieve | Retrieve License
[**license_upload_post**](LicenseApi.md#license_upload_post) | **POST** /license/upload | License File Upload


# **license_extend_trial_post**
> license_extend_trial_post()

License trial period extension

Extend license trial period for certain number of days. This runs only allowed once for a appliance, and if it fails, customer can have another try. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LicenseApi()

try:
    # License trial period extension
    api_instance.license_extend_trial_post()
except ApiException as e:
    print("Exception when calling LicenseApi->license_extend_trial_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_get**
> list[LicenseInstance] license_get()

Collection Query

Query license information for the cluster. There is always one license instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LicenseApi()

try:
    # Collection Query
    api_response = api_instance.license_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->license_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LicenseInstance]**](LicenseInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_id_get**
> LicenseInstance license_id_get(id)

Instance Query

Query the specific license information for the cluster.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LicenseApi()
id = 'id_example' # str | Unique identifier of the license information instance.

try:
    # Instance Query
    api_response = api_instance.license_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->license_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the license information instance. | 

### Return type

[**LicenseInstance**](LicenseInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_retrieve_post**
> license_retrieve_post()

Retrieve License

Retrieve the license directly from the DellEMC Software Licensing Central. This runs automatically when the cluster is configured, and if it fails, once per day during the trial period. This allows a manual attempt, normally after attempting to correct the network connectivity issue preventing the automatic retrieval.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LicenseApi()

try:
    # Retrieve License
    api_instance.license_retrieve_post()
except ApiException as e:
    print("Exception when calling LicenseApi->license_retrieve_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_upload_post**
> license_upload_post(license_file=license_file)

License File Upload

Upload a software license to install the license on the cluster.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LicenseApi()
license_file = '/path/to/file.txt' # file | The file to upload containing the software license to install the license on the cluster. (optional)

try:
    # License File Upload
    api_instance.license_upload_post(license_file=license_file)
except ApiException as e:
    print("Exception when calling LicenseApi->license_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_file** | **file**| The file to upload containing the software license to install the license on the cluster. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

