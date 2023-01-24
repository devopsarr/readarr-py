# readarr.HostConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_host_config**](HostConfigApi.md#get_host_config) | **GET** /api/v1/config/host | 
[**get_host_config_by_id**](HostConfigApi.md#get_host_config_by_id) | **GET** /api/v1/config/host/{id} | 
[**update_host_config**](HostConfigApi.md#update_host_config) | **PUT** /api/v1/config/host/{id} | 


# **get_host_config**
> HostConfigResource get_host_config()



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
    api_instance = readarr.HostConfigApi(api_client)

    try:
        api_response = api_instance.get_host_config()
        print("The response of HostConfigApi->get_host_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostConfigApi->get_host_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HostConfigResource**](HostConfigResource.md)

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

# **get_host_config_by_id**
> HostConfigResource get_host_config_by_id(id)



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
    api_instance = readarr.HostConfigApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_host_config_by_id(id)
        print("The response of HostConfigApi->get_host_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostConfigApi->get_host_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**HostConfigResource**](HostConfigResource.md)

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

# **update_host_config**
> HostConfigResource update_host_config(id, host_config_resource=host_config_resource)



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
    api_instance = readarr.HostConfigApi(api_client)
    id = 'id_example' # str | 
    host_config_resource = readarr.HostConfigResource() # HostConfigResource |  (optional)

    try:
        api_response = api_instance.update_host_config(id, host_config_resource=host_config_resource)
        print("The response of HostConfigApi->update_host_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostConfigApi->update_host_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **host_config_resource** | [**HostConfigResource**](HostConfigResource.md)|  | [optional] 

### Return type

[**HostConfigResource**](HostConfigResource.md)

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

