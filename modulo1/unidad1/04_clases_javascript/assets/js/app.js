console.log('Hola Mundo');

// 1. Métodos de Salidas
const ejecutarSalidas = () => {
    console.log('Mensaje desde consola.');
    alert('Alerta emergente.');
};

// 2. Variables y Tipos de Datos
const ejecutarVariables = () => {
    let edad = 25;

    console.log(edad);

    edad = 28;
    console.log(edad);

    const mensaje = 'El usuario tiene 28 años';
    console.log(mensaje);

    // Concatenar variables
    let suma = edad + 2;
    console.log(suma);

    let num = '2';
    console.log(num);

    suma = edad + num;
    console.log(suma);

    const mensaje2 = 'El usuario tiene ' + edad + ' años';
    console.log(mensaje2);

    let mensaje3 = `El usuario tiene ${edad} años`;
    console.log(mensaje3);
};

// 3. Operadores Aritméticos
const ejecutarAritmeticos = () => {
    let num1 = 15;
    let num2 = 4;

    let suma = num1 + num2;
    let resta = num1 - num2;
    let multi = num1 * num2;
    let divi = num1 / num2;

    let modulo = num1 % num2;

    console.log('--- Cálculos Aritméticos ---');
    console.log(`Suma: ${suma}`);
    console.log(`Resta: ${resta}`);
    console.log(`Multiplicación: ${multi}`);
    console.log(`División: ${divi}`);
    console.log(`Modulo: ${modulo}`);
};

// 4. Operadores de Comparación
const ejecutarComparacion = () => {
    const valorA = 10;
    const valorB = '10';

    // = -> asignación
    // == -> compara solo el valor, ignora el tipo de dato
    // === -> comparación estricta, si toma en cuenta el tipo de dato

    console.log('--- Evaluaciones Lógicas ---');
    console.log(`¿10 == '10'?: ${valorA == valorB}`);
    console.log(`¿10 === '10'?: ${valorA === valorB}`);
    console.log(`¿10 > 5?: ${valorA > 5}`);
    console.log(`¿10 >= 10?: ${valorA >= 10}`);
};

// 5. Entrada de Datos e Interacción con el DOM
const ejecutarInput = () => {
    let nombre = prompt('¿Cuál es tu nombre?', 'Ej: Juanito Pérez');
    let deporte = prompt('¿Cuál es tu deporte favorito', '');

    if (nombre && deporte) {
        document.write(`
            <div>
                <h1>Perfil Capturado</h1>
                <p><strong>Nombre:</strong> ${nombre}</p>
                <p><strong>Deporte:</strong> ${deporte}</p>
                <button onclick="location.reload()">Reiniciar Laboratorio</button>
            </div>    
        `);
    } else {
        alert('Falta completar datos.');
    }
};

// ---- Asignación de Eventos ----
const btnSalidas = document.querySelector('#btnSalidas');
btnSalidas.addEventListener('click', ejecutarSalidas);

const btnVariables = document.querySelector('#btnVariables');
btnVariables.addEventListener('click', ejecutarVariables);

const btnAritmeticos = document.querySelector('#btnAritmeticos');
btnAritmeticos.addEventListener('click', ejecutarAritmeticos);

const btnComparacion = document.querySelector('#btnComparacion');
btnComparacion.addEventListener('click', ejecutarComparacion);

const btnInput = document.querySelector('#btnInput');
btnInput.addEventListener('click', ejecutarInput);
