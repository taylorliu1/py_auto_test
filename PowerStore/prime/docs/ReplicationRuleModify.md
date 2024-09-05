# ReplicationRuleModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the replication rule. | [optional] 
**rpo** | [**RPOEnum**](RPOEnum.md) |  | [optional] 
**remote_system_id** | **str** | Unique identifier of the remote system to which this replication rule will replicate the associated storage resources.  name:{name} can be used instead of {id}. For example:&#39;remote_system_id&#39;:&#39;name:remote_system_name&#39; | [optional] 
**alert_threshold** | **int** | Number of minutes the system will wait before generating a compliance alert when a replication session does not meet the RPO.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


