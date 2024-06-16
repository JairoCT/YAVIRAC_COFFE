function showSignIn() {
    document.getElementById('signInForm').style.display = 'block';
    document.getElementById('signUpForm').style.display = 'none';
}

function showSignUp() {
    document.getElementById('signInForm').style.display = 'none';
    document.getElementById('signUpForm').style.display = 'block';
}


async function loguear() {
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    fetch('/registro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            correo_electronico: email,
            contraseña: password
        })
    })
    .then(data => {
        if (data.redirected) {
            window.location.href = '/inicio_logeado'; // Redirigir si se recibe la URL de redirección
        } else {
            throw new Error('Usuario no encontrado')
        }
    })
    .catch(error => {
        console.error('Error al iniciar sesión:', error);
        alert('Hubo un problema al iniciar sesión. Por favor, inténtalo de nuevo más tarde.');
    });
}
