# readarr.MediaCoverApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_media_cover_authorauthor_id_by_filename**](MediaCoverApi.md#get_media_cover_authorauthor_id_by_filename) | **GET** /api/v1/mediacover/author/{authorId}/{filename} | 
[**get_media_cover_bookbook_id_by_filename**](MediaCoverApi.md#get_media_cover_bookbook_id_by_filename) | **GET** /api/v1/mediacover/book/{bookId}/{filename} | 


# **get_media_cover_authorauthor_id_by_filename**
> get_media_cover_authorauthor_id_by_filename(author_id, filename)



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
    api_instance = readarr.MediaCoverApi(api_client)
    author_id = 56 # int | 
    filename = 'filename_example' # str | 

    try:
        api_instance.get_media_cover_authorauthor_id_by_filename(author_id, filename)
    except Exception as e:
        print("Exception when calling MediaCoverApi->get_media_cover_authorauthor_id_by_filename: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_id** | **int**|  | 
 **filename** | **str**|  | 

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

# **get_media_cover_bookbook_id_by_filename**
> get_media_cover_bookbook_id_by_filename(book_id, filename)



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
    api_instance = readarr.MediaCoverApi(api_client)
    book_id = 56 # int | 
    filename = 'filename_example' # str | 

    try:
        api_instance.get_media_cover_bookbook_id_by_filename(book_id, filename)
    except Exception as e:
        print("Exception when calling MediaCoverApi->get_media_cover_bookbook_id_by_filename: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**|  | 
 **filename** | **str**|  | 

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

