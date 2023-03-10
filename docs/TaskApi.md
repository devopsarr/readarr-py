# readarr.TaskApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_task_by_id**](TaskApi.md#get_system_task_by_id) | **GET** /api/v1/system/task/{id} | 
[**list_system_task**](TaskApi.md#list_system_task) | **GET** /api/v1/system/task | 


# **get_system_task_by_id**
> TaskResource get_system_task_by_id(id)



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
    api_instance = readarr.TaskApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_system_task_by_id(id)
        print("The response of TaskApi->get_system_task_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->get_system_task_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TaskResource**](TaskResource.md)

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

# **list_system_task**
> List[TaskResource] list_system_task()



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
    api_instance = readarr.TaskApi(api_client)

    try:
        api_response = api_instance.list_system_task()
        print("The response of TaskApi->list_system_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->list_system_task: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[TaskResource]**](TaskResource.md)

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

