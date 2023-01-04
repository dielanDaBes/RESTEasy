#! /bin/bash
printf '\n\n|| UPDATING PACKAGE MANAGER ||\n\n'
yes | sudo apt-get update && yes | sudo apt-get upgrade
printf '\n\n|| INSTALLING GIT ||\n\n'
yes | sudo apt install git
printf '\n\n|| CLONING REST EASY REPO ||\n\n'
git clone https://github.com/dielanDaBes/RESTEasy.git
printf '\n\n|| INSTALLING DOCKER ||\n\n'
yes | curl -fsSL test.docker.com -o get-docker.sh && yes | sh get-docker.sh
printf '\n\n|| ADDING CURRENT USER TO DOCKER GROUP ||\n\n'
sudo usermod -aG docker ${USER}
printf '\n\n|| INSTALLING DOCKER COMPOSE ||\n\n'
yes | sudo curl -SL https://github.com/docker/compose/releases/download/v2.14.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
printf '\n\n|| ALLOWING DOCKER TO RUN AT BOOT ||\n\n'
sudo systemctl enable docker
printf '\n\n|| REBOOTING - SSH CONNCETION CLOSED ||\n\n'
sudo reboot now


