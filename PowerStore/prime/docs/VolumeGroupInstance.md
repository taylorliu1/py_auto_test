# VolumeGroupInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the volume group. | [optional] 
**name** | **str** | Name of the volume group.  This property supports case-insensitive filtering. | [optional] 
**description** | **str** | Description for the volume group. | [optional] 
**creation_timestamp** | **datetime** | The time at which the volume group was created. | [optional] 
**is_protectable** | **bool** | This is a derived field that is set internally. It enables/disables the following functionality: * Whether a protection_policy can be applied to the group. * Whether manual snapshots can be taken. * Whether clones of the group can be created.  | [optional] 
**protection_policy_id** | **str** | Unique identifier of the protection policy assigned to the volume group. This attribute is only applicable to primary and clone volume groups. | [optional] 
**migration_session_id** | **str** | Unique identifier of the migration session assigned to the volume group when it is part of a migration activity. | [optional] 
**is_write_order_consistent** | **bool** | For a primary or a clone volume group, this property determines whether snapshot sets of the group will be write order consistent.  For a snapshot set, this property indicates whether the snapshot set is write-order consistent. | [optional] 
**placement_rule** | [**VGPlacementRule**](VGPlacementRule.md) |  | [optional] 
**type** | [**VolumeTypeEnum**](VolumeTypeEnum.md) |  | [optional] 
**is_replication_destination** | **bool** | Indicates whether this volume group is a replication destination. A replication destination will be created by the system when a replication session is created. When there is an active replication session, all the user operations are restricted including modification, deletion, host operation, snapshot, clone, etc. After the replication session is deleted, the replication destination will remain as it is until the end user changes it to be a non-replication destination. After the change, it becomes a primary volume group. If the end user keeps it as a replication destination, when the replication session is recreated, the replication destination could potentially be reused in the new session to avoid a time-consuming full sync. This property is only valid for primary and clone volume groups. | [optional] [default to False]
**protection_data** | [**ProtectionDataInstance**](ProtectionDataInstance.md) |  | [optional] 
**is_importing** | **bool** | Indicates whether the volume group is being imported. | [optional] 
**location_history** | [**list[LocationHistoryInstance]**](LocationHistoryInstance.md) | A list of locations. The list of locations includes the move to the current appliance.  Filtering on the fields of this embedded resource is not supported. | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type | [optional] 
**protection_policy** | [**PolicyInstance**](PolicyInstance.md) | This is the embeddable reference form of protection_policy_id attribute. | [optional] 
**migration_session** | [**MigrationSessionInstance**](MigrationSessionInstance.md) | This is the embeddable reference form of migration_session_id attribute. | [optional] 
**volumes** | [**list[VolumeInstance]**](VolumeInstance.md) | List of the volumes that are associated with this volume_group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


