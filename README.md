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

    git clone https://github.com/bibmartin/coco.main
    cd coco.mail

Now create the conda *virtual* environment for supervisor:

    conda env create -f supervisor.yml

Create and install your first service:

    ./templates/simpleServer/deploy.sh ./services/myservice myservice v1
    ./services/myservice/make.sh

You can edit the file `./services/myservice/config.yml` to tune the parameters.
In particular, you may need to change the port that the service will listen
to if `8801` is already used.

Run supervisor and your service:

    source activate supervisor
    supervisord
    supervisorctl start all

Your server should be running ; in typing `supervisorctl status`, you should get something like:

    > myservice-v1                  RUNNING   pid 13135, uptime 0:00:07

So you can test your service with:

    curl http://localhost:8801/foo/bar

    > Hello from service myservice. You've asked for uri foo/bar
