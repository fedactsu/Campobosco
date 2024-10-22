let currentFontSize = 16; // Tamaño inicial

function increaseFontSize() {
    currentFontSize += 2; // Incrementar tamaño en 2px
    let paragraphs = document.querySelectorAll("p");
    paragraphs.forEach(p => {
        p.style.fontSize = currentFontSize + "px";
    });
}

function decreaseFontSize() {
    if (currentFontSize > 10) { // Establece un tamaño mínimo para evitar que el texto sea demasiado pequeño
        currentFontSize -= 2; // Reducir tamaño en 2px
        let paragraphs = document.querySelectorAll("p");
        paragraphs.forEach(p => {
            p.style.fontSize = currentFontSize + "px";
        });
    }
}