const formObj = document.querySelector('#formularioAvanzado');
const alertObj = document.querySelector('#alertaSistema');
const btnProc = document.querySelector('#btnProcesar');

formObj.addEventListener('submit', (e) => {
    e.preventDefault();

    console.log('btn formulario');
});
