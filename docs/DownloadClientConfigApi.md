# readarr.DownloadClientConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_download_client_config**](DownloadClientConfigApi.md#get_download_client_config) | **GET** /api/v1/config/downloadclient | 
[**get_download_client_config_by_id**](DownloadClientConfigApi.md#get_download_client_config_by_id) | **GET** /api/v1/config/downloadclient/{id} | 
[**update_download_client_config**](DownloadClientConfigApi.md#update_download_client_config) | **PUT** /api/v1/config/downloadclient/{id} | 


# **get_download_client_config**
> DownloadClientConfigResource get_download_client_config()



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
    api_instance = readarr.DownloadClientConfigApi(api_client)

    try:
        api_response = api_instance.get_download_client_config()
        print("The response of DownloadClientConfigApi->get_download_client_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloadClientConfigApi->get_download_client_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DownloadClientConfigResource**](DownloadClientConfigResource.md)

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

# **get_download_client_config_by_id**
> DownloadClientConfigResource get_download_client_config_by_id(id)



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
    api_instance = readarr.DownloadClientConfigApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_download_client_config_by_id(id)
        print("The response of DownloadClientConfigApi->get_download_client_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloadClientConfigApi->get_download_client_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DownloadClientConfigResource**](DownloadClientConfigResource.md)

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

# **update_download_client_config**
> DownloadClientConfigResource update_download_client_config(id, download_client_config_resource=download_client_config_resource)



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
    api_instance = readarr.DownloadClientConfigApi(api_client)
    id = 'id_example' # str | 
    download_client_config_resource = readarr.DownloadClientConfigResource() # DownloadClientConfigResource |  (optional)

    try:
        api_response = api_instance.update_download_client_config(id, download_client_config_resource=download_client_config_resource)
        print("The response of DownloadClientConfigApi->update_download_client_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloadClientConfigApi->update_download_client_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **download_client_config_resource** | [**DownloadClientConfigResource**](DownloadClientConfigResource.md)|  | [optional] 

### Return type

[**DownloadClientConfigResource**](DownloadClientConfigResource.md)

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

