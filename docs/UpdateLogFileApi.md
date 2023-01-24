# readarr.UpdateLogFileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log_file_update_by_filename**](UpdateLogFileApi.md#get_log_file_update_by_filename) | **GET** /api/v1/log/file/update/{filename} | 
[**list_log_file_update**](UpdateLogFileApi.md#list_log_file_update) | **GET** /api/v1/log/file/update | 


# **get_log_file_update_by_filename**
> get_log_file_update_by_filename(filename)



### Example

```python
from __future__ import print_function
import time
import os
import readarr
from readarr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = readarr.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with readarr.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = readarr.UpdateLogFileApi(api_client)
    filename = 'filename_example' # str | 

    try:
        api_instance.get_log_file_update_by_filename(filename)
    except Exception as e:
        print("Exception when calling UpdateLogFileApi->get_log_file_update_by_filename: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_log_file_update**
> List[LogFileResource] list_log_file_update()



### Example

```python
from __future__ import print_function
import time
import os
import readarr
from readarr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = readarr.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with readarr.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = readarr.UpdateLogFileApi(api_client)

    try:
        api_response = api_instance.list_log_file_update()
        print("The response of UpdateLogFileApi->list_log_file_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateLogFileApi->list_log_file_update: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[LogFileResource]**](LogFileResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

