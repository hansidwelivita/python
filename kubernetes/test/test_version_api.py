# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.11.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.version_api import VersionApi


class TestVersionApi(unittest.TestCase):
    """ VersionApi unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.version_api.VersionApi()

    def tearDown(self):
        pass

    def test_get_code(self):
        """
        Test case for get_code

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
