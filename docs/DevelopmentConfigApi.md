# readarr.DevelopmentConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_development_config**](DevelopmentConfigApi.md#get_development_config) | **GET** /api/v1/config/development | 
[**get_development_config_by_id**](DevelopmentConfigApi.md#get_development_config_by_id) | **GET** /api/v1/config/development/{id} | 
[**update_development_config**](DevelopmentConfigApi.md#update_development_config) | **PUT** /api/v1/config/development/{id} | 


# **get_development_config**
> DevelopmentConfigResource get_development_config()



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
    api_instance = readarr.DevelopmentConfigApi(api_client)

    try:
        api_response = api_instance.get_development_config()
        print("The response of DevelopmentConfigApi->get_development_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopmentConfigApi->get_development_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DevelopmentConfigResource**](DevelopmentConfigResource.md)

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

# **get_development_config_by_id**
> DevelopmentConfigResource get_development_config_by_id(id)



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
    api_instance = readarr.DevelopmentConfigApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_development_config_by_id(id)
        print("The response of DevelopmentConfigApi->get_development_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopmentConfigApi->get_development_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DevelopmentConfigResource**](DevelopmentConfigResource.md)

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

# **update_development_config**
> DevelopmentConfigResource update_development_config(id, development_config_resource=development_config_resource)



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
    api_instance = readarr.DevelopmentConfigApi(api_client)
    id = 'id_example' # str | 
    development_config_resource = readarr.DevelopmentConfigResource() # DevelopmentConfigResource |  (optional)

    try:
        api_response = api_instance.update_development_config(id, development_config_resource=development_config_resource)
        print("The response of DevelopmentConfigApi->update_development_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopmentConfigApi->update_development_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **development_config_resource** | [**DevelopmentConfigResource**](DevelopmentConfigResource.md)|  | [optional] 

### Return type

[**DevelopmentConfigResource**](DevelopmentConfigResource.md)

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

