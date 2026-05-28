#! /bin/bash

#Dar permiso para que funcione
sudo chmod +x calculadora
#mover para inicial desde la terminal
sudo mv calculadora /usr/bin/
#
mkdir -p ~/.local/share/calculadora 
sudo mv calculadora.py ~/.local/share/calculadora/
#mover para que sarga en el menus de app intaladas
sudo mv calculadora.desktop /usr/share/applications
#
sudo mv calculadora.png /usr/share/pixmaps
touch desinstalador.sh
sudo chmod +x desinstalador.sh
echo  "#!/bin/bash
sudo rm -rf /usr/bin/calculadora /usr/share/applications/calculadora.desktop /usr/share/pixmaps/calculadora.png
sudo rm -rf ~/.local/share/calculadora desinstalador.sh ../calculadora
echo "Desintalado exitosamente.""> desinstalador.sh
sudo rm -rf install.sh instruciones.txt
echo "Instalado exitosamente."
