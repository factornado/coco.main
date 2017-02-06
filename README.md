# coco

Create, run and manage microservices with supervisor.

The goal is to orchestrate many services so that each service has it's own
threads an dependency stack.

We use [supervisor](http://supervisord.org) to monitor and control the running services.


## Requirements

You need to be on a unix-like system (to take advantage of bash scripts), and to have miniconda installed that way:

    wget http://bit.ly/miniconda -O miniconda.sh
    bash miniconda.sh -b -p $HOME/miniconda
    export PATH="$HOME/miniconda/bin:$PATH"
    conda update --yes --all


## Hello world

To create your first project, you need to clone the repository:

    git clone https://github.com/bibmartin/supernado
    cd supernado

Now create the conda *virtual* environment for supervisor:

    conda env create -f supervisor.yml

Create and install your first service:

    cp -R templates/python ./services/myservice
    ./services/myservice/make.sh

Run supervisor and your service:

    source activate supervisor
    supervisord
    supervisorctl start all

Your server should be running ; in typing `supervisorctl status`, you should get something like:

    > template_python                  RUNNING   pid 13135, uptime 0:00:07

You can test your service with:

    curl http://localhost:8001/foo/bar

    > Hello from service template_python. You've asked for uri foo/bar
