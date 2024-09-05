# VolumeGroupCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name for the volume group. The name should contain no special HTTP characters and no unprintable characters. Although the case of the name provided is reserved, uniqueness check is case-insensitive, so the same name in two different cases is not considered unique. | 
**description** | **str** | Description for the volume group. The description should not be more than 256 characters long and should not have any unprintable characters.  If description is not specified, the description for the volume group will not be set. | [optional] 
**volume_ids** | **list[str]** | A list of identifiers of existing volumes that should be added to the volume group.   All the volumes must be on the same Cyclone appliance and should not be part of another volume group.  If a list of volumes is not specified or if the specified list is empty, an empty volume group of type Volume will be created. | [optional] 
**is_write_order_consistent** | **bool** | A boolean flag to indicate whether snapshot sets of the volume group will be write-order consistent.  This parameter defaults to true, if not specified. | [optional] [default to True]
**protection_policy_id** | **str** | Unique identifier of an optional protection policy to assign to the volume group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


