$(() => {
    console.log('Entorno de jQuery inicializado.');

    // 1. Selectores

    $('#btnModificarPrecios').on('click', () => {
        $('.vacaciones .valor').text('$100.000').css({
            color: '#15803d',
            'font-weight': 'bold',
            'font-size': '1.2rem',
        });

        $('.vacaciones').css('background-color', '#fef08a');
    });

    $('#btnMarcarLinks').on('click', () => {
        $('[href]').css('border-bottom', '3px solid #ef4444').css('text-decoration', 'none');
    });

    // 2. Efectos

    $('#btnFade').on('click', () => {
        $('#cajaAnimada').fadeToggle(800); // Cambio automático entre fadeIn y fadeOut
    });

    $('#btnSlide').on('click', () => {
        $('#cajaAnimada').slideToggle(800);
    });

    // 3. Delegación de Eventos

    let contadorTareas = 1;

    $('#btnAgregarTarea').on('click', () => {
        // contadorTareas = contadorTareas + 1;
        contadorTareas++;
        $('#contenedorTareas').append(`
                <div class="tarea" style="display: none;">
                    <span>Nueva Tarea Dinámica #${contadorTareas}</span>
                    <button class="btn-eliminar">X</button>
                </div>
            `);

        $('.tarea').last().fadeIn(400);
    });

    $('#contenedorTareas').on('click', '.btn-eliminar', (e) => {
        const nodoPadre = $(e.currentTarget).parent();
        nodoPadre.slideUp(300, () => {
            nodoPadre.remove();
        });
    });

    // 4. Formulario

    $('#formularioRegistro').on('submit', (event) => {
        event.preventDefault();

        const nombreIngresado = $('#inputNombre').val();
        const rolSeleccionado = $('#inputRol').val();

        $('input[type="text"]').val('');

        $('#resultadoFormulario')
            .html(
                `<strong>¡Registro exitoso!</strong> <br> Usuario: ${nombreIngresado} <br> Área: ${rolSeleccionado.toUpperCase()}`,
            )
            .slideDown(400);

        setTimeout(() => {
            $('#resultadoFormulario').slideUp(400);
        }, 4000);
    });
});
