# ReplicationSessionInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the replication session instance.  | [optional] 
**state** | [**ReplicationStateEnum**](ReplicationStateEnum.md) | Current state of the replication session.  | [optional] 
**role** | [**ReplicationRoleEnum**](ReplicationRoleEnum.md) | Role of the replication session.  | [optional] 
**resource_type** | [**ReplicatedResourceTypeEnum**](ReplicatedResourceTypeEnum.md) | Type of the storage resource.  | [optional] 
**data_transfer_state** | [**DataTransferStateEnum**](DataTransferStateEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**type** | [**ReplicationSessionTypeEnum**](ReplicationSessionTypeEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**last_sync_timestamp** | **datetime** | Time of last successful synchronization. For metro type replication sessions, this property is updated only during asynchronous copy phases. This is not supported for Nas Server replication sessions.  | [optional] 
**local_resource_id** | **str** | Unique identifier of the local storage resource for the replication session.  | [optional] 
**remote_resource_id** | **str** | Unique identifier of the remote storage resource for the replication session.  | [optional] 
**remote_system_id** | **str** | Unique identifier of the remote system instance.  | [optional] 
**progress_percentage** | **int** | Progress of the current replication operation. This value is only available from the source system for the replication session, and is not supported for Nas Server replication sessions.  | [optional] 
**estimated_completion_timestamp** | **datetime** | Estimated completion time of the current replication operation. This is not supported for Nas Server replication sessions.  | [optional] 
**replication_rule_id** | **str** | Associated replication rule instance if created by policy engine.  | [optional] 
**last_sync_duration** | **int** | Elapsed time of the last synchronization operation in milliseconds.  This is not supported for Nas Server replication sessions. For metro type replication sessions, this property is updated only during asynchronous copy phases.  Was added in version 2.0.0.0. | [optional] 
**next_sync_timestamp** | **datetime** | Estimated start time of the next automatic synchronization operation. This is applicable to asynchronous type replication sessions. This is not supported for Nas Server replication sessions.  Was added in version 2.0.0.0. | [optional] 
**storage_element_pairs** | [**list[ReplicationElementPair]**](ReplicationElementPair.md) | List of storage element pairs for a replication session. For a volume or volume group replication session, the replicating storage elements are of type &#39;volume’. For a virtual volume replication session, the replicating storage elements are of type &#39;virtual volume’. For a volume group replication session, there will be as many pairs of storage elements as the number of volumes in the volume group. For volume/virtual volume replication session, there will be only one storage element pair.   Filtering on the fields of this embedded resource is not supported. | [optional] 
**failover_test_in_progress** | **bool** | Indicates whether a test failover is in progress on the destination system of this replication session. This is not supported for Nas Server replication sessions.  Was added in version 2.0.0.0. | [optional] [default to False]
**error_code** | **str** | Error code for the asynchronous copy phase failure.  Was added in version 3.0.0.0. | [optional] 
**data_connection_state** | [**DataConnectionStateEnum**](DataConnectionStateEnum.md) | State of the data connection.  Was added in version 3.0.0.0. | [optional] 
**parent_replication_session_id** | **str** | Parent Replication session identifier. This is only applicable for replication sessions of type file system.  Was added in version 3.0.0.0. | [optional] 
**local_resource_state** | [**ReplicationResourceStateEnum**](ReplicationResourceStateEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**state_l10n** | **str** | Localized message string corresponding to state | [optional] 
**role_l10n** | **str** | Localized message string corresponding to role | [optional] 
**resource_type_l10n** | **str** | Localized message string corresponding to resource_type | [optional] 
**data_transfer_state_l10n** | **str** | Localized message string corresponding to data_transfer_state Was added in version 3.0.0.0. | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type Was added in version 3.0.0.0. | [optional] 
**data_connection_state_l10n** | **str** | Localized message string corresponding to data_connection_state Was added in version 3.0.0.0. | [optional] 
**local_resource_state_l10n** | **str** | Localized message string corresponding to local_resource_state Was added in version 3.0.0.0. | [optional] 
**remote_system** | [**RemoteSystemInstance**](RemoteSystemInstance.md) | This is the embeddable reference form of remote_system_id attribute. | [optional] 
**migration_session** | [**MigrationSessionInstance**](MigrationSessionInstance.md) | This is the embeddable reference form of migration_session_id attribute. | [optional] 
**replication_rule** | [**ReplicationRuleInstance**](ReplicationRuleInstance.md) | This is the embeddable reference form of replication_rule_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


