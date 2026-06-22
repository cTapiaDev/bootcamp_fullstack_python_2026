const solicitarNota = (materia, numero) => {
    const entrada = prompt(`Ingrese la Nota ${numero} de ${materia}`);
    return parseFloat(entrada?.replace(',', '.') || '0'); // Si tiene decimales, tomalos en cuenta, y si no existe valor, agrega un 0
};

const html1 = document.querySelector('#HTML1');
const html2 = document.querySelector('#HTML2');
const html3 = document.querySelector('#HTML3');
const htmlPromedio = document.querySelector('#HTMLPromedio');

const nota1HTML = solicitarNota('HTML', 1);
const nota2HTML = solicitarNota('HTML', 2);
const nota3HTML = solicitarNota('HTML', 3);

html1.textContent = nota1HTML;
html2.textContent = nota2HTML;
html3.textContent = nota3HTML;
htmlPromedio.textContent = ((nota1HTML + nota2HTML + nota3HTML) / 3).toFixed(2);
