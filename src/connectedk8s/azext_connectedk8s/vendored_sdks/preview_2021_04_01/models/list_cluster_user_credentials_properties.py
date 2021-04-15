# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ListClusterUserCredentialsProperties(Model):
    """ListClusterUserCredentialsProperties.

    All required parameters must be populated in order to send to Azure.

    :param authentication_method: Required. The mode of client authentication.
     Possible values include: 'Token', 'AAD'
    :type authentication_method: str or
     ~azure.mgmt.hybridkubernetes.models.AuthenticationMethod
    :param client_proxy: Required. Boolean value to indicate whether the
     request is for client side proxy or not
    :type client_proxy: bool
    """

    _validation = {
        'authentication_method': {'required': True},
        'client_proxy': {'required': True},
    }

    _attribute_map = {
        'authentication_method': {'key': 'authenticationMethod', 'type': 'str'},
        'client_proxy': {'key': 'clientProxy', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ListClusterUserCredentialsProperties, self).__init__(**kwargs)
        self.authentication_method = kwargs.get('authentication_method', None)
        self.client_proxy = kwargs.get('client_proxy', None)