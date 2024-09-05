# MigrationSessionSync

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rescan_complete** | **bool** | Indicates whether a rescan will be performed during the sync operation. Default value is false. If the session creation completed with a message that rescan is required from one or more hosts, you must set this value to true during the subsequent sync operation. Otherwise, the sync operation will fail. | [optional] [default to False]
**automatic_cutover** | **bool** | Indicates whether the migration session cutover is manual or automatic. Default is manual. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


