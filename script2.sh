#!/bin/bash
sudo apt-get update
sudo apt-get install cowsay -y
cowsay -f dragon "Run for Cover, I am a Dragon .... RaWR" > $GITHUB_WORKSPACE/dragon.txt
cat $GITHUB_WORKSPACE/dragon.txt
grep -i "dragon" $GITHUB_WORKSPACE/dragon.txt