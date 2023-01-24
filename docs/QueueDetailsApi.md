# readarr.QueueDetailsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_queue_details_by_id**](QueueDetailsApi.md#get_queue_details_by_id) | **GET** /api/v1/queue/details/{id} | 
[**list_queue_details**](QueueDetailsApi.md#list_queue_details) | **GET** /api/v1/queue/details | 


# **get_queue_details_by_id**
> QueueResource get_queue_details_by_id(id)



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
    api_instance = readarr.QueueDetailsApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_queue_details_by_id(id)
        print("The response of QueueDetailsApi->get_queue_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueDetailsApi->get_queue_details_by_id: %s\n" % e)
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

# **list_queue_details**
> List[QueueResource] list_queue_details(author_id=author_id, book_ids=book_ids, include_author=include_author, include_book=include_book)



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
    api_instance = readarr.QueueDetailsApi(api_client)
    author_id = 56 # int |  (optional)
    book_ids = [56] # List[int] |  (optional)
    include_author = False # bool |  (optional) (default to False)
    include_book = True # bool |  (optional) (default to True)

    try:
        api_response = api_instance.list_queue_details(author_id=author_id, book_ids=book_ids, include_author=include_author, include_book=include_book)
        print("The response of QueueDetailsApi->list_queue_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueDetailsApi->list_queue_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_id** | **int**|  | [optional] 
 **book_ids** | [**List[int]**](int.md)|  | [optional] 
 **include_author** | **bool**|  | [optional] [default to False]
 **include_book** | **bool**|  | [optional] [default to True]

### Return type

[**List[QueueResource]**](QueueResource.md)

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

