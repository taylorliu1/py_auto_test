# MigrationSessionCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User-specified friendly name of the migration session instance. The name can contain a maximum of 32 Unicode characters. It cannot contain unprintable characters, special HTTP characters, or whitespace. | [optional] 
**resource_type** | [**MigrationResourceTypeEnum**](MigrationResourceTypeEnum.md) |  | 
**family_id** | **str** | Family identifier designating the storage resource or resources to migrate. For volume or virtual_volume migrations, the family is moved together because they share data among the primary object, snapshots, and clones. For volume_group migration, the family of each volume in the group is moved because it is a grouping of volumes. | 
**destination_appliance_id** | **str** | Unique identifier of the destination appliance instance. name:{name} can be used instead of {id}. For example:&#39;appliance_id&#39;:&#39;name:appliance_name&#39; | 
**automatic_cutover** | **bool** | Indicates whether the migration session cutover is manual or automatic. Default for virtual_volume resource type migrations is automatic, otherwise the default is manual. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


