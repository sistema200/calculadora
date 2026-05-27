#! /bin/bash

#Dar permiso para que funcione
sudo chmod +x calculadora
#mover para inicial desde la terminal
sudo mv calculadora /usr/bin/
#mover para que sarga en el menus de app intaladas
sudo mv calculadora.desktop /usr/share/applications
#
sudo mkdir -p /usr/share/calculadora
sudo mv calculadora.png /usr/share/calculadora/
sudo rm -rf install.sh instruciones.txt
