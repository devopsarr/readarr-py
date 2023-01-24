# readarr.RemotePathMappingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_remote_path_mapping**](RemotePathMappingApi.md#create_remote_path_mapping) | **POST** /api/v1/remotepathmapping | 
[**delete_remote_path_mapping**](RemotePathMappingApi.md#delete_remote_path_mapping) | **DELETE** /api/v1/remotepathmapping/{id} | 
[**get_remote_path_mapping_by_id**](RemotePathMappingApi.md#get_remote_path_mapping_by_id) | **GET** /api/v1/remotepathmapping/{id} | 
[**list_remote_path_mapping**](RemotePathMappingApi.md#list_remote_path_mapping) | **GET** /api/v1/remotepathmapping | 
[**update_remote_path_mapping**](RemotePathMappingApi.md#update_remote_path_mapping) | **PUT** /api/v1/remotepathmapping/{id} | 


# **create_remote_path_mapping**
> RemotePathMappingResource create_remote_path_mapping(remote_path_mapping_resource=remote_path_mapping_resource)



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
    api_instance = readarr.RemotePathMappingApi(api_client)
    remote_path_mapping_resource = readarr.RemotePathMappingResource() # RemotePathMappingResource |  (optional)

    try:
        api_response = api_instance.create_remote_path_mapping(remote_path_mapping_resource=remote_path_mapping_resource)
        print("The response of RemotePathMappingApi->create_remote_path_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotePathMappingApi->create_remote_path_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_path_mapping_resource** | [**RemotePathMappingResource**](RemotePathMappingResource.md)|  | [optional] 

### Return type

[**RemotePathMappingResource**](RemotePathMappingResource.md)

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

# **delete_remote_path_mapping**
> delete_remote_path_mapping(id)



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
    api_instance = readarr.RemotePathMappingApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_remote_path_mapping(id)
    except Exception as e:
        print("Exception when calling RemotePathMappingApi->delete_remote_path_mapping: %s\n" % e)
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

# **get_remote_path_mapping_by_id**
> RemotePathMappingResource get_remote_path_mapping_by_id(id)



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
    api_instance = readarr.RemotePathMappingApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_remote_path_mapping_by_id(id)
        print("The response of RemotePathMappingApi->get_remote_path_mapping_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotePathMappingApi->get_remote_path_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RemotePathMappingResource**](RemotePathMappingResource.md)

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

# **list_remote_path_mapping**
> List[RemotePathMappingResource] list_remote_path_mapping()



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
    api_instance = readarr.RemotePathMappingApi(api_client)

    try:
        api_response = api_instance.list_remote_path_mapping()
        print("The response of RemotePathMappingApi->list_remote_path_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotePathMappingApi->list_remote_path_mapping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[RemotePathMappingResource]**](RemotePathMappingResource.md)

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

# **update_remote_path_mapping**
> RemotePathMappingResource update_remote_path_mapping(id, remote_path_mapping_resource=remote_path_mapping_resource)



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
    api_instance = readarr.RemotePathMappingApi(api_client)
    id = 'id_example' # str | 
    remote_path_mapping_resource = readarr.RemotePathMappingResource() # RemotePathMappingResource |  (optional)

    try:
        api_response = api_instance.update_remote_path_mapping(id, remote_path_mapping_resource=remote_path_mapping_resource)
        print("The response of RemotePathMappingApi->update_remote_path_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotePathMappingApi->update_remote_path_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **remote_path_mapping_resource** | [**RemotePathMappingResource**](RemotePathMappingResource.md)|  | [optional] 

### Return type

[**RemotePathMappingResource**](RemotePathMappingResource.md)

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

