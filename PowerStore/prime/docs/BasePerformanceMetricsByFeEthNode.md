# BasePerformanceMetricsByFeEthNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Reference to the associated node on which these metrics were recorded. | [optional] 
**appliance_id** | **str** | Reference to the associated appliance on which these metrics were recorded. | [optional] 
**timestamp** | **datetime** | End of sample period. | [optional] 
**bytes_rx_ps** | **float** | The total bytes received per second. | [optional] 
**bytes_tx_ps** | **float** | The total bytes transmitted per second. | [optional] 
**pkt_rx_ps** | **float** | The number of packets received per second. | [optional] 
**pkt_tx_ps** | **float** | The number of packets transmitted per second. | [optional] 
**pkt_rx_no_buffer_error_ps** | **float** | The number of packets discarded per second due to lack of buffer space. | [optional] 
**pkt_rx_crc_error_ps** | **float** | The number of packets received with CRC error (and thus dropped) per second. | [optional] 
**pkt_tx_error_ps** | **float** | The number of packets that failed to be transmitted per second due to error. | [optional] 
**repeat_count** | **int** | Number of times the metrics are repeated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


