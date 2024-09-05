# prime.swagger_client.RemoteSystemApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remote_system_get**](RemoteSystemApi.md#remote_system_get) | **GET** /remote_system | Collection Query
[**remote_system_id_delete**](RemoteSystemApi.md#remote_system_id_delete) | **DELETE** /remote_system/{id} | Delete
[**remote_system_id_discover_post**](RemoteSystemApi.md#remote_system_id_discover_post) | **POST** /remote_system/{id}/discover | Discover
[**remote_system_id_get**](RemoteSystemApi.md#remote_system_id_get) | **GET** /remote_system/{id} | Instance Query
[**remote_system_id_patch**](RemoteSystemApi.md#remote_system_id_patch) | **PATCH** /remote_system/{id} | Modify
[**remote_system_id_verify_post**](RemoteSystemApi.md#remote_system_id_verify_post) | **POST** /remote_system/{id}/verify | Verify
[**remote_system_post**](RemoteSystemApi.md#remote_system_post) | **POST** /remote_system | Create


# **remote_system_get**
> list[RemoteSystemInstance] remote_system_get()

Collection Query

Query remote systems. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSystemApi()

try:
    # Collection Query
    api_response = api_instance.remote_system_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteSystemApi->remote_system_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RemoteSystemInstance]**](RemoteSystemInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_system_id_delete**
> remote_system_id_delete(id, body=body)

Delete

Delete a remote system. Deleting the remote system deletes the management and data connections established with the remote system. You cannot delete a remote system if there are active import sessions, or if there are remote protection policies active in the system referencing the remote system instance.     For PowerStore remote systems, the relationship is deleted in both directions if the remote system is up and connectable. You cannot delete a PowerStore remote system if there is no management connectivity between the local and remore systems. Only the local end of the relationship is deleted. Manually log in to the remote PowerStore system and remove the relationship. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSystemApi()
id = 'id_example' # str | Unique identifier of the remote system.  name:{name} can be used instead of {id}.
body = prime.swagger_client.RemoteSystemDelete() # RemoteSystemDelete | Parameters to delete a remote system.  (optional)

try:
    # Delete
    api_instance.remote_system_id_delete(id, body=body)
except ApiException as e:
    print("Exception when calling RemoteSystemApi->remote_system_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the remote system.  name:{name} can be used instead of {id}. | 
 **body** | [**RemoteSystemDelete**](RemoteSystemDelete.md)| Parameters to delete a remote system.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_system_id_discover_post**
> remote_system_id_discover_post(id)

Discover

Discover the importable resources such as volumes, consistency groups, file systems  and snapshot schedules from the remote system. This api is not applicable for PowerStore and cloud type remote systems. For VNX remote system it discovers both block and file resources together if it have both file and block import capabilities.  Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSystemApi()
id = 'id_example' # str | Unique identifier of the remote system.  name:{name} can be used instead of {id}.

try:
    # Discover
    api_instance.remote_system_id_discover_post(id)
except ApiException as e:
    print("Exception when calling RemoteSystemApi->remote_system_id_discover_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the remote system.  name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_system_id_get**
> RemoteSystemInstance remote_system_id_get(id)

Instance Query

Query a remote system instance. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSystemApi()
id = 'id_example' # str | Unique identifier of the remote system.  name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.remote_system_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteSystemApi->remote_system_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the remote system.  name:{name} can be used instead of {id}. | 

### Return type

[**RemoteSystemInstance**](RemoteSystemInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_system_id_patch**
> remote_system_id_patch(id, body)

Modify

Modify a remote system instance. The list of valid parameters depends on the type of remote system. For PowerStore remote system relationships: * Description * Management address - An IPv4 or IPv6 address or FQDN.  For non-PowerStore remote system relationships: * Name * Description * Management address - An IPv4 address or FQDN. * Remote administrator credentials For VNX remote system relationships, file properties such as file_connection_address, vnx_username and password can be provided during modify if it not exists already: * Description * Management address - An IPv4 address. FQDN is not supported. * Remote administrator credentials * File connection address - Control station IPv4 or IPv6 address of the VNX. * NAS admin username * NAS admin password For a PowerMax/VMAX remote system, the attributes that can be modified are * Description * Management address - An IPv4 address. FQDN is not supported. * Remote administrator credentials * Management Port After modifying the remote session instance, the system reestablishes the data connections as needed. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSystemApi()
id = 'id_example' # str | Unique identifier of the remote system.  name:{name} can be used instead of {id}.
body = prime.swagger_client.RemoteSystemModify() # RemoteSystemModify | Parameters to modify the remote system. 

try:
    # Modify
    api_instance.remote_system_id_patch(id, body)
except ApiException as e:
    print("Exception when calling RemoteSystemApi->remote_system_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the remote system.  name:{name} can be used instead of {id}. | 
 **body** | [**RemoteSystemModify**](RemoteSystemModify.md)| Parameters to modify the remote system.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_system_id_verify_post**
> remote_system_id_verify_post(id, body=body)

Verify

Verify and update the remote system instance.     Detects changes in the local and remote systems and reestablishes data connections, also taking the Challenge Handshake Authentication Protocol (CHAP) settings into account for iSCSI. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSystemApi()
id = 'id_example' # str | Unique identifier of the remote system.  name:{name} can be used instead of {id}.
body = prime.swagger_client.RemoteSystemVerify() # RemoteSystemVerify | Parameters to verify a remote system.  (optional)

try:
    # Verify
    api_instance.remote_system_id_verify_post(id, body=body)
except ApiException as e:
    print("Exception when calling RemoteSystemApi->remote_system_id_verify_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the remote system.  name:{name} can be used instead of {id}. | 
 **body** | [**RemoteSystemVerify**](RemoteSystemVerify.md)| Parameters to verify a remote system.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_system_post**
> CreateResponse remote_system_post(body)

Create

Create a new remote system relationship. The type of remote system being connected requires different parameter sets. For PowerStore remote system relationships, include the following parameters: * Management address - Either an IPv4 or IPv6 address or FQDN. * Type of remote system * Data network latency type PowerStore remote system will support Unified (Block and File) by default. For PowerStore remote system relationships, the relationship is created in both directions. Remote protection policies can be configured using the PowerStore remote system instance on either of the systems. This enables remote replication for storage resources in either direction. The data connections take into account whether Challenge Handshake Authentication Protocol (CHAP) is enabled on local and remote PowerStore systems. The PowerStore local system can establish a block import relationship with PS_Equalogic, Unity, Storage_Center, XtremeIO, NetApp, PowerMax/VMAX and VNX . For VNX both block and file import are supported. Unity, Storage_Center, XtremeIO, VNX remote system can be created with data connection type as iSCSI or FC.PS_Equalogic and NetApp can be created with data connection type as iSCSI only.PowerMax/VMAX can be created with data connection type as FC only. For VNX, Unity, PS_Equallogic , Storage_Center, XtremeIO, NetApp remote system relationships with iSCSI as backend connectivity, include the following parameters: * Management address - Either an IPv4 or IPv6 address or FQDN. * Type of remote system * Name * Description * Remote administrator credentials * iSCSI address - IPv4 address * CHAP mode for discovery or session * CHAP secrets details For VNX, Unity, Storage_Center, XtremeIO, PowerMax/VMAX remote system relationships with FC as backend connectivity, include the following parameters: * Management address - Either an IPv4 or IPv6 address or FQDN. * Type of remote system * Name * Description * Remote administrator credentials * Data Connection Type - FC * Management Port - Management port is applicable only for PowerMax/VMAX remote system.  For VNX remote system relationships for file import, include the following parameters along with above block parameters for both block and file import or only below file parameters for File import only cases: * File connection address - Control station IPv4 or IPv6 address of the VNX. * Type of remote system * NAS admin username * NAS admin password * Name * Description Based on the input parameters and the type of remote system, the system will automatically determine the capabilities for  remote systems. Remote Systems storage capabilities currently supported are: * Powerstore - Asynchronous_Block_Replication, Asynchronous_File_Replication, Asynchronous_Vvol_Replication * Unity - Block_Nondisruptive_Import, Block_Agentless_Import * VNX - Block_Nondisruptive_Import, Block_Agentless_Import, File_Import * PS_Equallogic - Block_Nondisruptive_Import, Block_Agentless_Import * Storage_Center - Block_Nondisruptive_Import, Block_Agentless_Import * XtremIO - Block_Agentless_Import * NetApp - Block_Agentless_Import * PowerMax/VMAX - Block_Agentless_Import  After the remote system relationship is created, the local system can communicate with the remote system, and open data connections for data transfer. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSystemApi()
body = prime.swagger_client.RemoteSystemCreate() # RemoteSystemCreate | Parameters to create a remote system. 

try:
    # Create
    api_response = api_instance.remote_system_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteSystemApi->remote_system_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteSystemCreate**](RemoteSystemCreate.md)| Parameters to create a remote system.  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

