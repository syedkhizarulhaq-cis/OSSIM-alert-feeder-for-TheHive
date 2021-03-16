The app.py should be put inside the root folder of OSSIM.

This python file can then be executed from with in the OSSIM when an alert is generated as following:

In OSSIM:
Go to Configuration -> Threat Intelligence -> Actions 

Now before adding the path to execute the file, install python3 on OSSIM using: 

apt-get install python3 

After installing python3, you would need to install theHive4py python library:

pip3 install theHive4py 

Now you can add the path to your app.py file in OSSIM as follow:

Thehive_OSSIM1![image](https://user-images.githubusercontent.com/33244888/111287966-8f5d3000-8665-11eb-9386-7926ed2c55e0.png)
