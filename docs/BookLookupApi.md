# readarr.BookLookupApi

All URIs are relative to *http://localhost:8787*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_book_lookup**](BookLookupApi.md#get_book_lookup) | **GET** /api/v1/book/lookup | 


# **get_book_lookup**
> get_book_lookup(term=term)

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
    api_instance = readarr.BookLookupApi(api_client)
    term = 'term_example' # str |  (optional)

    try:
        api_instance.get_book_lookup(term=term)
    except Exception as e:
        print("Exception when calling BookLookupApi->get_book_lookup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  | [optional] 

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

