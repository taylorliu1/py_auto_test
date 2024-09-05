# ReplicationStopFailoverTest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_end_of_test_snapshot** | **bool** | Indicates whether a snapshot of the destination resource should be created at the end of the test.  If set to true, the name of the created snapshot will contain a timestamp indicating its time of creation and will be of the format \&quot;failover_test_STOPPED_&amp;lt;timestamp&amp;gt;\&quot;. The snapshot will be set to automatically expire after a system determined interval.  | [optional] [default to False]
**force** | **bool** | By default a failover test cannot be stopped if the remote system is not reachable. This option allows for stopping the test even if the remote system is down. The intention is to enable disaster recovery to a point in time different than the one under test. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


