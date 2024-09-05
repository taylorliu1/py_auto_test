# ReplicationRuleCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the replication rule. | 
**rpo** | [**RPOEnum**](RPOEnum.md) |  | 
**remote_system_id** | **str** | Unique identifier of the remote system to which this replication rule will replicate the associated storage resources.  name:{name} can be used instead of {id}. For example:&#39;remote_system_id&#39;:&#39;name:remote_system_name&#39; | 
**alert_threshold** | **int** | Number of minutes the system will wait before generating a compliance alert when a replication session does not meet the RPO. By default, this will be set to the number of minutes in the configured RPO.  | [optional] 
**is_read_only** | **bool** | Indicates whether this replication rule can be modified.  Was added in version 3.0.0.0. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


