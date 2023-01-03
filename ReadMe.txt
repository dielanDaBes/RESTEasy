https://www.raspberrypi.com/news/raspberry-pi-bullseye-update-april-2022/

https://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/

sudo apt-get update && sudo apt-get upgrade

curl -fsSL test.docker.com -o get-docker.sh && sh get-docker.sh

sudo usermod -aG docker ${USER}

curl -SL https://github.com/docker/compose/releases/download/v2.14.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose

sudo systemctl enable docker

echo 'deb http://httpredir.debian.org/debian buster-backports main contrib non-free' | sudo tee -a /etc/apt/sources.list.d/debian-backports.list

sudo apt update

sudo apt install libseccomp2 -t buster-backports

docker run hello-world