
# Welcome to Cost Explorer CDK Python project!

This is a project for Python development with CDK.  The project contains python code that sends daily breakdown of costs to teams or slack channels, you may also choose to write it to s3.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

## Environment Variables

The webhook url, logging info, bucket, etc are added as environment variable, if you want any of these modified head over to cost_explorer_stack.py cdkstack which contains the cdk construct for all the resources used to set this up.  Update the varaibles and you should be good to go!

To add tags to your resources, go to app.py and for app level tags you can use, Tags.of(app).add('Account', 'Personal').  For resource level, go to the cost_explorer_stack.py where you can add the tags for the resource you're interested in.

Credits: https://github.com/iandees/aws-billing-to-slack

[![cost-notifications.png](https://i.postimg.cc/X7ff2NyY/cost-notifications.png)](https://postimg.cc/3dw0NTBs)