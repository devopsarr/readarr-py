# readarr.DelayProfileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_delay_profile**](DelayProfileApi.md#create_delay_profile) | **POST** /api/v1/delayprofile | 
[**delete_delay_profile**](DelayProfileApi.md#delete_delay_profile) | **DELETE** /api/v1/delayprofile/{id} | 
[**get_delay_profile_by_id**](DelayProfileApi.md#get_delay_profile_by_id) | **GET** /api/v1/delayprofile/{id} | 
[**list_delay_profile**](DelayProfileApi.md#list_delay_profile) | **GET** /api/v1/delayprofile | 
[**update_delay_profile**](DelayProfileApi.md#update_delay_profile) | **PUT** /api/v1/delayprofile/{id} | 
[**update_delay_profile_reorder**](DelayProfileApi.md#update_delay_profile_reorder) | **PUT** /api/v1/delayprofile/reorder/{id} | 


# **create_delay_profile**
> DelayProfileResource create_delay_profile(delay_profile_resource=delay_profile_resource)



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
    api_instance = readarr.DelayProfileApi(api_client)
    delay_profile_resource = readarr.DelayProfileResource() # DelayProfileResource |  (optional)

    try:
        api_response = api_instance.create_delay_profile(delay_profile_resource=delay_profile_resource)
        print("The response of DelayProfileApi->create_delay_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DelayProfileApi->create_delay_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delay_profile_resource** | [**DelayProfileResource**](DelayProfileResource.md)|  | [optional] 

### Return type

[**DelayProfileResource**](DelayProfileResource.md)

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

# **delete_delay_profile**
> delete_delay_profile(id)



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
    api_instance = readarr.DelayProfileApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_delay_profile(id)
    except Exception as e:
        print("Exception when calling DelayProfileApi->delete_delay_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delay_profile_by_id**
> DelayProfileResource get_delay_profile_by_id(id)



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
    api_instance = readarr.DelayProfileApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_delay_profile_by_id(id)
        print("The response of DelayProfileApi->get_delay_profile_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DelayProfileApi->get_delay_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DelayProfileResource**](DelayProfileResource.md)

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

# **list_delay_profile**
> List[DelayProfileResource] list_delay_profile()



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
    api_instance = readarr.DelayProfileApi(api_client)

    try:
        api_response = api_instance.list_delay_profile()
        print("The response of DelayProfileApi->list_delay_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DelayProfileApi->list_delay_profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[DelayProfileResource]**](DelayProfileResource.md)

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

# **update_delay_profile**
> DelayProfileResource update_delay_profile(id, delay_profile_resource=delay_profile_resource)



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
    api_instance = readarr.DelayProfileApi(api_client)
    id = 'id_example' # str | 
    delay_profile_resource = readarr.DelayProfileResource() # DelayProfileResource |  (optional)

    try:
        api_response = api_instance.update_delay_profile(id, delay_profile_resource=delay_profile_resource)
        print("The response of DelayProfileApi->update_delay_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DelayProfileApi->update_delay_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **delay_profile_resource** | [**DelayProfileResource**](DelayProfileResource.md)|  | [optional] 

### Return type

[**DelayProfileResource**](DelayProfileResource.md)

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

# **update_delay_profile_reorder**
> update_delay_profile_reorder(id, after_id=after_id)



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
    api_instance = readarr.DelayProfileApi(api_client)
    id = 56 # int | 
    after_id = 56 # int |  (optional)

    try:
        api_instance.update_delay_profile_reorder(id, after_id=after_id)
    except Exception as e:
        print("Exception when calling DelayProfileApi->update_delay_profile_reorder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **after_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

