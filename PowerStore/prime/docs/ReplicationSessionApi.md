# prime.swagger_client.ReplicationSessionApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replication_session_get**](ReplicationSessionApi.md#replication_session_get) | **GET** /replication_session | Collection Query
[**replication_session_id_demote_post**](ReplicationSessionApi.md#replication_session_id_demote_post) | **POST** /replication_session/{id}/demote | Demote replication session
[**replication_session_id_failover_post**](ReplicationSessionApi.md#replication_session_id_failover_post) | **POST** /replication_session/{id}/failover | Failover
[**replication_session_id_get**](ReplicationSessionApi.md#replication_session_id_get) | **GET** /replication_session/{id} | Instance Query
[**replication_session_id_pause_post**](ReplicationSessionApi.md#replication_session_id_pause_post) | **POST** /replication_session/{id}/pause | Pause
[**replication_session_id_promote_post**](ReplicationSessionApi.md#replication_session_id_promote_post) | **POST** /replication_session/{id}/promote | Promote replication session
[**replication_session_id_reprotect_post**](ReplicationSessionApi.md#replication_session_id_reprotect_post) | **POST** /replication_session/{id}/reprotect | Reprotect
[**replication_session_id_resume_post**](ReplicationSessionApi.md#replication_session_id_resume_post) | **POST** /replication_session/{id}/resume | Resume
[**replication_session_id_start_failover_test_post**](ReplicationSessionApi.md#replication_session_id_start_failover_test_post) | **POST** /replication_session/{id}/start_failover_test | Start DR Failover Simulation Test
[**replication_session_id_stop_failover_test_post**](ReplicationSessionApi.md#replication_session_id_stop_failover_test_post) | **POST** /replication_session/{id}/stop_failover_test | Stop DR Failover Simulation Test
[**replication_session_id_sync_post**](ReplicationSessionApi.md#replication_session_id_sync_post) | **POST** /replication_session/{id}/sync | Synchronize


# **replication_session_get**
> list[ReplicationSessionInstance] replication_session_get()

Collection Query

Query replication sessions. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationSessionApi()

try:
    # Collection Query
    api_response = api_instance.replication_session_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationSessionApi->replication_session_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ReplicationSessionInstance]**](ReplicationSessionInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_session_id_demote_post**
> replication_session_id_demote_post(id, body=body)

Demote replication session

This is to demote a local resource to make it unavailable. This is used in specific failure scenario where user needs ability to move a preferred side local resource into unavailable state. The local_resource_state property on the session instance will indicate that the local side of the metro session was demoted through user action.  Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationSessionApi()
id = 'id_example' # str | Unique identifier of the replication session.  Was added in version 3.0.0.0.
body = prime.swagger_client.ReplicationSessionDemote() # ReplicationSessionDemote | Parameters to demote a replication session. (optional)

try:
    # Demote replication session
    api_instance.replication_session_id_demote_post(id, body=body)
except ApiException as e:
    print("Exception when calling ReplicationSessionApi->replication_session_id_demote_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication session.  Was added in version 3.0.0.0. | 
 **body** | [**ReplicationSessionDemote**](ReplicationSessionDemote.md)| Parameters to demote a replication session. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_session_id_failover_post**
> replication_session_id_failover_post(id, body=body)

Failover

Fail over a replication session instance of type Asynchronous. Failing over the replication session changes the role of the destination system. After a failover, the original destination system becomes the source system, and production access is enabled for hosts and applications for recovery. Failovers can be planned or unplanned.     Planned failovers are issued from the source system and are indicated by setting the is_planned parameter to true. When you fail over a replication session from the source system, the destination system is fully synchronized with the source to ensure that there is no data loss. During a planned failover, stop I/O operations for any applications and hosts. If a synchronization error occurs during a planned failover, the replication session enters the System_Paused state. You cannot pause a replication session during a planned failover. The following operations can be performed during planned failover: * Unplanned failover * Delete the replication session by removing the protection policy on the storage resource     Failover (planned or unplanned) cannot be performed when a test failover is in progress.     After a planned failover, the replication session is in an inactive state. You can use the reprotect action to synchronize the destination storage resource, and then resume the replication session. The auto-reprotect feature can also be used after a planned failover by using the reverse parameter, which activates the session in the reverse direction.     Unplanned failures are events such as source system failure or an event on the source system that leads to downtime for production access.     Unplanned failovers are issued from the destination system, and are indicated by setting the is_planned parameter to false. Unplanned failovers provide production access to the original destination resource from a preview synchronized point-in-time snapshot referred to as replication common-base. After an unplanned failover, you can restore the system from any point-in-time snapshots on the new source resource. Unplanned failovers place the original source resource into destination mode once it reestablishes a connection to the source system.  You can use the reprotect action to synchronize the destination storage resource, and then resume the replication session.     After the replication session has failed over, you can resize the volume group or change the volume group membership on the new source resource. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationSessionApi()
id = 'id_example' # str | Unique identifier of the replication session. 
body = prime.swagger_client.ReplicationSessionFailover() # ReplicationSessionFailover |  (optional)

try:
    # Failover
    api_instance.replication_session_id_failover_post(id, body=body)
except ApiException as e:
    print("Exception when calling ReplicationSessionApi->replication_session_id_failover_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication session.  | 
 **body** | [**ReplicationSessionFailover**](ReplicationSessionFailover.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_session_id_get**
> ReplicationSessionInstance replication_session_id_get(id)

Instance Query

Query a replication session instance. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationSessionApi()
id = 'id_example' # str | Unique identifier of the replication session. 

try:
    # Instance Query
    api_response = api_instance.replication_session_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationSessionApi->replication_session_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication session.  | 

### Return type

[**ReplicationSessionInstance**](ReplicationSessionInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_session_id_pause_post**
> replication_session_id_pause_post(id)

Pause

Pause a replication session instance. You can pause a replication session for maintenance activities on local or remote system.     The session can be paused when it is in the following states: * OK * Synchronizing * System_Paused * Fractured     In case of loss of network connectivity between two sites, the replication session is paused only on the local system where it is issued. Pause the replication session again to pause both sites. The following operations are not allowed while only the replication session on the local system is paused: * Resume * Sync * Planned Failover     The following operations are allowed while only the replication session on the local system is paused: * Pause - Use to place both sites into the **Paused** state * Failover - Use to get production access from the disaster recovery site * Promote - Use to get production access from local cluster * Demote - Use to remove production access from local cluster * Delete - Delete the replication session     The following system operations may also pause, and subsequently resume, a replication session: * Non-disruptive upgrade * Intra-cluster migration     Leaving replication session in a paused state results in change accumulations on the production mode system. Resuming a replication session that has been paused for a long time can result in long synchronization times. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationSessionApi()
id = 'id_example' # str | Unique identifier of the replication session. 

try:
    # Pause
    api_instance.replication_session_id_pause_post(id)
except ApiException as e:
    print("Exception when calling ReplicationSessionApi->replication_session_id_pause_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication session.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_session_id_promote_post**
> replication_session_id_promote_post(id, body=body)

Promote replication session

Promote a metro type replication session to enable production access to the resource on the local side of the metro session. The local resource is granted production access independent of its preferred or non-preferred role in the metro relationship. This operation does not change the state of the Metro session. The local_resource_state property on the session instance will indicate that the local side of the metro session was promoted through user action. A snapshot of the local resource will be created before the promote operation. The expiration time of this snapshot will be set to 3 days. This operation can be performed only when the metro session is in the Fractured or Paused states.  Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationSessionApi()
id = 'id_example' # str | Unique identifier of the replication session.  Was added in version 3.0.0.0.
body = prime.swagger_client.ReplicationSessionPromote() # ReplicationSessionPromote | Parameters to promote a replication session. (optional)

try:
    # Promote replication session
    api_instance.replication_session_id_promote_post(id, body=body)
except ApiException as e:
    print("Exception when calling ReplicationSessionApi->replication_session_id_promote_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication session.  Was added in version 3.0.0.0. | 
 **body** | [**ReplicationSessionPromote**](ReplicationSessionPromote.md)| Parameters to promote a replication session. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_session_id_reprotect_post**
> replication_session_id_reprotect_post(id)

Reprotect

Reprotect a replication session instance of type Asynchronous. Activates the replication session and starts synchronization. For session of type Asynchronous, this can only be used when the session has been failed over and from the system that is reported as source. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationSessionApi()
id = 'id_example' # str | Unique identifier of the replication session. 

try:
    # Reprotect
    api_instance.replication_session_id_reprotect_post(id)
except ApiException as e:
    print("Exception when calling ReplicationSessionApi->replication_session_id_reprotect_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication session.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_session_id_resume_post**
> replication_session_id_resume_post(id)

Resume

Resume a replication session instance that is paused. Resuming the replication session initiates a synchronization cycle if the session was in the following states when the session was paused: * Synchronizing * System_Paused * Fractured     You cannot resume replication sessions paused by the system. The following system operations may also pause, and subsequently resume, a replication session. * Paused_for_NDU * Paused_for_Migration 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationSessionApi()
id = 'id_example' # str | Unique identifier of the replication session. 

try:
    # Resume
    api_instance.replication_session_id_resume_post(id)
except ApiException as e:
    print("Exception when calling ReplicationSessionApi->replication_session_id_resume_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication session.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_session_id_start_failover_test_post**
> replication_session_id_start_failover_test_post(id, body=body)

Start DR Failover Simulation Test

Start a disaster recovery (DR) failover simulation test at the destination site of a replication session of type Asynchronous to simulate a failover and grant production access to the destination resource. This will enable DR site hosts to access the destination site resource and allow users to test their DR configuration and readiness without interrupting activity at the production site. Replication synchronization activity from the production site will continue to happen while the test is in progress except for the actual synchronization of the destination resource with the primary. Any changes made to the destination resource during the test, including resizing, can be optionally saved in a snapshot at the end of the test, at which point the destination resource will revert to its normal state and role.  Starting of a DR failover simulation test is allowed only at the destination site of a replication session and only when the session is in the following states: * OK * Synchronizing * Paused * System_Paused   This operation is not allowed when a test failover is already in progress on the replication session or if the session is in the following states: * Planned_Failover_In_Progress * DR_Failover_In_Progress * Failed_Over * Paused_For_NDU * Paused_For_Migration   During the test, the following restrictions apply: * Membership changes are not allowed for destination resources that belong to a volume group. * The session cannot be failed over (planned or unplanned).  Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationSessionApi()
id = 'id_example' # str | Unique identifier of the replication session.  Was added in version 2.0.0.0.
body = prime.swagger_client.ReplicationStartFailoverTest() # ReplicationStartFailoverTest | Parameters to start a DR failover simulation test on a replication session. (optional)

try:
    # Start DR Failover Simulation Test
    api_instance.replication_session_id_start_failover_test_post(id, body=body)
except ApiException as e:
    print("Exception when calling ReplicationSessionApi->replication_session_id_start_failover_test_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication session.  Was added in version 2.0.0.0. | 
 **body** | [**ReplicationStartFailoverTest**](ReplicationStartFailoverTest.md)| Parameters to start a DR failover simulation test on a replication session. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_session_id_stop_failover_test_post**
> ReplicationSessionStopFailoverTestResponse replication_session_id_stop_failover_test_post(id, body=body)

Stop DR Failover Simulation Test

Stop a disaster recovery (DR) failover simulation test that is in progress at the destination site of a replication session of type Asynchronous and revert the destination resource to its normal state and role.  Stopping of a DR failover simulation test is allowed only at the destination site of a replication session and only when a test failover is in progress on the replication session.  Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationSessionApi()
id = 'id_example' # str | Unique identifier of the replication session.  Was added in version 2.0.0.0.
body = prime.swagger_client.ReplicationStopFailoverTest() # ReplicationStopFailoverTest | Parameters to stop a DR failover simulation test on a replication session. (optional)

try:
    # Stop DR Failover Simulation Test
    api_response = api_instance.replication_session_id_stop_failover_test_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationSessionApi->replication_session_id_stop_failover_test_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication session.  Was added in version 2.0.0.0. | 
 **body** | [**ReplicationStopFailoverTest**](ReplicationStopFailoverTest.md)| Parameters to stop a DR failover simulation test on a replication session. | [optional] 

### Return type

[**ReplicationSessionStopFailoverTestResponse**](ReplicationSessionStopFailoverTestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_session_id_sync_post**
> replication_session_id_sync_post(id)

Synchronize

Supported for Asynchronous type replication sessions. Synchronize the destination resource with changes on source resource from the previous synchronization cycle.    Also synchronizes any size changes, membership changes, or both, on the source resource. At the end of the synchronization cycle, the destination resource reflects the state as it was when synchronization began. Any size changes, membership changes, or both, to source resource done during the synchronization cycle are replicated in next synchronization cycle.     Synchronization is allowed when the replication session is in the following states: * OK * System_Paused     During synchronization, you can take the following actions: * Planned failover from the source system * Failover from the destination system * Pause replication sessions from the source or destination system * Delete a replication session by removing a protection policy     Synchronization failure places the replication session in a System_Paused state. When the system recovers, the replication session continues from the same point as when the system paused, using the restart address. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationSessionApi()
id = 'id_example' # str | Unique identifier of the replication session. 

try:
    # Synchronize
    api_instance.replication_session_id_sync_post(id)
except ApiException as e:
    print("Exception when calling ReplicationSessionApi->replication_session_id_sync_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication session.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

