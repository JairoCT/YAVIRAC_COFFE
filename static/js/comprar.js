    function comprar() {
      var usuarioRegistrado = true;
      if (usuarioRegistrado) {
        window.location.href = "http://localhost:5000/carrito";
      } else {
        mostrarModal();
      }
    }

    function mostrarModal() {
      var modal = document.getElementById('registroModal');
      modal.style.display = "block";
    }

    function cerrarModal() {
      var modal = document.getElementById('registroModal');
      modal.style.display = "none";
    }

    // Para cerrar el modal si el usuario hace clic fuera de él
    window.onclick = function(event) {
      var modal = document.getElementById('registroModal');
      if (event.target == modal) {
        modal.style.display = "none";
      }
    }