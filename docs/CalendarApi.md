# readarr.CalendarApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_calendar_by_id**](CalendarApi.md#get_calendar_by_id) | **GET** /api/v1/calendar/{id} | 
[**list_calendar**](CalendarApi.md#list_calendar) | **GET** /api/v1/calendar | 


# **get_calendar_by_id**
> BookResource get_calendar_by_id(id)



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
    api_instance = readarr.CalendarApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_calendar_by_id(id)
        print("The response of CalendarApi->get_calendar_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->get_calendar_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BookResource**](BookResource.md)

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

# **list_calendar**
> List[BookResource] list_calendar(start=start, end=end, unmonitored=unmonitored, include_author=include_author)



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
    api_instance = readarr.CalendarApi(api_client)
    start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    unmonitored = False # bool |  (optional) (default to False)
    include_author = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.list_calendar(start=start, end=end, unmonitored=unmonitored, include_author=include_author)
        print("The response of CalendarApi->list_calendar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->list_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **unmonitored** | **bool**|  | [optional] [default to False]
 **include_author** | **bool**|  | [optional] [default to False]

### Return type

[**List[BookResource]**](BookResource.md)

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

