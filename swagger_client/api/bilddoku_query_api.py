# coding: utf-8

"""
    Bilddoku

    Part of the server to support Bilddoku client and plugin.   # noqa: E501

    OpenAPI spec version: 1.0.3
    Contact: nobody@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class BilddokuQueryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_bilddoku_query(self, body, bilddoku_query_id, **kwargs):  # noqa: E501
        """Add a new bilddoku query or update an existing one  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_bilddoku_query(body, bilddoku_query_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BilddokuQuery body: Bilddoku query object that needs to be added to the store (required)
        :param int bilddoku_query_id: ID of bilddoku (required)
        :return: BilddokuQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_bilddoku_query_with_http_info(body, bilddoku_query_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_bilddoku_query_with_http_info(body, bilddoku_query_id, **kwargs)  # noqa: E501
            return data

    def add_bilddoku_query_with_http_info(self, body, bilddoku_query_id, **kwargs):  # noqa: E501
        """Add a new bilddoku query or update an existing one  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_bilddoku_query_with_http_info(body, bilddoku_query_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BilddokuQuery body: Bilddoku query object that needs to be added to the store (required)
        :param int bilddoku_query_id: ID of bilddoku (required)
        :return: BilddokuQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'bilddoku_query_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_bilddoku_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_bilddoku_query`")  # noqa: E501
        # verify the required parameter 'bilddoku_query_id' is set
        if ('bilddoku_query_id' not in params or
                params['bilddoku_query_id'] is None):
            raise ValueError("Missing the required parameter `bilddoku_query_id` when calling `add_bilddoku_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bilddoku_query_id' in params:
            path_params['bilddoku_query_id'] = params['bilddoku_query_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/bilddoku/query/{bilddoku_query_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BilddokuQuery',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_bilddoku_by_point(self, bilddoku_query_id, **kwargs):  # noqa: E501
        """delete Bilddoku for given point  # noqa: E501

        delete Bilddoku for a given point  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bilddoku_by_point(bilddoku_query_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bilddoku_query_id: ID of point (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_bilddoku_by_point_with_http_info(bilddoku_query_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_bilddoku_by_point_with_http_info(bilddoku_query_id, **kwargs)  # noqa: E501
            return data

    def delete_bilddoku_by_point_with_http_info(self, bilddoku_query_id, **kwargs):  # noqa: E501
        """delete Bilddoku for given point  # noqa: E501

        delete Bilddoku for a given point  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bilddoku_by_point_with_http_info(bilddoku_query_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bilddoku_query_id: ID of point (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bilddoku_query_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_bilddoku_by_point" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bilddoku_query_id' is set
        if ('bilddoku_query_id' not in params or
                params['bilddoku_query_id'] is None):
            raise ValueError("Missing the required parameter `bilddoku_query_id` when calling `delete_bilddoku_by_point`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bilddoku_query_id' in params:
            path_params['bilddoku_query_id'] = params['bilddoku_query_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/bilddoku/query/{bilddoku_query_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bilddoku_by_point(self, bilddoku_query_id, **kwargs):  # noqa: E501
        """get Bilddoku for given point  # noqa: E501

        Get Bilddoku query if exists for a given point  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bilddoku_by_point(bilddoku_query_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bilddoku_query_id: ID of point (required)
        :return: BilddokuQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bilddoku_by_point_with_http_info(bilddoku_query_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bilddoku_by_point_with_http_info(bilddoku_query_id, **kwargs)  # noqa: E501
            return data

    def get_bilddoku_by_point_with_http_info(self, bilddoku_query_id, **kwargs):  # noqa: E501
        """get Bilddoku for given point  # noqa: E501

        Get Bilddoku query if exists for a given point  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bilddoku_by_point_with_http_info(bilddoku_query_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bilddoku_query_id: ID of point (required)
        :return: BilddokuQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bilddoku_query_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bilddoku_by_point" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bilddoku_query_id' is set
        if ('bilddoku_query_id' not in params or
                params['bilddoku_query_id'] is None):
            raise ValueError("Missing the required parameter `bilddoku_query_id` when calling `get_bilddoku_by_point`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bilddoku_query_id' in params:
            path_params['bilddoku_query_id'] = params['bilddoku_query_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/bilddoku/query/{bilddoku_query_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BilddokuQuery',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bilddoku_query_list(self, **kwargs):  # noqa: E501
        """Get next bilddoku_query_id  # noqa: E501

        Get bilddoku_query_id list for which a bilddoku has been queried and a product is not yet produced  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bilddoku_query_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bilddoku_query_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_bilddoku_query_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_bilddoku_query_list_with_http_info(self, **kwargs):  # noqa: E501
        """Get next bilddoku_query_id  # noqa: E501

        Get bilddoku_query_id list for which a bilddoku has been queried and a product is not yet produced  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bilddoku_query_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bilddoku_query_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/bilddoku/query/next', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
