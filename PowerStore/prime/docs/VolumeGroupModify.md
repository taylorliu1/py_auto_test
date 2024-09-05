# VolumeGroupModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New name for the volume group. The name should contain no special HTTP characters and no unprintable characters. Although the case of the name provided is reserved, uniqueness check is case-insensitive, so the same name in two different cases is not considered unique. | [optional] 
**description** | **str** | New description for the volume group. The description should not have any unprintable characters. If an empty string is specified, the description will be cleared. | [optional] 
**is_write_order_consistent** | **bool** | A boolean flag to indicate whether snapshot sets of the volume group will be write-order consistent.  This parameter is only valid when modifying a primary or a clone volume group. | [optional] 
**protection_policy_id** | **str** | Unique identifier of the protection policy to assign to a primary or clone volume group.  If an empty string or null is specified, protection policy will be removed from the volume group. | [optional] 
**expiration_timestamp** | **str** | Time after which the snapshot set can be auto-purged. This parameter is only valid for a snapshot set. Time must be specified in Zulu time zone. Expiration time cannot be prior to current time.  Use a maximum timestamp value to set an expiration to never expire. If an empty string or null is specified, expiration_timestamp will be cleared for the snapshot set. Valid format is yyyy-MM-dd&#39;T&#39;HH:mm:ssZ or yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ. Was added in version 2.0.0.0. | [optional] 
**is_replication_destination** | **bool** | New value for is_replication_destination property. is_replication_destination property of all the volumes in the volume group will be modified to the specified value.   Modification of is_replication will not be transactional in nature. If the command only succeeds in modifying the is_replication_destination property of a subset of volumes, is_replication_destination property for the volume group will be set to true.  Modification of this property is idempotent.  This parameter is only valid when modifying a primary or a clone volume group, only when the volume group is no longer the destination of a replication session, and may only be set to false. | [optional] 
**force** | **bool** | Normally a replication destination volume group cannot be modified since it is controlled by replication. However, there can be cases where replication has failed or is no longer active and the replication destination volume group needs to be cleaned up. With the force option, the user will be allowed to remove the protection policy from the replication destination volume group provided that the replication session has never been synchronized. This parameter defaults to false, if not specified. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


