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

from openapi_client.models.search_asset_dto import SearchAssetDto  # noqa: E501

class TestSearchAssetDto(unittest.TestCase):
    """SearchAssetDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchAssetDto:
        """Test SearchAssetDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchAssetDto`
        """
        model = SearchAssetDto()  # noqa: E501
        if include_optional:
            return SearchAssetDto(
                search_term = ''
            )
        else:
            return SearchAssetDto(
                search_term = '',
        )
        """

    def testSearchAssetDto(self):
        """Test SearchAssetDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
