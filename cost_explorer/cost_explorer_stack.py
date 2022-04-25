from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as lambda_,
    aws_iam as iam,
    aws_s3 as s3,
    aws_events as events,
    aws_events_targets as targets
    # aws_sqs as sqs,
)
from constructs import Construct
import os

class CostExplorerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        awsaccountnumber = os.environ['CDK_DEFAULT_ACCOUNT']
        region = os.environ['CDK_DEFAULT_REGION']

        cost_explorer_lambda_role = iam.Role(
            self,
            f"ce-role-{construct_id}",
            assumed_by = iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies = [
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

        cost_explorer_lambda_role.add_to_policy(
            iam.PolicyStatement(
                actions=[
                    "iam:ListAccountAliases",
                    "ce:GetCostAndUsage"
                    ],
                resources=['*'],
                sid='AllowCEPolicy'
            )
        )

        bucket = s3.Bucket.from_bucket_name(self, "BucketByName", "ciexchange")
        bucket.grant_read_write(cost_explorer_lambda_role)

        environmentvar = dict()
        environmentvar['LOG_LEVEL'] = '10'
        environmentvar['LOGGER_LEVEL_STRING'] = 'INFO'
        environmentvar['NUMBER_OF_ITEMS'] = '10'
        environmentvar['TEAMS_WEBHOOK_URL'] = 'string'
        environmentvar['BUCKET'] = 'ciexchange'

        cost_explorer_lambda = lambda_.Function(
            self,
            f"ce-lambda-{construct_id}",
            code=lambda_.InlineCode(code=' ').from_asset("./src"),
            description="Lambda to send Billing info",
            handler="ce_billing.report_cost",
            environment=environmentvar,
            timeout=Duration.seconds(120),
            runtime=lambda_.Runtime.PYTHON_3_9,
            retry_attempts=0,
            log_retention=None,
            role=cost_explorer_lambda_role
        )

        invoke_rule = events.Schedule.cron(hour='22', minute='0', month='*', year='*')

        lambda_target = targets.LambdaFunction(handler=cost_explorer_lambda)

        event = events.Rule(self, "InvokeRule", schedule=invoke_rule, targets=[lambda_target])