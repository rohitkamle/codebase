//To run cloudformation stack run below command
$ aws cloudformation create-stack --stack-name NewProdvpc --template-body file://vpc_advance.yaml

// to update the state run below command
$ aws cloudformation update-stack --stack-name NewProdvpc --template-body file://vpc_advance.yaml

//Run with Parameter file
$ aws cloudformation create-stack --stack-name NewProdvpc --template-body file://vpc_advance.yaml --parameters  file://vpc-adv-param.json


//get details for the stack 
$ aws cloudformation describe-stack --stack-name NewProdvpc

// list all stack and it status
$ aws cloudformation list-stacks

// delete stack
$ aws cloudformation delete-stack --stack-name NewProdvpc


aws cloudformation create-stack --stack-name NewProdvpc --template-body file://vpc_advance.yaml --parameters  file://vpc-adv-param.json