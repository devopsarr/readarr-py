# readarr.ReleaseApi

All URIs are relative to *http://localhost:8787*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_release**](ReleaseApi.md#create_release) | **POST** /api/v1/release | 
[**list_release**](ReleaseApi.md#list_release) | **GET** /api/v1/release | 


# **create_release**
> ReleaseResource create_release(release_resource=release_resource)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import readarr
from readarr.models.release_resource import ReleaseResource
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

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_release**
> List[ReleaseResource] list_release(book_id=book_id, author_id=author_id)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import readarr
from readarr.models.release_resource import ReleaseResource
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

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

