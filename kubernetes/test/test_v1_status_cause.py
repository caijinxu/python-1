# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_status_cause import V1StatusCause


class TestV1StatusCause(unittest.TestCase):
    """ V1StatusCause unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1StatusCause(self):
        """
        Test V1StatusCause
        """
        model = kubernetes.client.models.v1_status_cause.V1StatusCause()


if __name__ == '__main__':
    unittest.main()
