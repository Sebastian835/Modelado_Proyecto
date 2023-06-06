function AgregarCliente() {
    var formulario = document.querySelector('.AgregarCliente');
    if (formulario.style.display === 'none') {
        formulario.style.display = 'block';
    } else {
        formulario.style.display = 'none';
    }
}

function EliminarCliente() {
    var formulario = document.querySelector('.EliminarCliente');
    if (formulario.style.display === 'none') {
        formulario.style.display = 'block';
    } else {
        formulario.style.display = 'none';
    }
}