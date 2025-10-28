#!/bin/bash

echo "🤖 Iniciando Presentación: Agentes Inteligentes y Resolución de Problemas"
echo "=========================================================================="
echo ""
echo "Verificando dependencias..."

# Verificar si streamlit está instalado
if ! command -v streamlit &> /dev/null; then
    echo "Instalando Streamlit..."
    pip install -q streamlit pandas
fi

echo "✓ Dependencias verificadas"
echo ""
echo "Iniciando aplicación Streamlit..."
echo "La aplicación se abrirá en: http://localhost:8501"
echo ""
echo "Presiona Ctrl+C para detener la aplicación"
echo ""

cd /home/ubuntu
streamlit run app.py
