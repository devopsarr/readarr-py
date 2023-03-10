# readarr.MediaManagementConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_media_management_config**](MediaManagementConfigApi.md#get_media_management_config) | **GET** /api/v1/config/mediamanagement | 
[**get_media_management_config_by_id**](MediaManagementConfigApi.md#get_media_management_config_by_id) | **GET** /api/v1/config/mediamanagement/{id} | 
[**update_media_management_config**](MediaManagementConfigApi.md#update_media_management_config) | **PUT** /api/v1/config/mediamanagement/{id} | 


# **get_media_management_config**
> MediaManagementConfigResource get_media_management_config()



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
    api_instance = readarr.MediaManagementConfigApi(api_client)

    try:
        api_response = api_instance.get_media_management_config()
        print("The response of MediaManagementConfigApi->get_media_management_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaManagementConfigApi->get_media_management_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MediaManagementConfigResource**](MediaManagementConfigResource.md)

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

# **get_media_management_config_by_id**
> MediaManagementConfigResource get_media_management_config_by_id(id)



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
    api_instance = readarr.MediaManagementConfigApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_media_management_config_by_id(id)
        print("The response of MediaManagementConfigApi->get_media_management_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaManagementConfigApi->get_media_management_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MediaManagementConfigResource**](MediaManagementConfigResource.md)

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

# **update_media_management_config**
> MediaManagementConfigResource update_media_management_config(id, media_management_config_resource=media_management_config_resource)



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
    api_instance = readarr.MediaManagementConfigApi(api_client)
    id = 'id_example' # str | 
    media_management_config_resource = readarr.MediaManagementConfigResource() # MediaManagementConfigResource |  (optional)

    try:
        api_response = api_instance.update_media_management_config(id, media_management_config_resource=media_management_config_resource)
        print("The response of MediaManagementConfigApi->update_media_management_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaManagementConfigApi->update_media_management_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **media_management_config_resource** | [**MediaManagementConfigResource**](MediaManagementConfigResource.md)|  | [optional] 

### Return type

[**MediaManagementConfigResource**](MediaManagementConfigResource.md)

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

