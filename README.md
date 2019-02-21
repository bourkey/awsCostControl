# AWS Cost Control #

## github.com/bourkey ##

A Simple (set of) Script(s) to Shutdown Instances off a cron job setup in Cloud Watch

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
