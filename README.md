[![CircleCI](https://dl.circleci.com/status-badge/img/gh/kragavendra/udacity_capstone_project/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/kragavendra/udacity_capstone_project/tree/main)

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
    I am using EKSCTL for creating EKS cluster(which is using cloud formation for creating the infrastructure) & deploying the app

Step 4: Build your pipeline
    the pipeline used for this project is tagged to GitHub repository link - https://github.com/kragavendra/udacity_capstone_project
    high level pipeline steps 
        install dependecies & lint -> build & upload docker image -> create EKS cluster -> perform rolling update

Step 5: Test your pipeline
    completed a working pipeline test and attached the screenshots
    
    access the wordle app from this link http://a9e8c28be83a546e7a13235d18d911e3-388845730.us-west-2.elb.amazonaws.com/
