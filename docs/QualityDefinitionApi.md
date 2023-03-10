# readarr.QualityDefinitionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_quality_definition_by_id**](QualityDefinitionApi.md#get_quality_definition_by_id) | **GET** /api/v1/qualitydefinition/{id} | 
[**list_quality_definition**](QualityDefinitionApi.md#list_quality_definition) | **GET** /api/v1/qualitydefinition | 
[**put_quality_definition_update**](QualityDefinitionApi.md#put_quality_definition_update) | **PUT** /api/v1/qualitydefinition/update | 
[**update_quality_definition**](QualityDefinitionApi.md#update_quality_definition) | **PUT** /api/v1/qualitydefinition/{id} | 


# **get_quality_definition_by_id**
> QualityDefinitionResource get_quality_definition_by_id(id)



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
    api_instance = readarr.QualityDefinitionApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_quality_definition_by_id(id)
        print("The response of QualityDefinitionApi->get_quality_definition_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityDefinitionApi->get_quality_definition_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**QualityDefinitionResource**](QualityDefinitionResource.md)

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

# **list_quality_definition**
> List[QualityDefinitionResource] list_quality_definition()



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
    api_instance = readarr.QualityDefinitionApi(api_client)

    try:
        api_response = api_instance.list_quality_definition()
        print("The response of QualityDefinitionApi->list_quality_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityDefinitionApi->list_quality_definition: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[QualityDefinitionResource]**](QualityDefinitionResource.md)

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

# **put_quality_definition_update**
> put_quality_definition_update(quality_definition_resource=quality_definition_resource)



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
    api_instance = readarr.QualityDefinitionApi(api_client)
    quality_definition_resource = [readarr.QualityDefinitionResource()] # List[QualityDefinitionResource] |  (optional)

    try:
        api_instance.put_quality_definition_update(quality_definition_resource=quality_definition_resource)
    except Exception as e:
        print("Exception when calling QualityDefinitionApi->put_quality_definition_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quality_definition_resource** | [**List[QualityDefinitionResource]**](QualityDefinitionResource.md)|  | [optional] 

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

# **update_quality_definition**
> QualityDefinitionResource update_quality_definition(id, quality_definition_resource=quality_definition_resource)



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
    api_instance = readarr.QualityDefinitionApi(api_client)
    id = 'id_example' # str | 
    quality_definition_resource = readarr.QualityDefinitionResource() # QualityDefinitionResource |  (optional)

    try:
        api_response = api_instance.update_quality_definition(id, quality_definition_resource=quality_definition_resource)
        print("The response of QualityDefinitionApi->update_quality_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityDefinitionApi->update_quality_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **quality_definition_resource** | [**QualityDefinitionResource**](QualityDefinitionResource.md)|  | [optional] 

### Return type

[**QualityDefinitionResource**](QualityDefinitionResource.md)

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

