#bin/sh
echo "What is the server address"
read ip

curl http://$ip/start > /dev/null
echo $ip > ip

number=1
quit="n"

while [ "quit" != "y" ]
do
	if [ "$quit" == "n" ]; then
		python camera.py $ip
		echo "Do you wish to quit"
		read quit
	fi
	if [ "$quit" == "y" ]; then
		echo "What is your phone number"
		read number
		curl http://$ip/result/+1$number/
		exit
	fi
done
