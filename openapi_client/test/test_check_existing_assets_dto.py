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

from openapi_client.models.check_existing_assets_dto import CheckExistingAssetsDto  # noqa: E501

class TestCheckExistingAssetsDto(unittest.TestCase):
    """CheckExistingAssetsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckExistingAssetsDto:
        """Test CheckExistingAssetsDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckExistingAssetsDto`
        """
        model = CheckExistingAssetsDto()  # noqa: E501
        if include_optional:
            return CheckExistingAssetsDto(
                device_asset_ids = [
                    ''
                    ],
                device_id = ''
            )
        else:
            return CheckExistingAssetsDto(
                device_asset_ids = [
                    ''
                    ],
                device_id = '',
        )
        """

    def testCheckExistingAssetsDto(self):
        """Test CheckExistingAssetsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
