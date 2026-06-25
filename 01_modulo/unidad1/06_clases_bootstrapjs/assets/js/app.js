const initComponents = () => {
    console.log('Inicializando componentes...');

    const listadoTooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    [...listadoTooltips].forEach((tooltipElement) => new bootstrap.Tooltip(tooltipElement));

    const listadoPopovers = document.querySelectorAll('[data-bs-toggle="popover"]');
    [...listadoPopovers].forEach((popoverElement) => new bootstrap.Popover(popoverElement));
};

document.addEventListener('DOMContentLoaded', initComponents);
