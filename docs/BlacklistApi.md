# readarr.BlacklistApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_blacklist**](BlacklistApi.md#delete_blacklist) | **DELETE** /api/v1/blacklist/{id} | 
[**delete_blacklist_bulk**](BlacklistApi.md#delete_blacklist_bulk) | **DELETE** /api/v1/blacklist/bulk | 
[**get_blacklist**](BlacklistApi.md#get_blacklist) | **GET** /api/v1/blacklist | 


# **delete_blacklist**
> delete_blacklist(id)



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
    api_instance = readarr.BlacklistApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_blacklist(id)
    except Exception as e:
        print("Exception when calling BlacklistApi->delete_blacklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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

# **delete_blacklist_bulk**
> delete_blacklist_bulk(blacklist_bulk_resource=blacklist_bulk_resource)



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
    api_instance = readarr.BlacklistApi(api_client)
    blacklist_bulk_resource = readarr.BlacklistBulkResource() # BlacklistBulkResource |  (optional)

    try:
        api_instance.delete_blacklist_bulk(blacklist_bulk_resource=blacklist_bulk_resource)
    except Exception as e:
        print("Exception when calling BlacklistApi->delete_blacklist_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blacklist_bulk_resource** | [**BlacklistBulkResource**](BlacklistBulkResource.md)|  | [optional] 

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

# **get_blacklist**
> BlacklistResourcePagingResource get_blacklist()



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
    api_instance = readarr.BlacklistApi(api_client)

    try:
        api_response = api_instance.get_blacklist()
        print("The response of BlacklistApi->get_blacklist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlacklistApi->get_blacklist: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BlacklistResourcePagingResource**](BlacklistResourcePagingResource.md)

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

