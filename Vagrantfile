# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = '2'.freeze
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # config.vm.synced_folder "D:/Arquivos/devops/vagrant/djangoserver", "/home/vagrant/share", nfs:true

  config.vm.box = 'ubuntu/trusty64'
  config.vm.define :srvdjango01 do |srvdjango01_config|
    # config.vm.network :forwarded_port, guest: 3308, host: 3308
    srvdjango01_config.vm.hostname = 'srvdjango01'
    srvdjango01_config.vm.network :private_network,
                         ip: '192.168.10.10'
    # config.vm.provision :shell, path: "boot.sh"
  end
  config.vm.define :srvdjango02 do |srvdjango02_config|
    srvdjango02_config.vm.network :forwarded_port, guest: 8000, host: 8000
    srvdjango02_config.vm.hostname = 'srvdjango02'
    srvdjango02_config.vm.network :private_network,
                         ip: '192.168.10.20'
    # config.vm.provision :shell, path: "boot.sh"
  end 
  #############################################################################
  # MONGODB
  ############################################################################# 
  config.vm.define :srvmongodb01 do |srvmongodb01_config|
    srvmongodb01_config.vm.network :forwarded_port, guest: 27017, host: 27017
    srvmongodb01_config.vm.hostname = 'srvmongodb01'
    srvmongodb01_config.vm.network :private_network,
                         ip: '192.168.90.10'
    # config.vm.provision :shell, path: "boot.sh"
  end   
end