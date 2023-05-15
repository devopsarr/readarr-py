# readarr.BookFileApi

All URIs are relative to *http://localhost:8787*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_book_file**](BookFileApi.md#delete_book_file) | **DELETE** /api/v1/bookfile/{id} | 
[**delete_book_file_bulk**](BookFileApi.md#delete_book_file_bulk) | **DELETE** /api/v1/bookfile/bulk | 
[**get_book_file_by_id**](BookFileApi.md#get_book_file_by_id) | **GET** /api/v1/bookfile/{id} | 
[**list_book_file**](BookFileApi.md#list_book_file) | **GET** /api/v1/bookfile | 
[**put_book_file_editor**](BookFileApi.md#put_book_file_editor) | **PUT** /api/v1/bookfile/editor | 
[**update_book_file**](BookFileApi.md#update_book_file) | **PUT** /api/v1/bookfile/{id} | 


# **delete_book_file**
> delete_book_file(id)



### Example

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = readarr.BookFileApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_book_file(id)
    except Exception as e:
        print("Exception when calling BookFileApi->delete_book_file: %s\n" % e)
```

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
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
    api_instance = readarr.BookFileApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_book_file(id)
    except Exception as e:
        print("Exception when calling BookFileApi->delete_book_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_book_file_bulk**
> delete_book_file_bulk(book_file_list_resource=book_file_list_resource)



### Example

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = readarr.BookFileApi(api_client)
    book_file_list_resource = readarr.BookFileListResource() # BookFileListResource |  (optional)

    try:
        api_instance.delete_book_file_bulk(book_file_list_resource=book_file_list_resource)
    except Exception as e:
        print("Exception when calling BookFileApi->delete_book_file_bulk: %s\n" % e)
```

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
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
    api_instance = readarr.BookFileApi(api_client)
    book_file_list_resource = readarr.BookFileListResource() # BookFileListResource |  (optional)

    try:
        api_instance.delete_book_file_bulk(book_file_list_resource=book_file_list_resource)
    except Exception as e:
        print("Exception when calling BookFileApi->delete_book_file_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_file_list_resource** | [**BookFileListResource**](BookFileListResource.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_book_file_by_id**
> BookFileResource get_book_file_by_id(id)



### Example

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = readarr.BookFileApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_book_file_by_id(id)
        print("The response of BookFileApi->get_book_file_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookFileApi->get_book_file_by_id: %s\n" % e)
```

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
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
    api_instance = readarr.BookFileApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_book_file_by_id(id)
        print("The response of BookFileApi->get_book_file_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookFileApi->get_book_file_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BookFileResource**](BookFileResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_book_file**
> List[BookFileResource] list_book_file(author_id=author_id, book_file_ids=book_file_ids, book_id=book_id, unmapped=unmapped)



### Example

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = readarr.BookFileApi(api_client)
    author_id = 56 # int |  (optional)
    book_file_ids = [56] # List[int] |  (optional)
    book_id = [56] # List[int] |  (optional)
    unmapped = True # bool |  (optional)

    try:
        api_response = api_instance.list_book_file(author_id=author_id, book_file_ids=book_file_ids, book_id=book_id, unmapped=unmapped)
        print("The response of BookFileApi->list_book_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookFileApi->list_book_file: %s\n" % e)
```

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
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
    api_instance = readarr.BookFileApi(api_client)
    author_id = 56 # int |  (optional)
    book_file_ids = [56] # List[int] |  (optional)
    book_id = [56] # List[int] |  (optional)
    unmapped = True # bool |  (optional)

    try:
        api_response = api_instance.list_book_file(author_id=author_id, book_file_ids=book_file_ids, book_id=book_id, unmapped=unmapped)
        print("The response of BookFileApi->list_book_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookFileApi->list_book_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_id** | **int**|  | [optional] 
 **book_file_ids** | [**List[int]**](int.md)|  | [optional] 
 **book_id** | [**List[int]**](int.md)|  | [optional] 
 **unmapped** | **bool**|  | [optional] 

### Return type

[**List[BookFileResource]**](BookFileResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_book_file_editor**
> put_book_file_editor(book_file_list_resource=book_file_list_resource)



### Example

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = readarr.BookFileApi(api_client)
    book_file_list_resource = readarr.BookFileListResource() # BookFileListResource |  (optional)

    try:
        api_instance.put_book_file_editor(book_file_list_resource=book_file_list_resource)
    except Exception as e:
        print("Exception when calling BookFileApi->put_book_file_editor: %s\n" % e)
```

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
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
    api_instance = readarr.BookFileApi(api_client)
    book_file_list_resource = readarr.BookFileListResource() # BookFileListResource |  (optional)

    try:
        api_instance.put_book_file_editor(book_file_list_resource=book_file_list_resource)
    except Exception as e:
        print("Exception when calling BookFileApi->put_book_file_editor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_file_list_resource** | [**BookFileListResource**](BookFileListResource.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_book_file**
> BookFileResource update_book_file(id, book_file_resource=book_file_resource)



### Example

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = readarr.BookFileApi(api_client)
    id = 'id_example' # str | 
    book_file_resource = readarr.BookFileResource() # BookFileResource |  (optional)

    try:
        api_response = api_instance.update_book_file(id, book_file_resource=book_file_resource)
        print("The response of BookFileApi->update_book_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookFileApi->update_book_file: %s\n" % e)
```

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
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
    api_instance = readarr.BookFileApi(api_client)
    id = 'id_example' # str | 
    book_file_resource = readarr.BookFileResource() # BookFileResource |  (optional)

    try:
        api_response = api_instance.update_book_file(id, book_file_resource=book_file_resource)
        print("The response of BookFileApi->update_book_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookFileApi->update_book_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **book_file_resource** | [**BookFileResource**](BookFileResource.md)|  | [optional] 

### Return type

[**BookFileResource**](BookFileResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

