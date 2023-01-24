# readarr.CustomFilterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_filter**](CustomFilterApi.md#create_custom_filter) | **POST** /api/v1/customfilter | 
[**delete_custom_filter**](CustomFilterApi.md#delete_custom_filter) | **DELETE** /api/v1/customfilter/{id} | 
[**get_custom_filter_by_id**](CustomFilterApi.md#get_custom_filter_by_id) | **GET** /api/v1/customfilter/{id} | 
[**list_custom_filter**](CustomFilterApi.md#list_custom_filter) | **GET** /api/v1/customfilter | 
[**update_custom_filter**](CustomFilterApi.md#update_custom_filter) | **PUT** /api/v1/customfilter/{id} | 


# **create_custom_filter**
> CustomFilterResource create_custom_filter(custom_filter_resource=custom_filter_resource)



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
    api_instance = readarr.CustomFilterApi(api_client)
    custom_filter_resource = readarr.CustomFilterResource() # CustomFilterResource |  (optional)

    try:
        api_response = api_instance.create_custom_filter(custom_filter_resource=custom_filter_resource)
        print("The response of CustomFilterApi->create_custom_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFilterApi->create_custom_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_filter_resource** | [**CustomFilterResource**](CustomFilterResource.md)|  | [optional] 

### Return type

[**CustomFilterResource**](CustomFilterResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_filter**
> delete_custom_filter(id)



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
    api_instance = readarr.CustomFilterApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_custom_filter(id)
    except Exception as e:
        print("Exception when calling CustomFilterApi->delete_custom_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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

# **get_custom_filter_by_id**
> CustomFilterResource get_custom_filter_by_id(id)



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
    api_instance = readarr.CustomFilterApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_custom_filter_by_id(id)
        print("The response of CustomFilterApi->get_custom_filter_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFilterApi->get_custom_filter_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CustomFilterResource**](CustomFilterResource.md)

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

# **list_custom_filter**
> List[CustomFilterResource] list_custom_filter()



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
    api_instance = readarr.CustomFilterApi(api_client)

    try:
        api_response = api_instance.list_custom_filter()
        print("The response of CustomFilterApi->list_custom_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFilterApi->list_custom_filter: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[CustomFilterResource]**](CustomFilterResource.md)

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

# **update_custom_filter**
> CustomFilterResource update_custom_filter(id, custom_filter_resource=custom_filter_resource)



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
    api_instance = readarr.CustomFilterApi(api_client)
    id = 'id_example' # str | 
    custom_filter_resource = readarr.CustomFilterResource() # CustomFilterResource |  (optional)

    try:
        api_response = api_instance.update_custom_filter(id, custom_filter_resource=custom_filter_resource)
        print("The response of CustomFilterApi->update_custom_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFilterApi->update_custom_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **custom_filter_resource** | [**CustomFilterResource**](CustomFilterResource.md)|  | [optional] 

### Return type

[**CustomFilterResource**](CustomFilterResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

