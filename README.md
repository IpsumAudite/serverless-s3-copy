# Using the Serverless Framework
## About
The serverless framework will take an easy to read yaml file and convert it into a cloud formation stack.
## Common Commands
### Install
`npm install -g serverless`
### Setup
Run the `serverless` command and follow the prompts.
### Initialize a new directory
`sls init {dir}`
(`sls` is shorthand for the `serverless` command)
### Update
`npm update -g serverless`
### Deploy
`sls deploy`
## Troubleshooting
#### Common Problems
1. Stack won't delete
   1. `sls` creates a bucket in which it stores the yaml and the functions and the cloudformation stack will not be able to delete this bucket while there are files in it. Find the bucket and delete the files, then try to delete the stack again.
2. Bucket already exists error
   1. See in the yaml where there is a `existing` property set to `true` - `sls` will try to create a new bucket with the name you have given it and this will cause an error if a bucket with that name already exists. If you would like to deploy a trigger or something else to an existing bucket, you need to set the `existing` property.
3. 
