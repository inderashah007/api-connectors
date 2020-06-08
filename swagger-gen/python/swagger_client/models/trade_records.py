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

from swagger_client.models.trade_records_info import TradeRecordsInfo  # noqa: F401,E501


class TradeRecords(object):
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
        'order_id': 'str',
        'trade_list': 'list[TradeRecordsInfo]'
    }

    attribute_map = {
        'order_id': 'order_id',
        'trade_list': 'trade_list'
    }

    def __init__(self, order_id=None, trade_list=None):  # noqa: E501
        """TradeRecords - a model defined in Swagger"""  # noqa: E501

        self._order_id = None
        self._trade_list = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if trade_list is not None:
            self.trade_list = trade_list

    @property
    def order_id(self):
        """Gets the order_id of this TradeRecords.  # noqa: E501


        :return: The order_id of this TradeRecords.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this TradeRecords.


        :param order_id: The order_id of this TradeRecords.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def trade_list(self):
        """Gets the trade_list of this TradeRecords.  # noqa: E501


        :return: The trade_list of this TradeRecords.  # noqa: E501
        :rtype: list[TradeRecordsInfo]
        """
        return self._trade_list

    @trade_list.setter
    def trade_list(self, trade_list):
        """Sets the trade_list of this TradeRecords.


        :param trade_list: The trade_list of this TradeRecords.  # noqa: E501
        :type: list[TradeRecordsInfo]
        """

        self._trade_list = trade_list

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
        if issubclass(TradeRecords, dict):
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
        if not isinstance(other, TradeRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
