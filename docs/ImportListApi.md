# readarr.ImportListApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_import_list**](ImportListApi.md#create_import_list) | **POST** /api/v1/importlist | 
[**create_import_list_action_by_name**](ImportListApi.md#create_import_list_action_by_name) | **POST** /api/v1/importlist/action/{name} | 
[**delete_import_list**](ImportListApi.md#delete_import_list) | **DELETE** /api/v1/importlist/{id} | 
[**get_import_list_by_id**](ImportListApi.md#get_import_list_by_id) | **GET** /api/v1/importlist/{id} | 
[**list_import_list**](ImportListApi.md#list_import_list) | **GET** /api/v1/importlist | 
[**list_import_list_schema**](ImportListApi.md#list_import_list_schema) | **GET** /api/v1/importlist/schema | 
[**test_import_list**](ImportListApi.md#test_import_list) | **POST** /api/v1/importlist/test | 
[**testall_import_list**](ImportListApi.md#testall_import_list) | **POST** /api/v1/importlist/testall | 
[**update_import_list**](ImportListApi.md#update_import_list) | **PUT** /api/v1/importlist/{id} | 


# **create_import_list**
> ImportListResource create_import_list(import_list_resource=import_list_resource)



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
    api_instance = readarr.ImportListApi(api_client)
    import_list_resource = readarr.ImportListResource() # ImportListResource |  (optional)

    try:
        api_response = api_instance.create_import_list(import_list_resource=import_list_resource)
        print("The response of ImportListApi->create_import_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportListApi->create_import_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_list_resource** | [**ImportListResource**](ImportListResource.md)|  | [optional] 

### Return type

[**ImportListResource**](ImportListResource.md)

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

# **create_import_list_action_by_name**
> create_import_list_action_by_name(name, import_list_resource=import_list_resource)



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
    api_instance = readarr.ImportListApi(api_client)
    name = 'name_example' # str | 
    import_list_resource = readarr.ImportListResource() # ImportListResource |  (optional)

    try:
        api_instance.create_import_list_action_by_name(name, import_list_resource=import_list_resource)
    except Exception as e:
        print("Exception when calling ImportListApi->create_import_list_action_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **import_list_resource** | [**ImportListResource**](ImportListResource.md)|  | [optional] 

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

# **delete_import_list**
> delete_import_list(id)



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
    api_instance = readarr.ImportListApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_import_list(id)
    except Exception as e:
        print("Exception when calling ImportListApi->delete_import_list: %s\n" % e)
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

# **get_import_list_by_id**
> ImportListResource get_import_list_by_id(id)



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
    api_instance = readarr.ImportListApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_import_list_by_id(id)
        print("The response of ImportListApi->get_import_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportListApi->get_import_list_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ImportListResource**](ImportListResource.md)

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

# **list_import_list**
> List[ImportListResource] list_import_list()



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
    api_instance = readarr.ImportListApi(api_client)

    try:
        api_response = api_instance.list_import_list()
        print("The response of ImportListApi->list_import_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportListApi->list_import_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ImportListResource]**](ImportListResource.md)

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

# **list_import_list_schema**
> List[ImportListResource] list_import_list_schema()



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
    api_instance = readarr.ImportListApi(api_client)

    try:
        api_response = api_instance.list_import_list_schema()
        print("The response of ImportListApi->list_import_list_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportListApi->list_import_list_schema: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ImportListResource]**](ImportListResource.md)

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

# **test_import_list**
> test_import_list(import_list_resource=import_list_resource)



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
    api_instance = readarr.ImportListApi(api_client)
    import_list_resource = readarr.ImportListResource() # ImportListResource |  (optional)

    try:
        api_instance.test_import_list(import_list_resource=import_list_resource)
    except Exception as e:
        print("Exception when calling ImportListApi->test_import_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_list_resource** | [**ImportListResource**](ImportListResource.md)|  | [optional] 

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

# **testall_import_list**
> testall_import_list()



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
    api_instance = readarr.ImportListApi(api_client)

    try:
        api_instance.testall_import_list()
    except Exception as e:
        print("Exception when calling ImportListApi->testall_import_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **update_import_list**
> ImportListResource update_import_list(id, import_list_resource=import_list_resource)



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
    api_instance = readarr.ImportListApi(api_client)
    id = 'id_example' # str | 
    import_list_resource = readarr.ImportListResource() # ImportListResource |  (optional)

    try:
        api_response = api_instance.update_import_list(id, import_list_resource=import_list_resource)
        print("The response of ImportListApi->update_import_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportListApi->update_import_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **import_list_resource** | [**ImportListResource**](ImportListResource.md)|  | [optional] 

### Return type

[**ImportListResource**](ImportListResource.md)

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

