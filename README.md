Deploy a simple Php application created using the [Slim Framework](http://www.slimframework.com/)
to a docker container using [Fabric](http://www.fabfile.org/).
```
sudo apt-get install python-dev python-pip
sudo pip install virtualenv
virtualenv --prompt="(dockersample)" env
source env/bin/activate
pip install -r requirements.txt
```