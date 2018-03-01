echo "----------------------------"
echo "Updating and Upgrading"
echo "----------------------------"
sudo apt-get -y -q update
#sudo apt-get upgrade
echo "----------------------------"
echo "Install and Configure Vim"
echo "----------------------------"
sudo apt-get install vim
sudo cp /vagrant_data/.vimrc /home/ubuntu
sudo cp /vagrant_data/.vimrc /root/
echo "----------------------------"
echo "Installing nginx"
echo "----------------------------"
sudo apt-get -y -q install nginx
echo "----------------------------"
sudo updatedb
