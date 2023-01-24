# readarr.IndexerConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_indexer_config**](IndexerConfigApi.md#get_indexer_config) | **GET** /api/v1/config/indexer | 
[**get_indexer_config_by_id**](IndexerConfigApi.md#get_indexer_config_by_id) | **GET** /api/v1/config/indexer/{id} | 
[**update_indexer_config**](IndexerConfigApi.md#update_indexer_config) | **PUT** /api/v1/config/indexer/{id} | 


# **get_indexer_config**
> IndexerConfigResource get_indexer_config()



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
    api_instance = readarr.IndexerConfigApi(api_client)

    try:
        api_response = api_instance.get_indexer_config()
        print("The response of IndexerConfigApi->get_indexer_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexerConfigApi->get_indexer_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IndexerConfigResource**](IndexerConfigResource.md)

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

# **get_indexer_config_by_id**
> IndexerConfigResource get_indexer_config_by_id(id)



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
    api_instance = readarr.IndexerConfigApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_indexer_config_by_id(id)
        print("The response of IndexerConfigApi->get_indexer_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexerConfigApi->get_indexer_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**IndexerConfigResource**](IndexerConfigResource.md)

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

# **update_indexer_config**
> IndexerConfigResource update_indexer_config(id, indexer_config_resource=indexer_config_resource)



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
    api_instance = readarr.IndexerConfigApi(api_client)
    id = 'id_example' # str | 
    indexer_config_resource = readarr.IndexerConfigResource() # IndexerConfigResource |  (optional)

    try:
        api_response = api_instance.update_indexer_config(id, indexer_config_resource=indexer_config_resource)
        print("The response of IndexerConfigApi->update_indexer_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexerConfigApi->update_indexer_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **indexer_config_resource** | [**IndexerConfigResource**](IndexerConfigResource.md)|  | [optional] 

### Return type

[**IndexerConfigResource**](IndexerConfigResource.md)

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

