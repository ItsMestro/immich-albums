# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.79.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.curated_objects_response_dto import CuratedObjectsResponseDto  # noqa: E501

class TestCuratedObjectsResponseDto(unittest.TestCase):
    """CuratedObjectsResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CuratedObjectsResponseDto:
        """Test CuratedObjectsResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CuratedObjectsResponseDto`
        """
        model = CuratedObjectsResponseDto()  # noqa: E501
        if include_optional:
            return CuratedObjectsResponseDto(
                device_asset_id = '',
                device_id = '',
                id = '',
                object = '',
                resize_path = ''
            )
        else:
            return CuratedObjectsResponseDto(
                device_asset_id = '',
                device_id = '',
                id = '',
                object = '',
                resize_path = '',
        )
        """

    def testCuratedObjectsResponseDto(self):
        """Test CuratedObjectsResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
