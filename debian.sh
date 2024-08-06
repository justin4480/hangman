setfont Lat15-Fixed15.psf.gz -d
sudo apt install xserver-xorg xinit
sudo apt install libpangocairo-1.0-0
sudo apt install python3-pip python3-xcffib python3-cairocffi
sudo apt install pipx vim git sddm alacritty
pipx install qtile
pipx ensurepath
sudo wget https://raw.githubusercontent.com/qtile/qtile/master/resources/qtile.desktop -P /usr/share/xsessions/