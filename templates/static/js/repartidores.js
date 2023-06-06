function AgregarRepartidor() {
    var formulario = document.querySelector('.AgregarRepartidor');
    if (formulario.style.display === 'none') {
        formulario.style.display = 'block';
    } else {
        formulario.style.display = 'none';
    }
}


document.addEventListener('DOMContentLoaded', function() {
    var vehiculos = document.getElementsByClassName('vehiculo');
    for (var i = 0; i < vehiculos.length; i++) {
        vehiculos[i].addEventListener('click', function() {
            var placa = this.getAttribute('data-placa');
            var modelo = this.getAttribute('data-modelo');
            
            // Crear el modal
            var modal = document.createElement('div');
            modal.className = 'modal fade';
            modal.innerHTML = `
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Información del vehículo</h5>
                            </button>
                        </div>
                        <div class="modal-body">
                            <p><strong>Placa:</strong> ${placa}</p>
                            <p><strong>Modelo:</strong> ${modelo}</p>
                        </div>
                    </div>
                </div>
            `;
            
            // Agregar el modal al documento
            document.body.appendChild(modal);
            
            // Mostrar el modal
            $(modal).modal('show');
            
            // Remover el modal del documento después de cerrarlo
            $(modal).on('hidden.bs.modal', function() {
                document.body.removeChild(modal);
            });
        });
    }
});

function mostrarOpciones() {
    var vehiculo = document.getElementById("vehiculo").value;
    var opcionesDiv = document.getElementById("opciones");

    if (vehiculo !== "") {
      opcionesDiv.style.display = "block";
    } else {
      opcionesDiv.style.display = "none";
    }
  }