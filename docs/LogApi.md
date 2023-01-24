# readarr.LogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log**](LogApi.md#get_log) | **GET** /api/v1/log | 


# **get_log**
> LogResourcePagingResource get_log()



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
    api_instance = readarr.LogApi(api_client)

    try:
        api_response = api_instance.get_log()
        print("The response of LogApi->get_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogApi->get_log: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogResourcePagingResource**](LogResourcePagingResource.md)

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

