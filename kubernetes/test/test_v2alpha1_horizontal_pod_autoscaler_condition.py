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
from kubernetes.client.models.v2alpha1_horizontal_pod_autoscaler_condition import V2alpha1HorizontalPodAutoscalerCondition


class TestV2alpha1HorizontalPodAutoscalerCondition(unittest.TestCase):
    """ V2alpha1HorizontalPodAutoscalerCondition unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV2alpha1HorizontalPodAutoscalerCondition(self):
        """
        Test V2alpha1HorizontalPodAutoscalerCondition
        """
        model = kubernetes.client.models.v2alpha1_horizontal_pod_autoscaler_condition.V2alpha1HorizontalPodAutoscalerCondition()


if __name__ == '__main__':
    unittest.main()
