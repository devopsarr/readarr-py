# readarr.ReleasePushApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_release_push**](ReleasePushApi.md#create_release_push) | **POST** /api/v1/release/push | 
[**get_release_push_by_id**](ReleasePushApi.md#get_release_push_by_id) | **GET** /api/v1/release/push/{id} | 


# **create_release_push**
> ReleaseResource create_release_push(release_resource=release_resource)



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
    api_instance = readarr.ReleasePushApi(api_client)
    release_resource = readarr.ReleaseResource() # ReleaseResource |  (optional)

    try:
        api_response = api_instance.create_release_push(release_resource=release_resource)
        print("The response of ReleasePushApi->create_release_push:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePushApi->create_release_push: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_resource** | [**ReleaseResource**](ReleaseResource.md)|  | [optional] 

### Return type

[**ReleaseResource**](ReleaseResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_push_by_id**
> ReleaseResource get_release_push_by_id(id)



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
    api_instance = readarr.ReleasePushApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_release_push_by_id(id)
        print("The response of ReleasePushApi->get_release_push_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePushApi->get_release_push_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReleaseResource**](ReleaseResource.md)

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

