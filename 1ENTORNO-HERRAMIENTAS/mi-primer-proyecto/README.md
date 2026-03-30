## Excepciones a PEP 8 en este proyecto

1. **Línea máxima de 120 caracteres**: Preferimos 120 en lugar de 79 para mejor legibilidad en código científico.
   - Configurado en `pyproject.toml` con:
     ```toml
     [tool.black]
     line-length = 120
     ```