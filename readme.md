# 2.I. Exportación e importación de bases de datos (25%)
## Objetivo

Comprender el proceso de exportación e importación de datos en bases de datos no relacionales.

## Modalidad

Por equipos

## Desarrollo

Desarrollar aplicación que almacene información en una base de datos no relacional, de al menos tres colecciones diferentes.

Generar archivo de exportación de la base de datos.

## Entregables

- URL de repositorio GIT, con aplicación y archivos de la base de datos

- Reporte de práctica.

## Integrantes
- Armando Elías Aguirre Sosa 1112150023
- Efraín Fernando Bejarano Puentes 1119150056
- Emmanuel Campuzano Contreras 1119150081
- Rosa Alejandra Legarda Bencomo 1119150016

## Información extra
- Grupo: IDGS81N
- Materia: ADMINISTRACIÓN DE BASES DE DATOS
- Docente: M.S.I. ALFONSO JOSÉ BARROSO BARAJAS

## End Points
<hr />

### New Blog

> #### Type: **POST**
>`Path: "/blog"`<br>

**REQUIREMENTS**
- JSON
```json
{
	"title" : "{THE ADDRESS}",
    "text": "{THE TEXT BODY}"
}
```

### Get All Blogs
> #### **GET**
>`Path: "/blog"`<br>

<hr />


### New Note
> #### **POST**
>`Path: "/note"`<br>

**REQUIREMENTS**
- JSON
```json
{
    "text": "{THE TEXT BODY}"
}
```

### Get All Notes
> #### **GET**
>`Path: "/note"`<br>

<hr />

### New Task
> #### **POST**
>`Path: "/task"`<br>

**REQUIREMENTS**
- JSON
```json
{
    "task": "{THE TASK DESCRIPTION}"
}
```


### Get All Tasks
> #### **GET**
>`Path: "/task"`<br>