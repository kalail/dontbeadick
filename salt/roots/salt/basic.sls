
packages:
    pkg.installed:
        - names:
            - build-essential
            - git
            - python
            - python-dev
            - python-pip
            - python-virtualenv


virtualenvwrapper:
    pip.installed:
        - require:
            - pkg: packages


/home/vagrant/.bashrc:
    file.append:
        - text:
            - source /usr/local/bin/virtualenvwrapper.sh
            - source /home/vagrant/env/bin/activate
