# readarr.MetadataProfileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadata_profile**](MetadataProfileApi.md#create_metadata_profile) | **POST** /api/v1/metadataprofile | 
[**delete_metadata_profile**](MetadataProfileApi.md#delete_metadata_profile) | **DELETE** /api/v1/metadataprofile/{id} | 
[**get_metadata_profile_by_id**](MetadataProfileApi.md#get_metadata_profile_by_id) | **GET** /api/v1/metadataprofile/{id} | 
[**list_metadata_profile**](MetadataProfileApi.md#list_metadata_profile) | **GET** /api/v1/metadataprofile | 
[**update_metadata_profile**](MetadataProfileApi.md#update_metadata_profile) | **PUT** /api/v1/metadataprofile/{id} | 


# **create_metadata_profile**
> MetadataProfileResource create_metadata_profile(metadata_profile_resource=metadata_profile_resource)



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
    api_instance = readarr.MetadataProfileApi(api_client)
    metadata_profile_resource = readarr.MetadataProfileResource() # MetadataProfileResource |  (optional)

    try:
        api_response = api_instance.create_metadata_profile(metadata_profile_resource=metadata_profile_resource)
        print("The response of MetadataProfileApi->create_metadata_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataProfileApi->create_metadata_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_profile_resource** | [**MetadataProfileResource**](MetadataProfileResource.md)|  | [optional] 

### Return type

[**MetadataProfileResource**](MetadataProfileResource.md)

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

# **delete_metadata_profile**
> delete_metadata_profile(id)



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
    api_instance = readarr.MetadataProfileApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_metadata_profile(id)
    except Exception as e:
        print("Exception when calling MetadataProfileApi->delete_metadata_profile: %s\n" % e)
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

# **get_metadata_profile_by_id**
> MetadataProfileResource get_metadata_profile_by_id(id)



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
    api_instance = readarr.MetadataProfileApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_metadata_profile_by_id(id)
        print("The response of MetadataProfileApi->get_metadata_profile_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataProfileApi->get_metadata_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MetadataProfileResource**](MetadataProfileResource.md)

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

# **list_metadata_profile**
> List[MetadataProfileResource] list_metadata_profile()



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
    api_instance = readarr.MetadataProfileApi(api_client)

    try:
        api_response = api_instance.list_metadata_profile()
        print("The response of MetadataProfileApi->list_metadata_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataProfileApi->list_metadata_profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[MetadataProfileResource]**](MetadataProfileResource.md)

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

# **update_metadata_profile**
> MetadataProfileResource update_metadata_profile(id, metadata_profile_resource=metadata_profile_resource)



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
    api_instance = readarr.MetadataProfileApi(api_client)
    id = 'id_example' # str | 
    metadata_profile_resource = readarr.MetadataProfileResource() # MetadataProfileResource |  (optional)

    try:
        api_response = api_instance.update_metadata_profile(id, metadata_profile_resource=metadata_profile_resource)
        print("The response of MetadataProfileApi->update_metadata_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataProfileApi->update_metadata_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **metadata_profile_resource** | [**MetadataProfileResource**](MetadataProfileResource.md)|  | [optional] 

### Return type

[**MetadataProfileResource**](MetadataProfileResource.md)

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

