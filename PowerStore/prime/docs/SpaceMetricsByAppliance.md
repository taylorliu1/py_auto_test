# SpaceMetricsByAppliance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliance_id** | **str** | Reference to the associated appliance on which these metrics were recorded. | [optional] 
**timestamp** | **datetime** | End of sample period. | [optional] 
**logical_provisioned** | **int** | Total configured size of all storage objects on an appliance. This metric includes all primaries, snaps and clones. | [optional] 
**logical_used** | **int** | Amount of data in bytes written to all storage objects on an appliance, without any deduplication and/or compression. This metric includes all primaries, snaps and clones. | [optional] 
**logical_used_volume** | **int** | Amount of data in bytes written to all block volumes on an appliance, without any deduplication and/or compression. This metric includes all primaries, snaps and clones. Was added in version 2.0.0.0. | [optional] 
**logical_used_file_system** | **int** | Amount of data in bytes written to all file systems on an appliance, without any deduplication and/or compression. This metric includes all primaries, snaps and clones. Was added in version 2.0.0.0. | [optional] 
**logical_used_vvol** | **int** | Amount of data in bytes written to all virtual volumes on an appliance, without any deduplication and/or compression. This metric includes all primaries, snaps and clones. Was added in version 2.0.0.0. | [optional] 
**shared_logical_used_volume** | **int** | Amount of data in bytes written to all block volumes on an appliance, without any deduplication and/or compression. This metric includes all primaries and clones. Was added in version 2.0.0.0. | [optional] 
**shared_logical_used_file_system** | **int** | Amount of data in bytes written to all file systems on an appliance, without any deduplication and/or compression. This metric includes all primaries and clones. Was added in version 2.0.0.0. | [optional] 
**shared_logical_used_vvol** | **int** | Amount of data in bytes written to all virtual volumes on an appliance, without any deduplication and/or compression. This metric includes all primaries and clones. Was added in version 2.0.0.0. | [optional] 
**physical_total** | **int** | Total combined space on the physical drives of the appliance available for data. | [optional] 
**physical_used** | **int** | Total physical space consumed in the appliance, accounting for all efficiency mechanisms, as well as all data protection. | [optional] 
**data_physical_used** | **int** | This metric represents amount of physical space user data occupies after deduplication and compression. | [optional] 
**efficiency_ratio** | **float** | The overall efficiency is computed as a ratio of the total space provisioned to physical used space. For example, ten 2 GB volumes were provisioned and 1 GB of data is written to each of them. Each of the volumes has one snapshot as well, for another ten 2 GB volumes. All volumes are thinly provisioned with deduplication and compression applied, there is 4 GB of physical space used. Overall efficiency would be (20 * 2 GB) / 4 GB or 10:1. The efficiency_ratio value will be 10 in this example. | [optional] 
**data_reduction** | **float** | Ratio of the logical used space to data physical used space which is after deduplication and compression. | [optional] 
**snapshot_savings** | **float** | Ratio of the amount of space that would have been used by snapshots if space efficiency was not applied to logical space used solely by snapshots. For example, an object is provisioned as 1 GB and it has two snapshots. Each snapshot has 200 MB of data. Snapshot savings will be (1 GB + 1 GB) / (0.2 GB + 0.2 GB) or 5:1. The snapshot_savings value will be 5 in this case. | [optional] 
**thin_savings** | **float** | Ratio of all the vVol provisioned to data they contain. This is the ratio of logical_provisioned to logical_used. For example, a cluster has two 2 GB objects and have written 500 MB bytes of data to them. The thin savings would be (2 * 2 GB) / (2 * 0.5 GB) or 4:1, so the thin_savings value would be 4.0. | [optional] 
**shared_logical_used** | **int** | Amount of space the volume family needs to hold the data written by host and shared by snaps and fast-clones in the family. This does not include deduplication or compression. | [optional] 
**system_free_space** | **int** | Space formerly used by the system for internal needs that will be reused for the same purpose as additional storage is provisioned. Was added in version 3.0.0.0. | [optional] 
**repeat_count** | **int** | Number of times the metrics are repeated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


