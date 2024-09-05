# prime.swagger_client.MigrationRecommendationApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**migration_recommendation_get**](MigrationRecommendationApi.md#migration_recommendation_get) | **GET** /migration_recommendation | Collection query
[**migration_recommendation_id_create_migration_sessions_post**](MigrationRecommendationApi.md#migration_recommendation_id_create_migration_sessions_post) | **POST** /migration_recommendation/{id}/create_migration_sessions | Create migrations
[**migration_recommendation_id_delete**](MigrationRecommendationApi.md#migration_recommendation_id_delete) | **DELETE** /migration_recommendation/{id} | Delete
[**migration_recommendation_id_get**](MigrationRecommendationApi.md#migration_recommendation_id_get) | **GET** /migration_recommendation/{id} | Instance query
[**migration_recommendation_id_patch**](MigrationRecommendationApi.md#migration_recommendation_id_patch) | **PATCH** /migration_recommendation/{id} | Modify
[**migration_recommendation_id_start_migration_sessions_post**](MigrationRecommendationApi.md#migration_recommendation_id_start_migration_sessions_post) | **POST** /migration_recommendation/{id}/start_migration_sessions | Start migrations
[**migration_recommendation_post**](MigrationRecommendationApi.md#migration_recommendation_post) | **POST** /migration_recommendation | Create


# **migration_recommendation_get**
> list[MigrationRecommendationInstance] migration_recommendation_get()

Collection query

Get migration recommendations.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MigrationRecommendationApi()

try:
    # Collection query
    api_response = api_instance.migration_recommendation_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationRecommendationApi->migration_recommendation_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MigrationRecommendationInstance]**](MigrationRecommendationInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_recommendation_id_create_migration_sessions_post**
> MigrationRecommendationCreateMigrationSessionsResponse migration_recommendation_id_create_migration_sessions_post(id)

Create migrations

Create the migration sessions to implement a migration recommendation. If the response contains a list of hosts to rescan, those hosts must be rescanned before starting the sessions or the host(s) may lose access to the data when the migration completes. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MigrationRecommendationApi()
id = 'id_example' # str | Unique ID of the migration recommendation.

try:
    # Create migrations
    api_response = api_instance.migration_recommendation_id_create_migration_sessions_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationRecommendationApi->migration_recommendation_id_create_migration_sessions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the migration recommendation. | 

### Return type

[**MigrationRecommendationCreateMigrationSessionsResponse**](MigrationRecommendationCreateMigrationSessionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_recommendation_id_delete**
> migration_recommendation_id_delete(id)

Delete

Delete a migration recommendation.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MigrationRecommendationApi()
id = 'id_example' # str | Unique ID of the migration recommendation.

try:
    # Delete
    api_instance.migration_recommendation_id_delete(id)
except ApiException as e:
    print("Exception when calling MigrationRecommendationApi->migration_recommendation_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the migration recommendation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_recommendation_id_get**
> MigrationRecommendationInstance migration_recommendation_id_get(id)

Instance query

Get a single migration recommendation.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MigrationRecommendationApi()
id = 'id_example' # str | Unique ID of the migration recommendation.

try:
    # Instance query
    api_response = api_instance.migration_recommendation_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationRecommendationApi->migration_recommendation_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the migration recommendation. | 

### Return type

[**MigrationRecommendationInstance**](MigrationRecommendationInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_recommendation_id_patch**
> migration_recommendation_id_patch(id, body)

Modify

Modify migration actions by applying specified dst appliance id and active flag to the migration actions specified by resource id. All specified modifications must be successful for the request to be successful. Partially successful modifications will be rejected and the recommendation object will be unchanged. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MigrationRecommendationApi()
id = 'id_example' # str | Unique ID of the migration recommendation.
body = prime.swagger_client.MigrationRecommendationActionModify() # MigrationRecommendationActionModify | 

try:
    # Modify
    api_instance.migration_recommendation_id_patch(id, body)
except ApiException as e:
    print("Exception when calling MigrationRecommendationApi->migration_recommendation_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the migration recommendation. | 
 **body** | [**MigrationRecommendationActionModify**](MigrationRecommendationActionModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_recommendation_id_start_migration_sessions_post**
> migration_recommendation_id_start_migration_sessions_post(id)

Start migrations

Start previously created migration sessions for recommendation. Ensure that any rescans specified in the create_migration_sessions response have been done before using this to start the sessions. Failure to do may result in data unavailability and/or data loss. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MigrationRecommendationApi()
id = 'id_example' # str | Unique ID of the migration recommendation.

try:
    # Start migrations
    api_instance.migration_recommendation_id_start_migration_sessions_post(id)
except ApiException as e:
    print("Exception when calling MigrationRecommendationApi->migration_recommendation_id_start_migration_sessions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the migration recommendation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_recommendation_post**
> CreateResponse migration_recommendation_post(body)

Create

Generate a recommendation for redistributing storage utilization between appliances.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MigrationRecommendationApi()
body = prime.swagger_client.MigrationRecommendationCreate() # MigrationRecommendationCreate | 

try:
    # Create
    api_response = api_instance.migration_recommendation_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationRecommendationApi->migration_recommendation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrationRecommendationCreate**](MigrationRecommendationCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

