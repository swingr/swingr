#bin/sh
echo "What is the server address"
read ip

curl http://$ip/start/ > /dev/null
echo $ip > ip

number=1
quit="n"

while [ x"$quit" != x"y" ]
do
	if [ x"$quit" = x"n" ]; then
		python camera.py $ip
		echo "Do you wish to quit"
		read quit
	fi
	if [ x"$quit" = x"y" ]; then
		echo "What is your phone number"
		read number
		curl http://$ip/result/+1$number/
		exit
	fi
done
