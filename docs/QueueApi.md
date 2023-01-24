# readarr.QueueApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_queue**](QueueApi.md#delete_queue) | **DELETE** /api/v1/queue/{id} | 
[**delete_queue_bulk**](QueueApi.md#delete_queue_bulk) | **DELETE** /api/v1/queue/bulk | 
[**get_queue**](QueueApi.md#get_queue) | **GET** /api/v1/queue | 
[**get_queue_by_id**](QueueApi.md#get_queue_by_id) | **GET** /api/v1/queue/{id} | 


# **delete_queue**
> delete_queue(id, remove_from_client=remove_from_client, blacklist=blacklist, skip_re_download=skip_re_download)



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
    api_instance = readarr.QueueApi(api_client)
    id = 56 # int | 
    remove_from_client = True # bool |  (optional) (default to True)
    blacklist = False # bool |  (optional) (default to False)
    skip_re_download = False # bool |  (optional) (default to False)

    try:
        api_instance.delete_queue(id, remove_from_client=remove_from_client, blacklist=blacklist, skip_re_download=skip_re_download)
    except Exception as e:
        print("Exception when calling QueueApi->delete_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **remove_from_client** | **bool**|  | [optional] [default to True]
 **blacklist** | **bool**|  | [optional] [default to False]
 **skip_re_download** | **bool**|  | [optional] [default to False]

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

# **delete_queue_bulk**
> delete_queue_bulk(remove_from_client=remove_from_client, blacklist=blacklist, skip_re_download=skip_re_download, queue_bulk_resource=queue_bulk_resource)



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
    api_instance = readarr.QueueApi(api_client)
    remove_from_client = True # bool |  (optional) (default to True)
    blacklist = False # bool |  (optional) (default to False)
    skip_re_download = False # bool |  (optional) (default to False)
    queue_bulk_resource = readarr.QueueBulkResource() # QueueBulkResource |  (optional)

    try:
        api_instance.delete_queue_bulk(remove_from_client=remove_from_client, blacklist=blacklist, skip_re_download=skip_re_download, queue_bulk_resource=queue_bulk_resource)
    except Exception as e:
        print("Exception when calling QueueApi->delete_queue_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_from_client** | **bool**|  | [optional] [default to True]
 **blacklist** | **bool**|  | [optional] [default to False]
 **skip_re_download** | **bool**|  | [optional] [default to False]
 **queue_bulk_resource** | [**QueueBulkResource**](QueueBulkResource.md)|  | [optional] 

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

# **get_queue**
> QueueResourcePagingResource get_queue(include_unknown_author_items=include_unknown_author_items, include_author=include_author, include_book=include_book)



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
    api_instance = readarr.QueueApi(api_client)
    include_unknown_author_items = False # bool |  (optional) (default to False)
    include_author = False # bool |  (optional) (default to False)
    include_book = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.get_queue(include_unknown_author_items=include_unknown_author_items, include_author=include_author, include_book=include_book)
        print("The response of QueueApi->get_queue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueApi->get_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_unknown_author_items** | **bool**|  | [optional] [default to False]
 **include_author** | **bool**|  | [optional] [default to False]
 **include_book** | **bool**|  | [optional] [default to False]

### Return type

[**QueueResourcePagingResource**](QueueResourcePagingResource.md)

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

# **get_queue_by_id**
> QueueResource get_queue_by_id(id)



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
    api_instance = readarr.QueueApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_queue_by_id(id)
        print("The response of QueueApi->get_queue_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueApi->get_queue_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**QueueResource**](QueueResource.md)

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

