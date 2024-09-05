# prime.swagger_client.SoftwarePackageApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**software_package_get**](SoftwarePackageApi.md#software_package_get) | **GET** /software_package | Collection Query
[**software_package_id_delete**](SoftwarePackageApi.md#software_package_id_delete) | **DELETE** /software_package/{id} | Delete
[**software_package_id_get**](SoftwarePackageApi.md#software_package_id_get) | **GET** /software_package/{id} | Instance Query
[**software_package_id_install_post**](SoftwarePackageApi.md#software_package_id_install_post) | **POST** /software_package/{id}/install | Start Upgrade
[**software_package_id_puhc_post**](SoftwarePackageApi.md#software_package_id_puhc_post) | **POST** /software_package/{id}/puhc | Pre-upgrade Health Check
[**software_package_post**](SoftwarePackageApi.md#software_package_post) | **POST** /software_package | Upload


# **software_package_get**
> list[SoftwarePackageInstance] software_package_get()

Collection Query

Query the software packages that are known by the cluster. The output returns a list of JSON objects representing the packages.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SoftwarePackageApi()

try:
    # Collection Query
    api_response = api_instance.software_package_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwarePackageApi->software_package_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SoftwarePackageInstance]**](SoftwarePackageInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_package_id_delete**
> JobResponse software_package_id_delete(id)

Delete

Delete the specified software package from the cluster. This operation may take some time to complete.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SoftwarePackageApi()
id = 'id_example' # str | Unique identifier of the software package to delete. name:{name} can be used instead of {id}.

try:
    # Delete
    api_response = api_instance.software_package_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwarePackageApi->software_package_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the software package to delete. name:{name} can be used instead of {id}. | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_package_id_get**
> SoftwarePackageInstance software_package_id_get(id)

Instance Query

Query a specific software package.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SoftwarePackageApi()
id = 'id_example' # str | Unique identifier of the software package to query. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.software_package_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwarePackageApi->software_package_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the software package to query. name:{name} can be used instead of {id}. | 

### Return type

[**SoftwarePackageInstance**](SoftwarePackageInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_package_id_install_post**
> software_package_id_install_post(id, body=body)

Start Upgrade

Start a software upgrade background job for the specified appliance within the cluster. If an  appliance is not specified, the upgrade is performed on all appliances in the cluster.    Only specify a subset of appliances to upgrade if the time required to upgrade the entire cluster does not fit within a desired maintenance window. When upgrading a subset of appliances, you must adhere to the following ordering rules:    * The primary appliance must always be upgraded first. * The secondary appliance, which is used as the cluster management database fail-over target, must be upgraded second. * After the primary and secondary appliances are upgraded, any remaining appliances in the cluster may be upgraded. By default, the process upgrades the appliances in the order they were added to the cluster if possible.    Because this operation takes a long time to complete, using the \"is_async flag\" is recommended. If the \"is_reboot_required\" flag is set to true, the primary appliance reboots before the install completes and the operation cannot return synchronously. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SoftwarePackageApi()
id = 'id_example' # str | Unique identifier of the instance. name:{name} can be used instead of {id}.
body = prime.swagger_client.SoftwarePackageInstall() # SoftwarePackageInstall |  (optional)

try:
    # Start Upgrade
    api_instance.software_package_id_install_post(id, body=body)
except ApiException as e:
    print("Exception when calling SoftwarePackageApi->software_package_id_install_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the instance. name:{name} can be used instead of {id}. | 
 **body** | [**SoftwarePackageInstall**](SoftwarePackageInstall.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_package_id_puhc_post**
> software_package_id_puhc_post(id, body=body)

Pre-upgrade Health Check

Run the pre-upgrade health check for a software package. This operation may take some time to respond.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SoftwarePackageApi()
id = 'id_example' # str | Unique identifier of the software package. name:{name} can be used instead of {id}.
body = prime.swagger_client.SoftwarePackagePuhc() # SoftwarePackagePuhc |  (optional)

try:
    # Pre-upgrade Health Check
    api_instance.software_package_id_puhc_post(id, body=body)
except ApiException as e:
    print("Exception when calling SoftwarePackageApi->software_package_id_puhc_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the software package. name:{name} can be used instead of {id}. | 
 **body** | [**SoftwarePackagePuhc**](SoftwarePackagePuhc.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_package_post**
> CreateResponse software_package_post(upload_file=upload_file)

Upload

Push a software package file from the client to the cluster. When successfully uploaded and verified, the result is a software_package in the downloaded state, ready to install.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SoftwarePackageApi()
upload_file = '/path/to/file.txt' # file | Name of the software package file to upload. (optional)

try:
    # Upload
    api_response = api_instance.software_package_post(upload_file=upload_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwarePackageApi->software_package_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_file** | **file**| Name of the software package file to upload. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

