# readarr.HistoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_history_failed**](HistoryApi.md#create_history_failed) | **POST** /api/v1/history/failed | 
[**get_history**](HistoryApi.md#get_history) | **GET** /api/v1/history | 
[**list_history_author**](HistoryApi.md#list_history_author) | **GET** /api/v1/history/author | 
[**list_history_since**](HistoryApi.md#list_history_since) | **GET** /api/v1/history/since | 


# **create_history_failed**
> create_history_failed(body=body)



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
    api_instance = readarr.HistoryApi(api_client)
    body = 56 # int |  (optional)

    try:
        api_instance.create_history_failed(body=body)
    except Exception as e:
        print("Exception when calling HistoryApi->create_history_failed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **int**|  | [optional] 

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

# **get_history**
> HistoryResourcePagingResource get_history(include_author=include_author, include_book=include_book)



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
    api_instance = readarr.HistoryApi(api_client)
    include_author = False # bool |  (optional) (default to False)
    include_book = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.get_history(include_author=include_author, include_book=include_book)
        print("The response of HistoryApi->get_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoryApi->get_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_author** | **bool**|  | [optional] [default to False]
 **include_book** | **bool**|  | [optional] [default to False]

### Return type

[**HistoryResourcePagingResource**](HistoryResourcePagingResource.md)

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

# **list_history_author**
> List[HistoryResource] list_history_author(author_id=author_id, book_id=book_id, event_type=event_type, include_author=include_author, include_book=include_book)



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
    api_instance = readarr.HistoryApi(api_client)
    author_id = 56 # int |  (optional)
    book_id = 56 # int |  (optional)
    event_type = readarr.HistoryEventType() # HistoryEventType |  (optional)
    include_author = False # bool |  (optional) (default to False)
    include_book = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.list_history_author(author_id=author_id, book_id=book_id, event_type=event_type, include_author=include_author, include_book=include_book)
        print("The response of HistoryApi->list_history_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoryApi->list_history_author: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_id** | **int**|  | [optional] 
 **book_id** | **int**|  | [optional] 
 **event_type** | [**HistoryEventType**](.md)|  | [optional] 
 **include_author** | **bool**|  | [optional] [default to False]
 **include_book** | **bool**|  | [optional] [default to False]

### Return type

[**List[HistoryResource]**](HistoryResource.md)

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

# **list_history_since**
> List[HistoryResource] list_history_since(var_date=var_date, event_type=event_type, include_author=include_author, include_book=include_book)



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
    api_instance = readarr.HistoryApi(api_client)
    var_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    event_type = readarr.HistoryEventType() # HistoryEventType |  (optional)
    include_author = False # bool |  (optional) (default to False)
    include_book = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.list_history_since(var_date=var_date, event_type=event_type, include_author=include_author, include_book=include_book)
        print("The response of HistoryApi->list_history_since:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoryApi->list_history_since: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **datetime**|  | [optional] 
 **event_type** | [**HistoryEventType**](.md)|  | [optional] 
 **include_author** | **bool**|  | [optional] [default to False]
 **include_book** | **bool**|  | [optional] [default to False]

### Return type

[**List[HistoryResource]**](HistoryResource.md)

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

