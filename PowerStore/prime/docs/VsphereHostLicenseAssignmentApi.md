# prime.swagger_client.VsphereHostLicenseAssignmentApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vsphere_host_license_assignment_get**](VsphereHostLicenseAssignmentApi.md#vsphere_host_license_assignment_get) | **GET** /vsphere_host_license_assignment | Collection Query
[**vsphere_host_license_assignment_id_get**](VsphereHostLicenseAssignmentApi.md#vsphere_host_license_assignment_id_get) | **GET** /vsphere_host_license_assignment/{id} | Instance Query


# **vsphere_host_license_assignment_get**
> list[VsphereHostLicenseAssignmentInstance] vsphere_host_license_assignment_get()

Collection Query

Query information about ESXi hosts license assignments in vCenter. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VsphereHostLicenseAssignmentApi()

try:
    # Collection Query
    api_response = api_instance.vsphere_host_license_assignment_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VsphereHostLicenseAssignmentApi->vsphere_host_license_assignment_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VsphereHostLicenseAssignmentInstance]**](VsphereHostLicenseAssignmentInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vsphere_host_license_assignment_id_get**
> VsphereHostLicenseAssignmentInstance vsphere_host_license_assignment_id_get(id)

Instance Query

Query a specific vsphere_host_license_assignment instance. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VsphereHostLicenseAssignmentApi()
id = 'id_example' # str | Unique identifier of the vsphere_host_license_assignment to query license. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.vsphere_host_license_assignment_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VsphereHostLicenseAssignmentApi->vsphere_host_license_assignment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the vsphere_host_license_assignment to query license. name:{name} can be used instead of {id}. | 

### Return type

[**VsphereHostLicenseAssignmentInstance**](VsphereHostLicenseAssignmentInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

