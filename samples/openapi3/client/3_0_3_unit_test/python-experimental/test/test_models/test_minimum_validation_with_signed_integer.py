# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.model.minimum_validation_with_signed_integer import MinimumValidationWithSignedInteger
from unit_test_api import configuration


class TestMinimumValidationWithSignedInteger(unittest.TestCase):
    """MinimumValidationWithSignedInteger unit test stubs"""
    _configuration = configuration.Configuration()

    def test_boundary_point_is_valid_passes(self):
        # boundary point is valid
        MinimumValidationWithSignedInteger._from_openapi_data(
            -2,
            _configuration=self._configuration
        )

    def test_positive_above_the_minimum_is_valid_passes(self):
        # positive above the minimum is valid
        MinimumValidationWithSignedInteger._from_openapi_data(
            0,
            _configuration=self._configuration
        )

    def test_int_below_the_minimum_is_invalid_fails(self):
        # int below the minimum is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            MinimumValidationWithSignedInteger._from_openapi_data(
                -3,
                _configuration=self._configuration
            )

    def test_float_below_the_minimum_is_invalid_fails(self):
        # float below the minimum is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            MinimumValidationWithSignedInteger._from_openapi_data(
                -2.0001,
                _configuration=self._configuration
            )

    def test_boundary_point_with_float_is_valid_passes(self):
        # boundary point with float is valid
        MinimumValidationWithSignedInteger._from_openapi_data(
            -2.0,
            _configuration=self._configuration
        )

    def test_negative_above_the_minimum_is_valid_passes(self):
        # negative above the minimum is valid
        MinimumValidationWithSignedInteger._from_openapi_data(
            -1,
            _configuration=self._configuration
        )

    def test_ignores_non_numbers_passes(self):
        # ignores non-numbers
        MinimumValidationWithSignedInteger._from_openapi_data(
            "x",
            _configuration=self._configuration
        )


if __name__ == '__main__':
    unittest.main()