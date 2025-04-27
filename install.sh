#!/bin/bash

set -e  # Terminar en el primer error

echo "🚀 Instalando dependencias necesarias..."
# (Este paso es opcional si el profesor ya tiene un entorno preparado)
pip install kivy pyinstaller

# Definir rutas
PROJECT_DIR="$(pwd)"
DIST_DIR="$PROJECT_DIR/dist/CalculadoraPensional"
ICON_PATH="$PROJECT_DIR/src/view/gui/icono_calculadora_pensional.png"  # 👈 Ajusta al nombre real

# 1. Limpiar builds anteriores
echo "🧹 Limpiando builds anteriores..."
rm -rf build dist *.spec

# 2. Ejecutar PyInstaller
echo "⚙️ Compilando la aplicación..."
pyinstaller --onefile --noconsole --name CalculadoraPensional --icon "$ICON_PATH" --add-data "src/view/gui/pension_gui.kv:." src/view/gui/main.py

# 3. Crear archivo .desktop
echo "🖥️ Creando lanzador de aplicación..."
cat > "$HOME/.local/share/applications/CalculadoraPensional.desktop" << EOL
[Desktop Entry]
Name=Calculadora Pensional
Exec=$DIST_DIR/CalculadoraPensional
Icon=$ICON_PATH
Terminal=false
Type=Application
Categories=Finance;Utility;
EOL

# 4. Dar permisos
chmod +x "$HOME/.local/share/applications/CalculadoraPensional.desktop"
chmod +x "$DIST_DIR/CalculadoraPensional"

# 5. Actualizar base de datos de aplicaciones
echo "🔄 Actualizando base de datos de aplicaciones..."
update-desktop-database ~/.local/share/applications/

echo "✅ Instalación completa. Puedes buscar 'Calculadora Pensional' en tu sistema."
