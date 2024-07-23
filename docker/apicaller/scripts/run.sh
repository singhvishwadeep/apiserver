IP_ADDRESS=$(dig +short apiserver)
while true; do curl $IP_ADDRESS:5000/system_info; sleep 1; done
