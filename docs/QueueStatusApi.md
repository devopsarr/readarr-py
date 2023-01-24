# readarr.QueueStatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_queue_status**](QueueStatusApi.md#get_queue_status) | **GET** /api/v1/queue/status | 
[**get_queue_status_by_id**](QueueStatusApi.md#get_queue_status_by_id) | **GET** /api/v1/queue/status/{id} | 


# **get_queue_status**
> QueueStatusResource get_queue_status()



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
    api_instance = readarr.QueueStatusApi(api_client)

    try:
        api_response = api_instance.get_queue_status()
        print("The response of QueueStatusApi->get_queue_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueStatusApi->get_queue_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QueueStatusResource**](QueueStatusResource.md)

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

# **get_queue_status_by_id**
> QueueStatusResource get_queue_status_by_id(id)



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
    api_instance = readarr.QueueStatusApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_queue_status_by_id(id)
        print("The response of QueueStatusApi->get_queue_status_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueStatusApi->get_queue_status_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**QueueStatusResource**](QueueStatusResource.md)

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

