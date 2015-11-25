# GINI_Cloud

Automatic Creation of Tunnel:

git clone https://github.com/connorwstein/GINI_Cloud.git  
Make sure you have run chmod 400 GINI.pem  
Make sure that the yrouter executable has been built (i.e. make clean; make)
Make sure you have a GINI_HOME (doesnt matter where it points to) 
python AmazonCloudServer.py, should show serving on 8000
open a new terminal and then do python TestClient.py, will open up a shell ">>>"

\>>>get_running  // will use an already running instance

\>>>create //will create a new instance

\>>>ip 
52.123... // should print the ip of the instance to be used, if it prints "None", you need to either >>>create or >>>get_running

\>>>create_local_config //creates the local tunnel config script, run this before create_tunnel

\>>>create_cloud_config //creates the cloud tunnel config script, run this before create_tunnel

\>>>create_tunnel // should open up 2 xterm terminals, the router on the cloud and the router locally with the proper interfaces and route rules setup for the tunnel

\>>>killall // kills all instances
