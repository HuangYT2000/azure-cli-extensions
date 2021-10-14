# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

from azure.cli.core.util import ScopedConfig


def create_init(cmd, resource_group_name, init_name, location=None, tags=None):
    raise CLIError('TODO: Implement `init create`')


def list_init(cmd, resource_group_name=None):
    raise CLIError('TODO: Implement `init list`')


def update_init(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance

def print_config_init(cmd):
    with ScopedConfig(cmd.cli_ctx.config, False):
        sections = cmd.cli_ctx.config.sections()
        for section in sections:
            items = cmd.cli_ctx.config.items(section)
            print('[',section,']')
            for item in items:
                print(item['name'],'=',item['value'])