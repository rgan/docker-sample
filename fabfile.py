from fabric.api import *
from jinja2 import Template

def generate_from_template(output_file_name, template_file_name, config):
    with open(output_file_name, "w") as output_file:
        with open(template_file_name) as template_file:
            output_file.write(Template(template_file.read()).render(config=config))

def configure():
    config = {"server_name" : "testapp", "app_root" : "/var/testapp",
              "greeting" : "Hello!", "site_name" : "testapp" }
    generate_from_template("config.php", "config.php.tmpl", config)
    generate_from_template(config["site_name"], "apache.vhost.tmpl", config)
    generate_from_template("Dockerfile", "Dockerfile.tmpl", config)

@task
def deploy():
    configure()
    local("tar -czf app.tar.gz www composer.json config.php")
    local("sudo docker build -t test_app .")
    local("rm app.tar.gz")
    local("sudo docker run -p 80:80 -d test_app")
    #local("sudo docker run -p 80:80 -t -i test_app /bin/bash")

