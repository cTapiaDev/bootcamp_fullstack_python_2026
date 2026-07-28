pool_preguntas = {
    'basicas': {
        'pregunta_1': {
            'enunciado': '¿Qué etiqueta HTML semántica se utiliza para definir el contenido principal y único de un documento?',
            'alternativas': [
                ['<main>', 1],
                ['<section>', 0],
                ['<header>', 0],
                ['<div>', 0]
            ]
        },
        'pregunta_2': {
            'enunciado': 'En diseño UI, ¿qué significa el acrónimo "UX"?',
            'alternativas': [
                ['User Experience (Experiencia de Usuario)', 1],
                ['User Interface (Interfaz de Usuario)', 0],
                ['Universal Execution (Ejecución Universal)', 0],
                ['Unified X-axis (Eje X Unificado)', 0]
            ]
        },
        'pregunta_3': {
            'enunciado': '¿Cuál es la forma correcta de enlazar una hoja de estilos externa en HTML?',
            'alternativas': [
                ['<link rel="stylesheet" href="style.css">', 1],
                ['<style src="style.css">', 0],
                ['<css link="style.css">', 0],
                ['<script href="style.css">', 0]
            ]
        }
    },
    'intermedias': {
        'pregunta_1': {
            'enunciado': '¿Qué propiedad CSS se utiliza para convertir un contenedor en un Flexbox?',
            'alternativas': [
                ['display: flex;', 1],
                ['align-items: flex;', 0],
                ['position: flexbox;', 0],
                ['float: flex;', 0]
            ]
        },
        'pregunta_2': {
            'enunciado': 'En la metodología BEM para nombrar clases CSS, ¿qué representan los guiones bajos dobles (__)?',
            'alternativas': [
                ['Un Elemento que forma parte de un Bloque', 1],
                ['Un Modificador de estado', 0],
                ['Una variable global', 0],
                ['Un estilo de texto inline', 0]
            ]
        },
        'pregunta_3': {
            'enunciado': '¿Cuál es la unidad de medida en CSS que es relativa al tamaño de fuente del elemento raíz (html)?',
            'alternativas': [
                ['rem', 1],
                ['em', 0],
                ['vh', 0],
                ['px', 0]
            ]
        }
    },
    'avanzadas': {
        'pregunta_1': {
            'enunciado': 'En JavaScript Moderno (ES6+), ¿cuál es la diferencia principal entre let y var?',
            'alternativas': [
                ['let tiene scope de bloque, var tiene scope de función', 1],
                ['var permite constantes, let no', 0],
                ['let solo acepta números, var acepta strings', 0],
                ['No hay diferencia, son alias del mismo comando', 0]
            ]
        },
        'pregunta_2': {
            'enunciado': '¿Qué devuelve el método Array.prototype.map() en JavaScript?',
            'alternativas': [
                ['Un nuevo arreglo con los resultados de la función callback', 1],
                ['El mismo arreglo modificado (in-place)', 0],
                ['Un único valor booleano', 0],
                ['El número de elementos iterados', 0]
            ]
        },
        'pregunta_3': {
            'enunciado': 'Al realizar una petición asíncrona con fetch(), ¿qué devuelve inicialmente la función?',
            'alternativas': [
                ['Una Promesa (Promise)', 1],
                ['Un objeto JSON', 0],
                ['Un string de texto', 0],
                ['Un callback', 0]
            ]
        }
    }
}