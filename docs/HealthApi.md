# readarr.HealthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health_by_id**](HealthApi.md#get_health_by_id) | **GET** /api/v1/health/{id} | 
[**list_health**](HealthApi.md#list_health) | **GET** /api/v1/health | 


# **get_health_by_id**
> HealthResource get_health_by_id(id)



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
    api_instance = readarr.HealthApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_health_by_id(id)
        print("The response of HealthApi->get_health_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->get_health_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**HealthResource**](HealthResource.md)

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

# **list_health**
> List[HealthResource] list_health()



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
    api_instance = readarr.HealthApi(api_client)

    try:
        api_response = api_instance.list_health()
        print("The response of HealthApi->list_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->list_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[HealthResource]**](HealthResource.md)

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

