# readarr.BookshelfApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bookshelf**](BookshelfApi.md#create_bookshelf) | **POST** /api/v1/bookshelf | 


# **create_bookshelf**
> create_bookshelf(bookshelf_resource=bookshelf_resource)



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
    api_instance = readarr.BookshelfApi(api_client)
    bookshelf_resource = readarr.BookshelfResource() # BookshelfResource |  (optional)

    try:
        api_instance.create_bookshelf(bookshelf_resource=bookshelf_resource)
    except Exception as e:
        print("Exception when calling BookshelfApi->create_bookshelf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bookshelf_resource** | [**BookshelfResource**](BookshelfResource.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

