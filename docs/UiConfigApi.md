# readarr.UiConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ui_config**](UiConfigApi.md#get_ui_config) | **GET** /api/v1/config/ui | 
[**get_ui_config_by_id**](UiConfigApi.md#get_ui_config_by_id) | **GET** /api/v1/config/ui/{id} | 
[**update_ui_config**](UiConfigApi.md#update_ui_config) | **PUT** /api/v1/config/ui/{id} | 


# **get_ui_config**
> UiConfigResource get_ui_config()



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
    api_instance = readarr.UiConfigApi(api_client)

    try:
        api_response = api_instance.get_ui_config()
        print("The response of UiConfigApi->get_ui_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiConfigApi->get_ui_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UiConfigResource**](UiConfigResource.md)

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

# **get_ui_config_by_id**
> UiConfigResource get_ui_config_by_id(id)



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
    api_instance = readarr.UiConfigApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_ui_config_by_id(id)
        print("The response of UiConfigApi->get_ui_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiConfigApi->get_ui_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UiConfigResource**](UiConfigResource.md)

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

# **update_ui_config**
> UiConfigResource update_ui_config(id, ui_config_resource=ui_config_resource)



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
    api_instance = readarr.UiConfigApi(api_client)
    id = 'id_example' # str | 
    ui_config_resource = readarr.UiConfigResource() # UiConfigResource |  (optional)

    try:
        api_response = api_instance.update_ui_config(id, ui_config_resource=ui_config_resource)
        print("The response of UiConfigApi->update_ui_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiConfigApi->update_ui_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ui_config_resource** | [**UiConfigResource**](UiConfigResource.md)|  | [optional] 

### Return type

[**UiConfigResource**](UiConfigResource.md)

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

