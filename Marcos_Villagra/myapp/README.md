# Este es mi proyecto en Django

Este proyecto consiste en una aplicacion web en Django utilizando el patron MVT.

## Funcionalidades

- busqueda de libros en la base de datos
- Tres modelos: Autor, Libro y Editoria
- Formulario para la busqueda.

## instalacion

1) clonar el repositorio:
    '''sh
    git clone [URL_DEL_REPOSITORIO]
    cd mi_proyecto
    '''
2) instalar las dependencias
    '''sh
    pip install - r requirements.txt
    '''
3) crear y aplicar migraciones:
    '''sh
    python manage.py makemigrations
    python manage.py migrate

4) ejecutar el servidor:
    '''sh
    python manage.py runserver
    '''

## contribuir

para contribuir seguir estos pasos:
1) fork este repositorio
2) crea una rama con la nueva funcionalidad: get checkout -b nueva-funcionalidad.
3) realiza los cambios y haz un commit: 
git commit -m 'agrega nueva funcionalidad'
4) realiza un push a la rama: git push origin nueva-funcionalidad
5) Envia un pull request

#autor

[Marcos villagra]