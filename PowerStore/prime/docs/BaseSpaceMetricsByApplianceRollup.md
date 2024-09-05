# BaseSpaceMetricsByApplianceRollup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliance_id** | **str** | Reference to the associated appliance on which these metrics were recorded. | [optional] 
**timestamp** | **datetime** | End of sample period. | [optional] 
**last_logical_provisioned** | **int** | Last logical total space during the period. | [optional] 
**last_logical_used** | **int** | Last logical used space during the period. | [optional] 
**last_logical_used_volume** | **int** | Last logical used space for block volumes during the period. Was added in version 2.0.0.0. | [optional] 
**last_logical_used_file_system** | **int** | Last logical used space for file systems during the period. Was added in version 2.0.0.0. | [optional] 
**last_logical_used_vvol** | **int** | Last logical used space for virtual volumes during the period. Was added in version 2.0.0.0. | [optional] 
**last_shared_logical_used_volume** | **int** | Last shared logical used space for block volumes during the period. Was added in version 2.0.0.0. | [optional] 
**last_shared_logical_used_file_system** | **int** | Last shared logical used space for file systems during the period. Was added in version 2.0.0.0. | [optional] 
**last_shared_logical_used_vvol** | **int** | Last shared logical used space for virtual volumes during the period. Was added in version 2.0.0.0. | [optional] 
**last_physical_total** | **int** | Last physical total space during the period. | [optional] 
**last_physical_used** | **int** | Last physical used space during the period. | [optional] 
**last_data_physical_used** | **int** | Last physical used space for data during the period. | [optional] 
**max_logical_provisioned** | **int** | Maxiumum logical total space during the period. | [optional] 
**max_logical_used** | **int** | Maxiumum logical used space during the period. | [optional] 
**max_logical_used_volume** | **int** | Maximum logical used space for block volumes during the period. Was added in version 2.0.0.0. | [optional] 
**max_logical_used_file_system** | **int** | Maximum logical used space for file systems during the period. Was added in version 2.0.0.0. | [optional] 
**max_logical_used_vvol** | **int** | Maximum logical used space for virtual volumes during the period. Was added in version 2.0.0.0. | [optional] 
**max_shared_logical_used_volume** | **int** | Maximum shared logical used space for block volumes during the period. Was added in version 2.0.0.0. | [optional] 
**max_shared_logical_used_file_system** | **int** | Maximum shared logical used space for file volumes during the period. Was added in version 2.0.0.0. | [optional] 
**max_shared_logical_used_vvol** | **int** | Maximum shared logical used space for virtual volumes during the period. Was added in version 2.0.0.0. | [optional] 
**max_physical_total** | **int** | Maximum physical total space during the period. | [optional] 
**max_physical_used** | **int** | Maximum physical used space during the period. | [optional] 
**max_data_physical_used** | **int** | Maximum physical used space for data during the period. | [optional] 
**last_efficiency_ratio** | **float** | Last efficiency ratio during the period. | [optional] 
**last_data_reduction** | **float** | Last data reduction space during the period. | [optional] 
**last_snapshot_savings** | **float** | Last snapshot savings space during the period. | [optional] 
**last_thin_savings** | **float** | Last thin savings ratio during the period. | [optional] 
**last_shared_logical_used** | **int** | Last shared logical used during the period. | [optional] 
**last_system_free_space** | **int** | Last system free space during the period. Was added in version 3.0.0.0. | [optional] 
**max_efficiency_ratio** | **float** | Maximum efficiency ratio during the period. | [optional] 
**max_data_reduction** | **float** | Maximum data reduction space during the period. | [optional] 
**max_snapshot_savings** | **float** | Maximum snapshot savings space during the period. | [optional] 
**max_thin_savings** | **float** | Maximum thin savings ratio during the period. | [optional] 
**max_shared_logical_used** | **int** | Max shared logical used during the period. | [optional] 
**max_system_free_space** | **int** | Maximum system free space during the period. Was added in version 3.0.0.0. | [optional] 
**repeat_count** | **int** | Number of times the metrics are repeated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


