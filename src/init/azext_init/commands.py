# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azext_init._client_factory import cf_init


def load_command_table(self, _):

    # TODO: Add command type here
    # init_sdk = CliCommandType(
    #    operations_tmpl='<PATH>.operations#None.{}',
    #    client_factory=cf_init)


    with self.command_group('init') as g:
        g.custom_command('create', 'create_init')
        # g.command('delete', 'delete')
        g.custom_command('list', 'list_init')
        g.custom_command('print-config', 'print_config_init')
        # g.show_command('show', 'get')
        # g.generic_update_command('update', setter_name='update', custom_func_name='update_init')


    with self.command_group('init', is_preview=True):
        pass

