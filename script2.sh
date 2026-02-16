#!/bin/bash
# Install cowsay
sudo apt-get update && sudo apt-get install cowsay -y

# Generate ASCII art
/usr/games/cowsay -f dragon "Run for Cover, I am a Dragon .... RaWR" > dragon.txt

# Display content
cat dragon.txt

# Check for keyword
grep -i "dragon" dragon.txt