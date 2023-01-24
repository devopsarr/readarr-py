# readarr.ReleaseApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_release**](ReleaseApi.md#create_release) | **POST** /api/v1/release | 
[**get_release_by_id**](ReleaseApi.md#get_release_by_id) | **GET** /api/v1/release/{id} | 
[**list_release**](ReleaseApi.md#list_release) | **GET** /api/v1/release | 


# **create_release**
> ReleaseResource create_release(release_resource=release_resource)



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
    api_instance = readarr.ReleaseApi(api_client)
    release_resource = readarr.ReleaseResource() # ReleaseResource |  (optional)

    try:
        api_response = api_instance.create_release(release_resource=release_resource)
        print("The response of ReleaseApi->create_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleaseApi->create_release: %s\n" % e)
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

# **get_release_by_id**
> ReleaseResource get_release_by_id(id)



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
    api_instance = readarr.ReleaseApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_release_by_id(id)
        print("The response of ReleaseApi->get_release_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleaseApi->get_release_by_id: %s\n" % e)
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

# **list_release**
> List[ReleaseResource] list_release(book_id=book_id, author_id=author_id)



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
    api_instance = readarr.ReleaseApi(api_client)
    book_id = 56 # int |  (optional)
    author_id = 56 # int |  (optional)

    try:
        api_response = api_instance.list_release(book_id=book_id, author_id=author_id)
        print("The response of ReleaseApi->list_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleaseApi->list_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**|  | [optional] 
 **author_id** | **int**|  | [optional] 

### Return type

[**List[ReleaseResource]**](ReleaseResource.md)

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

