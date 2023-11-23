# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.88.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.file_report_dto import FileReportDto  # noqa: E501

class TestFileReportDto(unittest.TestCase):
    """FileReportDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileReportDto:
        """Test FileReportDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileReportDto`
        """
        model = FileReportDto()  # noqa: E501
        if include_optional:
            return FileReportDto(
                extras = [
                    ''
                    ],
                orphans = [
                    openapi_client.models.file_report_item_dto.FileReportItemDto(
                        checksum = '', 
                        entity_id = '', 
                        entity_type = 'asset', 
                        path_type = 'original', 
                        path_value = '', )
                    ]
            )
        else:
            return FileReportDto(
                extras = [
                    ''
                    ],
                orphans = [
                    openapi_client.models.file_report_item_dto.FileReportItemDto(
                        checksum = '', 
                        entity_id = '', 
                        entity_type = 'asset', 
                        path_type = 'original', 
                        path_value = '', )
                    ],
        )
        """

    def testFileReportDto(self):
        """Test FileReportDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
