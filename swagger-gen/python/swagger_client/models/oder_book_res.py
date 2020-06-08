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


class OderBookRes(object):
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
        'symbol': 'str',
        'price': 'str',
        'size': 'float',
        'side': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'price': 'price',
        'size': 'size',
        'side': 'side'
    }

    def __init__(self, symbol=None, price=None, size=None, side=None):  # noqa: E501
        """OderBookRes - a model defined in Swagger"""  # noqa: E501

        self._symbol = None
        self._price = None
        self._size = None
        self._side = None
        self.discriminator = None

        if symbol is not None:
            self.symbol = symbol
        if price is not None:
            self.price = price
        if size is not None:
            self.size = size
        if side is not None:
            self.side = side

    @property
    def symbol(self):
        """Gets the symbol of this OderBookRes.  # noqa: E501


        :return: The symbol of this OderBookRes.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this OderBookRes.


        :param symbol: The symbol of this OderBookRes.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def price(self):
        """Gets the price of this OderBookRes.  # noqa: E501


        :return: The price of this OderBookRes.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OderBookRes.


        :param price: The price of this OderBookRes.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def size(self):
        """Gets the size of this OderBookRes.  # noqa: E501


        :return: The size of this OderBookRes.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this OderBookRes.


        :param size: The size of this OderBookRes.  # noqa: E501
        :type: float
        """

        self._size = size

    @property
    def side(self):
        """Gets the side of this OderBookRes.  # noqa: E501


        :return: The side of this OderBookRes.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this OderBookRes.


        :param side: The side of this OderBookRes.  # noqa: E501
        :type: str
        """

        self._side = side

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
        if issubclass(OderBookRes, dict):
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
        if not isinstance(other, OderBookRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
