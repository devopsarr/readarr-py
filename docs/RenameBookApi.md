# readarr.RenameBookApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_rename**](RenameBookApi.md#list_rename) | **GET** /api/v1/rename | 


# **list_rename**
> List[RenameBookResource] list_rename(author_id=author_id, book_id=book_id)



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
    api_instance = readarr.RenameBookApi(api_client)
    author_id = 56 # int |  (optional)
    book_id = 56 # int |  (optional)

    try:
        api_response = api_instance.list_rename(author_id=author_id, book_id=book_id)
        print("The response of RenameBookApi->list_rename:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RenameBookApi->list_rename: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_id** | **int**|  | [optional] 
 **book_id** | **int**|  | [optional] 

### Return type

[**List[RenameBookResource]**](RenameBookResource.md)

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

