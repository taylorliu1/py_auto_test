# ReplicationSessionFailover

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_planned** | **bool** | Indicates whether the replication session failover is planned or unplanned. For planned failovers, the value is true. For unplanned failovers, the value is false.  | [optional] [default to True]
**reverse** | **bool** | Indicates whether the system is auto-reprotected. Auto-reprotect is combination of failover and reprotect.  This is only allowed when issuing a planned failover.  | [optional] [default to False]
**use_test_copy** | **bool** | When a failover test is in progress and an unplanned failover needs to be started, this flag must be set to true. Setting this flag to true will keep the destination resources&#39; data as is before starting the unplanned failover. Please stop the failover test first if you do not wish to keep the test data before starting an unplanned failover.  Was added in version 2.0.0.0. | [optional] [default to False]
**failover_snapshot_id** | **str** | Optional identifier of a snapshot that the destination resource must be restored to as part of an unplanned failover. If a failover_snapshot_id is not specified, the destination will be restored to the last common base snapshot. This identifier is not supported when a failover test is in progress.  Was added in version 2.0.0.0. | [optional] 
**force** | **bool** | Indicates whether an unplanned failover needs to be performed for a session that is already in a failed over state.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


