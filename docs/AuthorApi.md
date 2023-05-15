# readarr.AuthorApi

All URIs are relative to *http://localhost:8787*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_author**](AuthorApi.md#create_author) | **POST** /api/v1/author | 
[**delete_author**](AuthorApi.md#delete_author) | **DELETE** /api/v1/author/{id} | 
[**get_author_by_id**](AuthorApi.md#get_author_by_id) | **GET** /api/v1/author/{id} | 
[**list_author**](AuthorApi.md#list_author) | **GET** /api/v1/author | 
[**update_author**](AuthorApi.md#update_author) | **PUT** /api/v1/author/{id} | 


# **create_author**
> AuthorResource create_author(author_resource=author_resource)



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
    api_instance = readarr.AuthorApi(api_client)
    author_resource = readarr.AuthorResource() # AuthorResource |  (optional)

    try:
        api_response = api_instance.create_author(author_resource=author_resource)
        print("The response of AuthorApi->create_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorApi->create_author: %s\n" % e)
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
    api_instance = readarr.AuthorApi(api_client)
    author_resource = readarr.AuthorResource() # AuthorResource |  (optional)

    try:
        api_response = api_instance.create_author(author_resource=author_resource)
        print("The response of AuthorApi->create_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorApi->create_author: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_resource** | [**AuthorResource**](AuthorResource.md)|  | [optional] 

### Return type

[**AuthorResource**](AuthorResource.md)

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

# **delete_author**
> delete_author(id)



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
    api_instance = readarr.AuthorApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_author(id)
    except Exception as e:
        print("Exception when calling AuthorApi->delete_author: %s\n" % e)
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
    api_instance = readarr.AuthorApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_author(id)
    except Exception as e:
        print("Exception when calling AuthorApi->delete_author: %s\n" % e)
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

# **get_author_by_id**
> AuthorResource get_author_by_id(id)



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
    api_instance = readarr.AuthorApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_author_by_id(id)
        print("The response of AuthorApi->get_author_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorApi->get_author_by_id: %s\n" % e)
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
    api_instance = readarr.AuthorApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_author_by_id(id)
        print("The response of AuthorApi->get_author_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorApi->get_author_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AuthorResource**](AuthorResource.md)

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

# **list_author**
> List[AuthorResource] list_author()



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
    api_instance = readarr.AuthorApi(api_client)

    try:
        api_response = api_instance.list_author()
        print("The response of AuthorApi->list_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorApi->list_author: %s\n" % e)
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
    api_instance = readarr.AuthorApi(api_client)

    try:
        api_response = api_instance.list_author()
        print("The response of AuthorApi->list_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorApi->list_author: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[AuthorResource]**](AuthorResource.md)

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

# **update_author**
> AuthorResource update_author(id, author_resource=author_resource)



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
    api_instance = readarr.AuthorApi(api_client)
    id = 'id_example' # str | 
    author_resource = readarr.AuthorResource() # AuthorResource |  (optional)

    try:
        api_response = api_instance.update_author(id, author_resource=author_resource)
        print("The response of AuthorApi->update_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorApi->update_author: %s\n" % e)
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
    api_instance = readarr.AuthorApi(api_client)
    id = 'id_example' # str | 
    author_resource = readarr.AuthorResource() # AuthorResource |  (optional)

    try:
        api_response = api_instance.update_author(id, author_resource=author_resource)
        print("The response of AuthorApi->update_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorApi->update_author: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **author_resource** | [**AuthorResource**](AuthorResource.md)|  | [optional] 

### Return type

[**AuthorResource**](AuthorResource.md)

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

