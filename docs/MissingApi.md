# readarr.MissingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_wanted_missing**](MissingApi.md#get_wanted_missing) | **GET** /api/v1/wanted/missing | 
[**get_wanted_missing_by_id**](MissingApi.md#get_wanted_missing_by_id) | **GET** /api/v1/wanted/missing/{id} | 


# **get_wanted_missing**
> BookResourcePagingResource get_wanted_missing(include_author=include_author)



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
    api_instance = readarr.MissingApi(api_client)
    include_author = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.get_wanted_missing(include_author=include_author)
        print("The response of MissingApi->get_wanted_missing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MissingApi->get_wanted_missing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_author** | **bool**|  | [optional] [default to False]

### Return type

[**BookResourcePagingResource**](BookResourcePagingResource.md)

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

# **get_wanted_missing_by_id**
> BookResource get_wanted_missing_by_id(id)



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
    api_instance = readarr.MissingApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_wanted_missing_by_id(id)
        print("The response of MissingApi->get_wanted_missing_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MissingApi->get_wanted_missing_by_id: %s\n" % e)
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

