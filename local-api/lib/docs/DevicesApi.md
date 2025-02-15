# formlabs_local_api.DevicesApi

All URIs are relative to *http://localhost:44388*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discover_devices**](DevicesApi.md#discover_devices) | **POST** /discover-devices/ | Discover Devices
[**get_device**](DevicesApi.md#get_device) | **GET** /devices/{id}/ | Get Device
[**get_devices**](DevicesApi.md#get_devices) | **GET** /devices/ | Get Devices
[**upload_firmware**](DevicesApi.md#upload_firmware) | **POST** /upload-firmware/ | Upload Firmware


# **discover_devices**
> DiscoverDevices200Response discover_devices(discover_devices_request, var_async=var_async)

Discover Devices

Discover new devices on the network

### Example


```python
import formlabs_local_api
from formlabs_local_api.models.discover_devices200_response import DiscoverDevices200Response
from formlabs_local_api.models.discover_devices_request import DiscoverDevicesRequest
from formlabs_local_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs_local_api.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs_local_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_local_api.DevicesApi(api_client)
    discover_devices_request = {"timeout_seconds":10} # DiscoverDevicesRequest | 
    var_async = True # bool | Whether to run the operation asynchronously (optional)

    try:
        # Discover Devices
        api_response = api_instance.discover_devices(discover_devices_request, var_async=var_async)
        print("The response of DevicesApi->discover_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->discover_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discover_devices_request** | [**DiscoverDevicesRequest**](DiscoverDevicesRequest.md)|  | 
 **var_async** | **bool**| Whether to run the operation asynchronously | [optional] 

### Return type

[**DiscoverDevices200Response**](DiscoverDevices200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**202** | Async operation accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device**
> DeviceStatusModel get_device(id)

Get Device

Get a previously discovered device's status

### Example


```python
import formlabs_local_api
from formlabs_local_api.models.device_status_model import DeviceStatusModel
from formlabs_local_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs_local_api.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs_local_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_local_api.DevicesApi(api_client)
    id = 'id_example' # str | The unique identifier of the printer

    try:
        # Get Device
        api_response = api_instance.get_device(id)
        print("The response of DevicesApi->get_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the printer | 

### Return type

[**DeviceStatusModel**](DeviceStatusModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices**
> GetDevices200Response get_devices(can_print=can_print)

Get Devices

List of previously discovered device statuses  By default, only locally discovered printer names are returned. To include your Fleet Control queues or printers registered to your Dashboard account, you must be logged in and have an Internet connection. Use the Login endpoint to authenticate with Formlabs Web Services. 

### Example


```python
import formlabs_local_api
from formlabs_local_api.models.get_devices200_response import GetDevices200Response
from formlabs_local_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs_local_api.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs_local_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_local_api.DevicesApi(api_client)
    can_print = True # bool | If true, only devices that can receive prints will be returned. (optional)

    try:
        # Get Devices
        api_response = api_instance.get_devices(can_print=can_print)
        print("The response of DevicesApi->get_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **can_print** | **bool**| If true, only devices that can receive prints will be returned. | [optional] 

### Return type

[**GetDevices200Response**](GetDevices200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_firmware**
> DiscoverDevices200Response upload_firmware(upload_firmware_request, var_async=var_async)

Upload Firmware

Upload new firmware to a device

### Example


```python
import formlabs_local_api
from formlabs_local_api.models.discover_devices200_response import DiscoverDevices200Response
from formlabs_local_api.models.upload_firmware_request import UploadFirmwareRequest
from formlabs_local_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs_local_api.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs_local_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_local_api.DevicesApi(api_client)
    upload_firmware_request = {"printer":"Form4-TestyTest","file_path":"C:\\Users\\user\\Desktop\\form4-public-1.9.0-2444.formware"} # UploadFirmwareRequest | 
    var_async = True # bool | Whether to run the operation asynchronously (optional)

    try:
        # Upload Firmware
        api_response = api_instance.upload_firmware(upload_firmware_request, var_async=var_async)
        print("The response of DevicesApi->upload_firmware:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->upload_firmware: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_firmware_request** | [**UploadFirmwareRequest**](UploadFirmwareRequest.md)|  | 
 **var_async** | **bool**| Whether to run the operation asynchronously | [optional] 

### Return type

[**DiscoverDevices200Response**](DiscoverDevices200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**202** | Async operation accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

