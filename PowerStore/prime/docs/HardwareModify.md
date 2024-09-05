# HardwareModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_marked** | **bool** | New state for the hardware component location marker LED. Setting it to true will put the LED in a blinking state until set to false. Note that the state returned in the hardware component may not actually change for up to 60 seconds. This operation is currently supported for Base_Enclosure, Expansion_Enclosure, Node, Drive, and Access_Module. Note that operations at the Base_Enclosure and Expansion_Enclosure apply to their children (Nodes and Drives for Base_Enclosure, and Access_Modules and Drives for Expansion_Enclosure). For components with a single physical LED (Base_Enclosure, NVME Expansion_Enclosure, Node, Drive, and Access_Module), setting is_marked&#x3D;true overrides the status_led_state property from on (or off) to Null, and setting is_marked&#x3D;false reverts status_led_state to showing the state of the physical LED. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


