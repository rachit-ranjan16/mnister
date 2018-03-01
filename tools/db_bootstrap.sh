echo "----------------------------"
echo "Update and Upgrade"
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
echo "Install Mysql"
echo "----------------------------"
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password rootPass'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password rootPass'
sudo apt-get install -y -q mysql-server
sudo service mysql stop
echo "----------------------------"
echo "Configure Mysql for Remote Access"
echo "----------------------------"
echo "[mysqld]" >> /etc/mysql/my.cnf
echo "port = 3306" >> /etc/mysql/my.cnf
echo "bind-address = 0.0.0.0" >> /etc/mysql/my.cnf
echo "----------------------------"
echo "Start Mysql"
echo "----------------------------"
sudo service mysql start
echo "----------------------------"
echo "Configure User and Privileges"
echo "----------------------------"
mysql -uroot -prootPass < /vagrant_data/Config.sql
sudo updatedb
