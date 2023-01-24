# readarr.MetadataProviderConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metadata_provider_config**](MetadataProviderConfigApi.md#get_metadata_provider_config) | **GET** /api/v1/config/metadataprovider | 
[**get_metadata_provider_config_by_id**](MetadataProviderConfigApi.md#get_metadata_provider_config_by_id) | **GET** /api/v1/config/metadataprovider/{id} | 
[**update_metadata_provider_config**](MetadataProviderConfigApi.md#update_metadata_provider_config) | **PUT** /api/v1/config/metadataprovider/{id} | 


# **get_metadata_provider_config**
> MetadataProviderConfigResource get_metadata_provider_config()



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
    api_instance = readarr.MetadataProviderConfigApi(api_client)

    try:
        api_response = api_instance.get_metadata_provider_config()
        print("The response of MetadataProviderConfigApi->get_metadata_provider_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataProviderConfigApi->get_metadata_provider_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetadataProviderConfigResource**](MetadataProviderConfigResource.md)

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

# **get_metadata_provider_config_by_id**
> MetadataProviderConfigResource get_metadata_provider_config_by_id(id)



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
    api_instance = readarr.MetadataProviderConfigApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_metadata_provider_config_by_id(id)
        print("The response of MetadataProviderConfigApi->get_metadata_provider_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataProviderConfigApi->get_metadata_provider_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MetadataProviderConfigResource**](MetadataProviderConfigResource.md)

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

# **update_metadata_provider_config**
> MetadataProviderConfigResource update_metadata_provider_config(id, metadata_provider_config_resource=metadata_provider_config_resource)



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
    api_instance = readarr.MetadataProviderConfigApi(api_client)
    id = 'id_example' # str | 
    metadata_provider_config_resource = readarr.MetadataProviderConfigResource() # MetadataProviderConfigResource |  (optional)

    try:
        api_response = api_instance.update_metadata_provider_config(id, metadata_provider_config_resource=metadata_provider_config_resource)
        print("The response of MetadataProviderConfigApi->update_metadata_provider_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataProviderConfigApi->update_metadata_provider_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **metadata_provider_config_resource** | [**MetadataProviderConfigResource**](MetadataProviderConfigResource.md)|  | [optional] 

### Return type

[**MetadataProviderConfigResource**](MetadataProviderConfigResource.md)

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

