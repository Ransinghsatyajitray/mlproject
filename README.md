# End to End Machine Learning Project

# deployment to azure , creating webapp
1. signing to azure
2. create resourese
3. create webapp > subs / RG/ Web app name (app will be named webappnamewe havegiven.azurewebsites.net
4. publish - code
5.runtime - python 3.8
6. next
7. deployment - Github action settings - enable, github account , organization (usually github name), repo, branch main
8. review create
9. create (it takes couple of min)
10. automatically a .github/workflow folder will get created in github once the deployment is complete
11. if we see the file inside .github/workflow main_webappnamewehavegiven.yml file is created. 
It say name -> description
push -> the branch we are pushing from / where the code needs to be dispatched

job -> build -----
build -> run-on - ubuntu-latest server
steps -> it pushes the repo
python version -> 
run -> the virtual environment creation and activation (name <description>and run<terminal command>)
run -> installing dependencies
run -> uploading the artifact for deployment jobs, where the artifacts are going


job -> deploy -----
run-on - ubuntu-latest server
environemnt -> web app url we specified in azure, it is picking from secret key
steps to deploy

publish profile



in Github if we go to setting 
secrets and variables > actions > we see a secret variable has been created in github (this secret key accesses all the secrets mentioned in the yml file)

The github action actually creates the entire yml file. 

As soon as the yml file is created , we can see in github > actions all the build and deploy steps

build ---
1. set up job
2. run actions/checkout@v2 - it is syncing with which repo, it is seeing the app runner (it facilitate the automatically build is happending when the changes are happening), it is fetching the repo 
3. set up python version - 
4. create and start virtual environment
5. Install dependencies
6. upload artifacts for deployment jobs
7. post run actions/checkout@v2 (what ever cleanup is required after github repo is synced with the cloud)
8. complete job


the entire steps mentioned on the build is happening line by line


deployment ---


In github action we will see the url below the flowchart (under deploy)
once we click on the url we will be able to see the entire project


Once deployed and tested delete the webapp(as it may incur charges)



# Step By Step Production Grade Machine Learning Projects Deployment Azure Web App MLOPS

1. web app -> docker image -> private image 
2. docker image -> container registry (azure)
3. once we upload we can create image, this can be pulled once we create azure web app


azure > container registry -> create a new one
> subs , RG, Registry name, location
> review and create
> go to resource
> access key - admin user enable, copy the login server and keep it handy
, password, password2

> go to overview

Home > create resource > web app - sub, rg, name, publish - docker container
os - linux, region,   docker - option - single container, image source ACR, Registry, image - empty (we have to build it from our specific repo)

we need to have docker desktop

docker build -t urlofcontainerregistry.azurecr.io(we had saved it)/ourapplicationname:latest . <it will take some time>

docker login urlofcontainerregistry(we had saved it).azurecr.io, it will ask for username and password

docker push urlofcontainerregistry.azurecr.io(we had saved it)/ourapplicationname:latest  <the entire docker image is pushed to container registry>  it will take some min


We can see our image file in the acr

Create the web app
-------------------
subs, rg, name, publish -docker container
docker - single container, image cource acr, registry name, automatically image will be shown
create and validate
create
now when we go to the RG, we can see the web app
when the app is created, go to resource
go to deployment center -> we will get many option
keep continuous deployment to on
source - github action
organization, repo, branch
registry setting - registry source, subscription id, authentication - admin credentials, registry, image  -> save (saving container configuration)

in the github we will see .github/ workflows getting showed and github action is running

we will see the entire build and deployment pipeline is executed(we will get email too)


Build ->
1. setup job
2. run actions/checkout@v2
3. set up docker buildx
4. login to registry
5. build and push container image to registry
6. post build and push continaer image to registry
7. post login to registry
8. post set up docker buildx
9. post run actions/checkout@v2


deploy ->
1. setup job
2. deploy to azure web app
3. complete job (we will get the url) 2 min to load

















