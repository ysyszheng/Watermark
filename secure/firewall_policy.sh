su # run as superuser

systemctl start firewalld # start firewall service

firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="local_ip_address" port protocol="tcp" port="443" accept' --permanent # port 443 only accept ip packages from local address
firewall-cmd --zone=public --add-service=https --permanent # allow https in port 80
firewall-cmd --zone=public --add-service=ssh --permanent # allow ssh in port 22
firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="any" port protocol="tcp" port="1:21,23:79,81:442,444:65535" reject' --permanent

firewall-cmd --reload # reload to make it work