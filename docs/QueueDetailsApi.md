# readarr.QueueDetailsApi

All URIs are relative to *http://localhost:8787*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_queue_details**](QueueDetailsApi.md#list_queue_details) | **GET** /api/v1/queue/details | 


# **list_queue_details**
> List[QueueResource] list_queue_details(author_id=author_id, book_ids=book_ids, include_author=include_author, include_book=include_book)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import readarr
from readarr.models.queue_resource import QueueResource
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

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

