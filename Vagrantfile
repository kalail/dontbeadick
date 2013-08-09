Vagrant.configure("2") do |config|
    # Make box
    config.vm.box = "precise64"
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    # Sync app folders
    config.vm.synced_folder "dontbeadick/", "/home/vagrant/dontbeadick/"
    # Ports
    config.vm.network :forwarded_port, guest: 80, host: 8000
    # Config management
    config.vm.synced_folder "salt/roots/", "/srv/"
    config.vm.provision :salt do |salt|
      salt.minion_config = "salt/minion.conf"
      salt.verbose = true
      salt.run_highstate = true
    end
end