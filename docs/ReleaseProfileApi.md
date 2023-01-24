# readarr.ReleaseProfileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_release_profile**](ReleaseProfileApi.md#create_release_profile) | **POST** /api/v1/releaseprofile | 
[**delete_release_profile**](ReleaseProfileApi.md#delete_release_profile) | **DELETE** /api/v1/releaseprofile/{id} | 
[**get_release_profile_by_id**](ReleaseProfileApi.md#get_release_profile_by_id) | **GET** /api/v1/releaseprofile/{id} | 
[**list_release_profile**](ReleaseProfileApi.md#list_release_profile) | **GET** /api/v1/releaseprofile | 
[**update_release_profile**](ReleaseProfileApi.md#update_release_profile) | **PUT** /api/v1/releaseprofile/{id} | 


# **create_release_profile**
> ReleaseProfileResource create_release_profile(release_profile_resource=release_profile_resource)



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
    api_instance = readarr.ReleaseProfileApi(api_client)
    release_profile_resource = readarr.ReleaseProfileResource() # ReleaseProfileResource |  (optional)

    try:
        api_response = api_instance.create_release_profile(release_profile_resource=release_profile_resource)
        print("The response of ReleaseProfileApi->create_release_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleaseProfileApi->create_release_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_profile_resource** | [**ReleaseProfileResource**](ReleaseProfileResource.md)|  | [optional] 

### Return type

[**ReleaseProfileResource**](ReleaseProfileResource.md)

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

# **delete_release_profile**
> delete_release_profile(id)



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
    api_instance = readarr.ReleaseProfileApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_release_profile(id)
    except Exception as e:
        print("Exception when calling ReleaseProfileApi->delete_release_profile: %s\n" % e)
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

# **get_release_profile_by_id**
> ReleaseProfileResource get_release_profile_by_id(id)



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
    api_instance = readarr.ReleaseProfileApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_release_profile_by_id(id)
        print("The response of ReleaseProfileApi->get_release_profile_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleaseProfileApi->get_release_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReleaseProfileResource**](ReleaseProfileResource.md)

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

# **list_release_profile**
> List[ReleaseProfileResource] list_release_profile()



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
    api_instance = readarr.ReleaseProfileApi(api_client)

    try:
        api_response = api_instance.list_release_profile()
        print("The response of ReleaseProfileApi->list_release_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleaseProfileApi->list_release_profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ReleaseProfileResource]**](ReleaseProfileResource.md)

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

# **update_release_profile**
> ReleaseProfileResource update_release_profile(id, release_profile_resource=release_profile_resource)



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
    api_instance = readarr.ReleaseProfileApi(api_client)
    id = 'id_example' # str | 
    release_profile_resource = readarr.ReleaseProfileResource() # ReleaseProfileResource |  (optional)

    try:
        api_response = api_instance.update_release_profile(id, release_profile_resource=release_profile_resource)
        print("The response of ReleaseProfileApi->update_release_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleaseProfileApi->update_release_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **release_profile_resource** | [**ReleaseProfileResource**](ReleaseProfileResource.md)|  | [optional] 

### Return type

[**ReleaseProfileResource**](ReleaseProfileResource.md)

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

