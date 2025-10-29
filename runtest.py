import pytest

# Lista de archivos de prueba a ejecutar
test_files = [
    "test/prueba_login.py",
    "test/test_inventory.py",
    "test/test_productos.py"
]

# Argumentos para ejecutar las pruebas: Archivos + REPORT HTML
pytest_args = test_files + ["--html=report.html", "--self-contained-html", "-v"]

pytest.main(pytest_args)