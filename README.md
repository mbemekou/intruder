# intruder
simple  pythonic  fuzzer

intruder is a simple tool written in python to help you fuzz web pages

Author: Mbemekou Fred

Requirements: Python 2.7.x

Install apt-get -y install git python-pip

pip install Queue termcolor threading getopt requests re json argparse

git clone https://github.com/mbemekou/intruder.git

cd ./intruder

chmod +x intruder.py
 
        ./intruder.py [-h] -u <target url> -w <wordlist> [-t] <number of threads>
        
example:

./intruder.py -u http://127.0.0.1/^ATTACK^ -w /usr/share/wordlist/rockyou.txt -t 50

./intruder.py -u http://127.0.0.1/login.php?username=admin&password=^ATTACK^ -w rockyou.txt -t 50
