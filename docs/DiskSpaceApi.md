# readarr.DiskSpaceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_disk_space**](DiskSpaceApi.md#list_disk_space) | **GET** /api/v1/diskspace | 


# **list_disk_space**
> List[DiskSpaceResource] list_disk_space()



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
    api_instance = readarr.DiskSpaceApi(api_client)

    try:
        api_response = api_instance.list_disk_space()
        print("The response of DiskSpaceApi->list_disk_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiskSpaceApi->list_disk_space: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[DiskSpaceResource]**](DiskSpaceResource.md)

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

