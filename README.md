# gh_pipeline_test
Just a test of github pipelines

Build docker image:
`docker build - < Dockerfile -t pipeline_test_di`

Create container from image 
`docker run -d --name pipeline_test_cntn pipeline_test_di`

Start container
`docker start pipeline_test_cntn`