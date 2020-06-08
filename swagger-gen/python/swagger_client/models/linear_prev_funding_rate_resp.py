# coding: utf-8

"""
    Bybit API

    ## REST API for the Bybit Exchange. Base URI: [https://api.bybit.com]    # noqa: E501

    OpenAPI spec version: 0.2.6
    Contact: support@bybit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LinearPrevFundingRateResp(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'funding_rate': 'float',
        'funding_rate_timestamp': 'str',
        'symbol': 'str'
    }

    attribute_map = {
        'funding_rate': 'funding_rate',
        'funding_rate_timestamp': 'funding_rate_timestamp',
        'symbol': 'symbol'
    }

    def __init__(self, funding_rate=None, funding_rate_timestamp=None, symbol=None):  # noqa: E501
        """LinearPrevFundingRateResp - a model defined in Swagger"""  # noqa: E501

        self._funding_rate = None
        self._funding_rate_timestamp = None
        self._symbol = None
        self.discriminator = None

        if funding_rate is not None:
            self.funding_rate = funding_rate
        if funding_rate_timestamp is not None:
            self.funding_rate_timestamp = funding_rate_timestamp
        if symbol is not None:
            self.symbol = symbol

    @property
    def funding_rate(self):
        """Gets the funding_rate of this LinearPrevFundingRateResp.  # noqa: E501


        :return: The funding_rate of this LinearPrevFundingRateResp.  # noqa: E501
        :rtype: float
        """
        return self._funding_rate

    @funding_rate.setter
    def funding_rate(self, funding_rate):
        """Sets the funding_rate of this LinearPrevFundingRateResp.


        :param funding_rate: The funding_rate of this LinearPrevFundingRateResp.  # noqa: E501
        :type: float
        """

        self._funding_rate = funding_rate

    @property
    def funding_rate_timestamp(self):
        """Gets the funding_rate_timestamp of this LinearPrevFundingRateResp.  # noqa: E501


        :return: The funding_rate_timestamp of this LinearPrevFundingRateResp.  # noqa: E501
        :rtype: str
        """
        return self._funding_rate_timestamp

    @funding_rate_timestamp.setter
    def funding_rate_timestamp(self, funding_rate_timestamp):
        """Sets the funding_rate_timestamp of this LinearPrevFundingRateResp.


        :param funding_rate_timestamp: The funding_rate_timestamp of this LinearPrevFundingRateResp.  # noqa: E501
        :type: str
        """

        self._funding_rate_timestamp = funding_rate_timestamp

    @property
    def symbol(self):
        """Gets the symbol of this LinearPrevFundingRateResp.  # noqa: E501


        :return: The symbol of this LinearPrevFundingRateResp.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this LinearPrevFundingRateResp.


        :param symbol: The symbol of this LinearPrevFundingRateResp.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LinearPrevFundingRateResp, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LinearPrevFundingRateResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
