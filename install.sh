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
touch desinstalador.sh
echo  "
#!/bin/bash
sudo rm -rf /usr/bin/calculadora /usr/share/applications/calculadora.desktop /usr/share/calculadora
"> desinstalador.sh

sudo rm -rf install.sh instruciones.txt
