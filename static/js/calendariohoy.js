document.addEventListener('DOMContentLoaded', function() {
    const inputFecha = document.getElementById('calendariohoy');
    
    const fechaActual = calhoy();
    
    inputFecha.value = fechaActual;
});

function calhoy() {
        const today = new Date();
        const year = today.getFullYear();
        const month = String(today.getMonth() + 1).padStart(2, '0');
        const day = String(today.getDate()).padStart(2, '0');

        return `${year}-${month}-${day}`;
    }