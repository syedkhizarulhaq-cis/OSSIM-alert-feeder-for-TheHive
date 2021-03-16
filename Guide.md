The app.py should be put inside the root folder of OSSIM.

This python file can then be executed from with in the OSSIM when an alert is generated as following:

In OSSIM:
Go to Configuration -> Threat Intelligence -> Actions 

Now before adding the path to execute the file, install python3 on OSSIM using: 

apt-get install python3 

After installing python3, you would need to install theHive4py python library:

pip3 install theHive4py 

Now you can add the path to your app.py file in OSSIM as follow:

Thehive_OSSIM1![image](https://user-images.githubusercontent.com/33244888/111288973-80c34880-8666-11eb-8e69-157516ead5a7.png)

You can pass on whatever variables you may desire to your alert in TheHive, you should pass the variables which are meaningful for your IR team.

Thehive_OSSIM2![image](https://user-images.githubusercontent.com/33244888/111290499-08f61d80-8668-11eb-90c1-00d7d8117d2f.png)

Alert imported as a Case:

Thehive_OSSIM3![image](https://user-images.githubusercontent.com/33244888/111291005-8a4db000-8668-11eb-917b-f26d6d9ea895.png)
