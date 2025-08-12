# Unihiker-Edge-Impulse
## How to connect Unihiker to Edge Impulse

### First Install npm using nvm
Run the following commands
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm ls-remote –lts
```
pick one out of the list
```
nvm install v22.18.0
```
Then set it as default:
```
nvm alias default v22.18.0
```
Fix broken/missing metadata in nvm (if you insist on using --lts)
```
cd ~/.nvm
git pull origin master
```
### Intall edge-impulse-linux
```
sudo apt update
curl -sL https://deb.nodesource.com/setup_20.x | sudo bash -
```
#### Update source list to point to debian archive
```
sudo nano /etc/apt/sources.list
```
Then replace everything in that file with the following:
```
deb http://archive.debian.org/debian buster main contrib non-free
deb-src http://archive.debian.org/debian buster main contrib non-free

```
 Force APT to accept old releases
 ```
sudo apt update -o Acquire::Check-Valid-Until=false
```
Now run the following commands
```
sudo apt update -o Acquire::ForceIPv4=true
sudo apt install -o Acquire::ForceIPv4=true -y gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
sudo npm install edge-impulse-linux -g --unsafe-perm
```

### Run edge-impulse-linux
```
edge-impulse-linux
```

mic and camera setup
