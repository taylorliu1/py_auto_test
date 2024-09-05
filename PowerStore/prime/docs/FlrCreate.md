# FlrCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**FileSystemFLRModeEnum**](FileSystemFLRModeEnum.md) |  | [optional] 
**minimum_retention** | **str** | The shortest retention period for which files on an FLR-enabled file system can be locked and protected from deletion. This value must be less than or equal to the maximum retention period. Any attempt to lock a file for less than the minimum retention period results in the file being locked until the current system time plus the minimum retention period is reached. Format [default_int][Y|M|D] (example 5Y for 5 years). Specify Y for years, M for months, D for days, or the keyword infinite. Setting infinite means that the files can never be deleted. This attribute should be set only for FLR enabled filesystems.  | [optional] [default to '1D']
**default_retention** | **str** | The default retention period that is used in an FLR-enabled file system when a file is locked and a retention period is not specified. This value must be greater than or equal to the minimum retention period, and less than or equal to the maximum retention period. Format [default_int][Y|M|D] (example 5Y for 5 years). Specify Y for years, M for months, D for days, or infinite. The default value for the default retention period is infinite for Enterprise FLR mode, and 1 year for Compliance FLR mode. This attribute should be set only for FLR enabled filesystems.  | [optional] 
**maximum_retention** | **str** | The longest retention period for which files on an FLR-enabled file system can be locked and protected from deletion. Any attempt to lock a file for more than this maximum retention period results in the file being locked until the current system time plus the maximum retention period is reached. Format [default_int][Y|M|D] (example 5Y for 5 years). Specify Y for years, M for months, D for days, or infinite. Setting infinite means that the files can never be deleted. This attribute should be set only for FLR enabled filesystems.  | [optional] [default to 'infinite']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


