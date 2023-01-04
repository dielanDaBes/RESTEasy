#! /bin/bash
yes | sudo apt-get update && yes | sudo apt-get upgrade
yes | sudo apt install git
git clone https://github.com/dielanDaBes/RESTEasy.git
yes | curl -fsSL test.docker.com -o get-docker.sh && yes | sh get-docker.sh
sudo usermod -aG docker ${USER}
yes | sudo curl -SL https://github.com/docker/compose/releases/download/v2.14.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo systemctl enable docker
sudo reboot now


