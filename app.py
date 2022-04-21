#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import Tags

from cost_explorer.cost_explorer_stack import CostExplorerStack


app = cdk.App()

Environment=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))

CostExplorerStack(app, "CostExplorerStack", env=Environment)

Tags.of(app).add('Account', 'Personal')

app.synth()
