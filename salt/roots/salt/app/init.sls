include:
- basic


/home/vagrant/env:
    virtualenv.managed:
        - runas: vagrant
        - requirements: salt://app/requirements.txt
        - require:
            - pkg: packages
