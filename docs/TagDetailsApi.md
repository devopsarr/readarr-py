# readarr.TagDetailsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tag_detail_by_id**](TagDetailsApi.md#get_tag_detail_by_id) | **GET** /api/v1/tag/detail/{id} | 
[**list_tag_detail**](TagDetailsApi.md#list_tag_detail) | **GET** /api/v1/tag/detail | 


# **get_tag_detail_by_id**
> TagDetailsResource get_tag_detail_by_id(id)



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
    api_instance = readarr.TagDetailsApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_tag_detail_by_id(id)
        print("The response of TagDetailsApi->get_tag_detail_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagDetailsApi->get_tag_detail_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TagDetailsResource**](TagDetailsResource.md)

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

# **list_tag_detail**
> List[TagDetailsResource] list_tag_detail()



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
    api_instance = readarr.TagDetailsApi(api_client)

    try:
        api_response = api_instance.list_tag_detail()
        print("The response of TagDetailsApi->list_tag_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagDetailsApi->list_tag_detail: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[TagDetailsResource]**](TagDetailsResource.md)

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

