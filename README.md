Cloud DevOps Nanodegree Capstone Project

In this project I will apply the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These include:

    Working in AWS
    Using Circle CI to implement Continuous Integration and Continuous Deployment
    Building pipelines
    Working with CloudFormation to deploy clusters
    Building Kubernetes clusters
    Building Docker containers in pipelines

Project Overview

Step 1: Project Scope
    In this project, I am deploying a simple wordle game app(sourced from internet) in AWS EKS  

Step 2: Pick Deployment strategy & Tool 
    I have used Circle CI tool to perform Rolling Update deployment. 

Step 3: Setup Infrastructure 
    I have used CloudFormation to build infrastructure. As part of the cloudformation stack, I am creating a EKS cluster & deploying the app

Step 4: Build your pipeline
    the pipeline used for this project is tagged to GitHub repository link - https://github.com/kragavendra/udacity_capstone_project
    high level pipeline steps 
        install dependecies & lint -> build & upload docker image -> create EKS cluster -> perform rolling update

Step 5: Test your pipeline
    Perform builds on your pipeline.
    
    Verify that your pipeline works as you designed it. Take a screenshot of the Circle CI or Jenkins pipeline showing the deployment, and all stages passed successfully.
    
    Take a screenshot of your AWS EC2 page showing the newly created (for blue/green) or modified (for rolling) instances running as the EKS cluster nodes. Make sure you name your instances differently between blue and green deployments.

    Take a screenshot of the kubectl command output showing that the deployment is successful, pods are running, and the service can be accessed via an external IP or port forwarding.

    Take a screenshot showing that you can access the application after deployment.

