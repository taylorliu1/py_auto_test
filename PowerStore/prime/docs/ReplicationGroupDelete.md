# ReplicationGroupDelete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_session** | **bool** | Normally, only replication groups without a session can be deleted. This option overrides that behavior and deletes replication session before deleting the replication group. Note that this option only deletes the session on local appliance. Peer session and replication group won&#39;t be affected and may require separate delete operation. | [optional] [default to False]
**delete_members** | **bool** | Normally, only empty replication groups can be deleted. This option overrides that behavior and deletes member vVols before deleting the replication group. Deletes bound and attached vVols, which is equivalent to virtual_volume delete with force set to true. May not be used together with unassign_members. | [optional] [default to False]
**unassign_members** | **bool** | Normally, only empty replication groups can be deleted. This option overrides that behavior and unassigns replication group from member vVols before deleting the replication group. May not be used together with delete_members. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


