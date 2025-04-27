[app]
title = Calculadora Pensional
package.name = calculadorapensional
package.domain = org.calculadora
source.dir = .  # Raíz del proyecto
source.include_patterns = src/**/*.py, src/**/*.kv  
version = 1.0
requirements = 
    python3==3.9.18,
    kivy==2.3.0,
    openssl==3.1.2,
    setuptools==68.2.2
orientation = portrait
android.api = 34
android.ndk = 25b
android.archs = arm64-v8a
android.minapi = 24  # Android 7.0+
p4a.branch = develop

# Especificar el punto de entrada correcto
[android:entrypoint]
main = src/view/gui/main.py  # Ruta al nuevo main.py

[buildozer]
log_level = 2