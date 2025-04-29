set -e  

echo "Instalando dependencias necesarias..."
pip install kivy pyinstaller

PROJECT_DIR="$(pwd)"
DIST_DIR="$PROJECT_DIR/dist/CalculadoraPensional"
ICON_PATH="$PROJECT_DIR/src/view/gui/icono_calculadora_pensional.png" 

echo "Limpiando builds..."
rm -rf build dist *.spec

echo "Compilando la aplicación..."
pyinstaller --onefile --noconsole --name CalculadoraPensional --icon "$ICON_PATH" --add-data "src/view/gui/pension_gui.kv:." src/view/gui/main.py

echo "Creando lanzador de aplicación..."
cat > "$HOME/.local/share/applications/CalculadoraPensional.desktop" << EOL
[Desktop Entry]
Name=Calculadora Pensional
Exec=$DIST_DIR/CalculadoraPensional
Icon=$ICON_PATH
Terminal=false
Type=Application
Categories=Finance;Utility;
EOL

chmod +x "$HOME/.local/share/applications/CalculadoraPensional.desktop"
chmod +x "$DIST_DIR/CalculadoraPensional"

echo "Actualizando base de datos de aplicaciones..."
update-desktop-database ~/.local/share/applications/

echo "Instalación completa. Puedes buscar 'Calculadora Pensional' en tu sistema."
