# readarr.MediaCoverApi

All URIs are relative to *http://localhost:8787*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_media_cover_author_by_filename**](MediaCoverApi.md#get_media_cover_author_by_filename) | **GET** /api/v1/mediacover/author/{authorId}/{filename} | 
[**get_media_cover_book_by_filename**](MediaCoverApi.md#get_media_cover_book_by_filename) | **GET** /api/v1/mediacover/book/{bookId}/{filename} | 


# **get_media_cover_author_by_filename**
> get_media_cover_author_by_filename(author_id, filename)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import readarr
from readarr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8787
# See configuration.py for a list of all supported configuration parameters.
configuration = readarr.Configuration(
    host = "http://localhost:8787"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with readarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = readarr.MediaCoverApi(api_client)
    author_id = 56 # int | 
    filename = 'filename_example' # str | 

    try:
        api_instance.get_media_cover_author_by_filename(author_id, filename)
    except Exception as e:
        print("Exception when calling MediaCoverApi->get_media_cover_author_by_filename: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_id** | **int**|  | 
 **filename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_cover_book_by_filename**
> get_media_cover_book_by_filename(book_id, filename)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import readarr
from readarr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8787
# See configuration.py for a list of all supported configuration parameters.
configuration = readarr.Configuration(
    host = "http://localhost:8787"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with readarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = readarr.MediaCoverApi(api_client)
    book_id = 56 # int | 
    filename = 'filename_example' # str | 

    try:
        api_instance.get_media_cover_book_by_filename(book_id, filename)
    except Exception as e:
        print("Exception when calling MediaCoverApi->get_media_cover_book_by_filename: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**|  | 
 **filename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

