#!/usr/bin/env bash
# This code write by Mr.nope
if [[ "$(id -u)" -ne 0 ]]; then
  echo ""
  echo "Please, Usage: sudo bash install.sh !"
  echo ""
  exit 1
fi
clear
echo "Installing..."
sleep 2
chmod +x clone.py
apt install python
apt install python3
apt install python3-pip
pip3 install --upgrade pip
echo ""
echo "Installing..., Finish...!"
echo ""
exit 1