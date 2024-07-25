IP_ADDRESS=$(dig +short apiserver)
echo $IP_ADDRESS
while true; do echo "curl $IP_ADDRESS:5000/system_info" && curl $IP_ADDRESS:5000/system_info; sleep 1; done
