function toggleFormulario() {
    var formulario = document.querySelector('.formulario');
    if (formulario.style.display === 'none') {
        formulario.style.display = 'block';
    } else {
        formulario.style.display = 'none';
    }
}