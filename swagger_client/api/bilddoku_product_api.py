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


class BilddokuProductApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_bilddoku_product(self, bilddoku_product_id, **kwargs):  # noqa: E501
        """delete Bilddoku produkt  # noqa: E501

        delete Bilddoku product for a id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bilddoku_product(bilddoku_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bilddoku_product_id: ID of bilddoku (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_bilddoku_product_with_http_info(bilddoku_product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_bilddoku_product_with_http_info(bilddoku_product_id, **kwargs)  # noqa: E501
            return data

    def delete_bilddoku_product_with_http_info(self, bilddoku_product_id, **kwargs):  # noqa: E501
        """delete Bilddoku produkt  # noqa: E501

        delete Bilddoku product for a id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bilddoku_product_with_http_info(bilddoku_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bilddoku_product_id: ID of bilddoku (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bilddoku_product_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_bilddoku_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bilddoku_product_id' is set
        if ('bilddoku_product_id' not in params or
                params['bilddoku_product_id'] is None):
            raise ValueError("Missing the required parameter `bilddoku_product_id` when calling `delete_bilddoku_product`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bilddoku_product_id' in params:
            path_params['bilddoku_product_id'] = params['bilddoku_product_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/bilddoku/product/{bilddoku_product_id}', 'DELETE',
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

    def get_bilddoku_product(self, bilddoku_product_id, **kwargs):  # noqa: E501
        """add new product for a given bilddoku query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bilddoku_product(bilddoku_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bilddoku_product_id: ID of bilddoku (required)
        :return: ComponentsrequestBodiesBilddokuProduct
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bilddoku_product_with_http_info(bilddoku_product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bilddoku_product_with_http_info(bilddoku_product_id, **kwargs)  # noqa: E501
            return data

    def get_bilddoku_product_with_http_info(self, bilddoku_product_id, **kwargs):  # noqa: E501
        """add new product for a given bilddoku query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bilddoku_product_with_http_info(bilddoku_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bilddoku_product_id: ID of bilddoku (required)
        :return: ComponentsrequestBodiesBilddokuProduct
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bilddoku_product_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bilddoku_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bilddoku_product_id' is set
        if ('bilddoku_product_id' not in params or
                params['bilddoku_product_id'] is None):
            raise ValueError("Missing the required parameter `bilddoku_product_id` when calling `get_bilddoku_product`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bilddoku_product_id' in params:
            path_params['bilddoku_product_id'] = params['bilddoku_product_id']  # noqa: E501

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
            '/bilddoku/product/{bilddoku_product_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComponentsrequestBodiesBilddokuProduct',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_bilddoku_product(self, **kwargs):  # noqa: E501
        """add new product for a given bilddoku query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_bilddoku_product(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BilddokuProduct body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_bilddoku_product_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_bilddoku_product_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_bilddoku_product_with_http_info(self, **kwargs):  # noqa: E501
        """add new product for a given bilddoku query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_bilddoku_product_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BilddokuProduct body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_bilddoku_product" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/bilddoku/product/', 'POST',
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

    def put_bilddoku_product(self, bilddoku_product_id, **kwargs):  # noqa: E501
        """add new product for a given bilddoku query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_bilddoku_product(bilddoku_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bilddoku_product_id: ID of bilddoku (required)
        :param BilddokuProduct body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_bilddoku_product_with_http_info(bilddoku_product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.put_bilddoku_product_with_http_info(bilddoku_product_id, **kwargs)  # noqa: E501
            return data

    def put_bilddoku_product_with_http_info(self, bilddoku_product_id, **kwargs):  # noqa: E501
        """add new product for a given bilddoku query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_bilddoku_product_with_http_info(bilddoku_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bilddoku_product_id: ID of bilddoku (required)
        :param BilddokuProduct body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bilddoku_product_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_bilddoku_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bilddoku_product_id' is set
        if ('bilddoku_product_id' not in params or
                params['bilddoku_product_id'] is None):
            raise ValueError("Missing the required parameter `bilddoku_product_id` when calling `put_bilddoku_product`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bilddoku_product_id' in params:
            path_params['bilddoku_product_id'] = params['bilddoku_product_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/bilddoku/product/{bilddoku_product_id}', 'PUT',
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
