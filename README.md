# hugin
Project to learn CI/CD and docker.

Project target:
- automated testing on pull request to prod branch.
- if tests are a success automaticaly deploy to prod and update running image.


V1 flow:
- upload the code to dev branch from the dev machine, do a pull request to prod.
- clone the prod branch to a ubuntu server
- create and upload the docker image to docker hub
- pull down the new image on the prod server.

no automated testing, all manual deployment.

