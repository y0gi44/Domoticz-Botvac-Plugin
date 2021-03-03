# Domoticz-Botvac-Plugin
 Domoticz Plugin for Botvac (Neato or vorwerk) Vacuum
 
 *This plugin uses the [pybotvac](https://github.com/stianaske/pybotvac) library 0.0.20 or later*

## How it works

Plugin provides: Status, Control and schedule status devices

**Status**: show current status in readable layout of switch. Status updates by polls 
(interval) and when you click Control device (for instant status change)

**Control**: for sending commands

**Schedule**: for enable or disbled sheduled cleans


## Installation

Before installation plugin check the `python3`, `python3-dev`, `pip3` is installed for Domoticz plugin system:
```
sudo apt-get update && sudo apt-get install python3 python3-dev pip3
```

Install Botvac plugin dependencies:
```
sudo pip3 install pybotvac urllib3 requests
```

Then go to plugins folder and clone repository:
```
cd domoticz/plugins
git clone https://github.com/y0gi44/Domoticz-Botvac-Plugin.git
```

**Only for Botvac D5 owners**

If you use persistent map for cleaning, please add this step so the cleaning will the map
*(Map is not detected by the pybotvac before Botvac D7 version)*
```
git checkout BotvacD5

```
**Only for vorwerk VR200/VR300 owners**

If you use persistent map for cleaning, please add this step so the cleaning will the map
*(Map is not detected by the pybotvac before Botvac D7 version)*
```
git checkout vorwerk
```

get your token_id 
launch script to get your id using One time password

```
python3 ./initOtpVorwerk.py

```
copy the Id_Token and paste it on the *password* field of the page of the domoticz plugin 


Restart the Domoticz service
```
sudo service domoticz restart
```

Now go to **Setup** -> **Hardware** in your Domoticz interface and add type with name **Botvac Vacuum**.

| Field | Information|
| ----- | ---------- |
| Neato email | Neato email account |
| Neato password | Neato password |
| Botvac vacuum name | The name of your Botvac vacuum |
| Debug | When set to true the plugin shows additional information in the Domoticz log |
| Update interval | In seconds, this determines with which interval the plugin polls the status of Vacuum. Minimun 10s. Default 60s   |

After clicking on the Add button the new devices are available in **Setup** -> **Devices**.

## How to update plugin
```
cd domoticz/plugins/Domoticz-Botvac-Plugin
git pull
```

Restart the Domoticz service
```
sudo service domoticz restart
```
## OPTIONAL: Update pybotvac
```
pip3 install --upgrade pybotvac
```
or update to selected version using:
```
pip3 install --upgrade pybotvac==0.0.20
```

## Screenshots
![](https://user-images.githubusercontent.com/4236800/80859999-1fb89f00-8c65-11ea-8b10-32316c23bfd2.png)


### Create a Neato account if not already done

Create a Neato account if not already done at [neatorobotics.com](https://neatorobotics.com/fr/my-neato-create-account/)
Then go to your [account](https://neatorobotics.com/fr/my-neato/)
or 
Use the Neato mobile app

## Custom Icons
You can add dedicated custom icons in Domoticz by loading icons.zip in Settings/Custom Icons/Add<br>
*INFO : I removed the automatic icons insertion due to a bug in Python Plugin in Domiticz which failed when plugin restart to create icons again causing error (seen in error logs)*
