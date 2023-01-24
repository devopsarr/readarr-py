# readarr.AuthorEditorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_author_editor**](AuthorEditorApi.md#delete_author_editor) | **DELETE** /api/v1/author/editor | 
[**put_author_editor**](AuthorEditorApi.md#put_author_editor) | **PUT** /api/v1/author/editor | 


# **delete_author_editor**
> delete_author_editor(author_editor_resource=author_editor_resource)



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
    api_instance = readarr.AuthorEditorApi(api_client)
    author_editor_resource = readarr.AuthorEditorResource() # AuthorEditorResource |  (optional)

    try:
        api_instance.delete_author_editor(author_editor_resource=author_editor_resource)
    except Exception as e:
        print("Exception when calling AuthorEditorApi->delete_author_editor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_editor_resource** | [**AuthorEditorResource**](AuthorEditorResource.md)|  | [optional] 

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

# **put_author_editor**
> put_author_editor(author_editor_resource=author_editor_resource)



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
    api_instance = readarr.AuthorEditorApi(api_client)
    author_editor_resource = readarr.AuthorEditorResource() # AuthorEditorResource |  (optional)

    try:
        api_instance.put_author_editor(author_editor_resource=author_editor_resource)
    except Exception as e:
        print("Exception when calling AuthorEditorApi->put_author_editor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_editor_resource** | [**AuthorEditorResource**](AuthorEditorResource.md)|  | [optional] 

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

