# readarr.MetadataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadata**](MetadataApi.md#create_metadata) | **POST** /api/v1/metadata | 
[**create_metadata_action_by_name**](MetadataApi.md#create_metadata_action_by_name) | **POST** /api/v1/metadata/action/{name} | 
[**delete_metadata**](MetadataApi.md#delete_metadata) | **DELETE** /api/v1/metadata/{id} | 
[**get_metadata_by_id**](MetadataApi.md#get_metadata_by_id) | **GET** /api/v1/metadata/{id} | 
[**list_metadata**](MetadataApi.md#list_metadata) | **GET** /api/v1/metadata | 
[**list_metadata_schema**](MetadataApi.md#list_metadata_schema) | **GET** /api/v1/metadata/schema | 
[**test_metadata**](MetadataApi.md#test_metadata) | **POST** /api/v1/metadata/test | 
[**testall_metadata**](MetadataApi.md#testall_metadata) | **POST** /api/v1/metadata/testall | 
[**update_metadata**](MetadataApi.md#update_metadata) | **PUT** /api/v1/metadata/{id} | 


# **create_metadata**
> MetadataResource create_metadata(metadata_resource=metadata_resource)



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
    api_instance = readarr.MetadataApi(api_client)
    metadata_resource = readarr.MetadataResource() # MetadataResource |  (optional)

    try:
        api_response = api_instance.create_metadata(metadata_resource=metadata_resource)
        print("The response of MetadataApi->create_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->create_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_resource** | [**MetadataResource**](MetadataResource.md)|  | [optional] 

### Return type

[**MetadataResource**](MetadataResource.md)

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

# **create_metadata_action_by_name**
> create_metadata_action_by_name(name, metadata_resource=metadata_resource)



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
    api_instance = readarr.MetadataApi(api_client)
    name = 'name_example' # str | 
    metadata_resource = readarr.MetadataResource() # MetadataResource |  (optional)

    try:
        api_instance.create_metadata_action_by_name(name, metadata_resource=metadata_resource)
    except Exception as e:
        print("Exception when calling MetadataApi->create_metadata_action_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **metadata_resource** | [**MetadataResource**](MetadataResource.md)|  | [optional] 

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

# **delete_metadata**
> delete_metadata(id)



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
    api_instance = readarr.MetadataApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_metadata(id)
    except Exception as e:
        print("Exception when calling MetadataApi->delete_metadata: %s\n" % e)
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

# **get_metadata_by_id**
> MetadataResource get_metadata_by_id(id)



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
    api_instance = readarr.MetadataApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_metadata_by_id(id)
        print("The response of MetadataApi->get_metadata_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_metadata_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MetadataResource**](MetadataResource.md)

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

# **list_metadata**
> List[MetadataResource] list_metadata()



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
    api_instance = readarr.MetadataApi(api_client)

    try:
        api_response = api_instance.list_metadata()
        print("The response of MetadataApi->list_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->list_metadata: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[MetadataResource]**](MetadataResource.md)

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

# **list_metadata_schema**
> List[MetadataResource] list_metadata_schema()



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
    api_instance = readarr.MetadataApi(api_client)

    try:
        api_response = api_instance.list_metadata_schema()
        print("The response of MetadataApi->list_metadata_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->list_metadata_schema: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[MetadataResource]**](MetadataResource.md)

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

# **test_metadata**
> test_metadata(metadata_resource=metadata_resource)



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
    api_instance = readarr.MetadataApi(api_client)
    metadata_resource = readarr.MetadataResource() # MetadataResource |  (optional)

    try:
        api_instance.test_metadata(metadata_resource=metadata_resource)
    except Exception as e:
        print("Exception when calling MetadataApi->test_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_resource** | [**MetadataResource**](MetadataResource.md)|  | [optional] 

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

# **testall_metadata**
> testall_metadata()



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
    api_instance = readarr.MetadataApi(api_client)

    try:
        api_instance.testall_metadata()
    except Exception as e:
        print("Exception when calling MetadataApi->testall_metadata: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **update_metadata**
> MetadataResource update_metadata(id, metadata_resource=metadata_resource)



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
    api_instance = readarr.MetadataApi(api_client)
    id = 'id_example' # str | 
    metadata_resource = readarr.MetadataResource() # MetadataResource |  (optional)

    try:
        api_response = api_instance.update_metadata(id, metadata_resource=metadata_resource)
        print("The response of MetadataApi->update_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->update_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **metadata_resource** | [**MetadataResource**](MetadataResource.md)|  | [optional] 

### Return type

[**MetadataResource**](MetadataResource.md)

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

