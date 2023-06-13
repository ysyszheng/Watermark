su # run as superuser

iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ALLOW

iptables -A INPUT -p tcp --dport 443 -j ACCEPT
iptables -A INPUT -p tcp -s $1 --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

iptables -L