# AWS Cost Control #

## github.com/bourkey ##

A Simple (set of) Script(s) to alter Instance state based on a CloudWatch Event Rule

Look for an AWS Tag, check if the instance is in the correct state, and take action.

### Installation ###

* IAM Permissions
  * Create Policy with permissions (awsPolicy.json)
    * logs:CreateLogGroup
    * logs:CreateLogStream
    * logs:PutLogEvents
    * ec2:DescribeInstances
    * ec2:DescribeTags
    * ec2:StartInstances
    * ec2:StopInstances
    * Restrict ARNs as Required
  * Create Role
    * Trusted Entites: Lambda
    * Attach Above policy
* Create Lambda
  * Name Function
  * Runtime : Python 3.6 (Also Tested in Python 2.6)
  * Select Above Role
  * Paste In Script
  * Edit Region
  * Handler: lambda_function.lambda_handler
  * Add CloudWatch Event
    * Create Rule
    * Schedule: Cron expression
    * Example : 0 8 ? * * *
    * Enable Trigger

