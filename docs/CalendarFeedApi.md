# readarr.CalendarFeedApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_calendar_readarr_ics**](CalendarFeedApi.md#get_calendar_readarr_ics) | **GET** /api/v1/calendar/readarr.ics | 


# **get_calendar_readarr_ics**
> get_calendar_readarr_ics(past_days=past_days, future_days=future_days, tag_list=tag_list, unmonitored=unmonitored)



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
    api_instance = readarr.CalendarFeedApi(api_client)
    past_days = 7 # int |  (optional) (default to 7)
    future_days = 28 # int |  (optional) (default to 28)
    tag_list = '' # str |  (optional) (default to '')
    unmonitored = False # bool |  (optional) (default to False)

    try:
        api_instance.get_calendar_readarr_ics(past_days=past_days, future_days=future_days, tag_list=tag_list, unmonitored=unmonitored)
    except Exception as e:
        print("Exception when calling CalendarFeedApi->get_calendar_readarr_ics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **past_days** | **int**|  | [optional] [default to 7]
 **future_days** | **int**|  | [optional] [default to 28]
 **tag_list** | **str**|  | [optional] [default to &#39;&#39;]
 **unmonitored** | **bool**|  | [optional] [default to False]

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

