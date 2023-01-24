# readarr.LanguageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_language_by_id**](LanguageApi.md#get_language_by_id) | **GET** /api/v1/language/{id} | 
[**list_language**](LanguageApi.md#list_language) | **GET** /api/v1/language | 


# **get_language_by_id**
> LanguageResource get_language_by_id(id)



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
    api_instance = readarr.LanguageApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_language_by_id(id)
        print("The response of LanguageApi->get_language_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LanguageApi->get_language_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**LanguageResource**](LanguageResource.md)

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

# **list_language**
> List[LanguageResource] list_language()



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
    api_instance = readarr.LanguageApi(api_client)

    try:
        api_response = api_instance.list_language()
        print("The response of LanguageApi->list_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LanguageApi->list_language: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[LanguageResource]**](LanguageResource.md)

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

