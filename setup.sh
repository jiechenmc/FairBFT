# Installing build tools
sudo apt-get install libssl-dev libuv1-dev cmake make

# Installing Ansible
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
