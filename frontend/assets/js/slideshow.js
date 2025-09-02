const slides = document.querySelectorAll('.slide');
const pontos = document.querySelectorAll('.ponto');

// Botões de navegação - O seletor precisa do ponto "."
const btnAnterior = document.querySelector('.btn-anterior-slide');
const btnProximo = document.querySelector('.btn-proximo-slide');

let slideAtual = 0;

function mudarSlide(n){
    for(let i = 0; i < slides.length; i++){
        slides[i].style.display = 'none';
        pontos[i].classList.remove('ativo');
    }
    
    // Corrigindo a lógica de loop
    if (n >= slides.length) {
        slideAtual = 0;
    } else if (n < 0) {
        slideAtual = slides.length - 1;
    } else {
        slideAtual = n;
    }
    
    slides[slideAtual].style.display = 'block';
    pontos[slideAtual].classList.add('ativo');
}

btnAnterior.addEventListener('click',() => {
    mudarSlide(slideAtual - 1)
});

// Botão de avanço deve somar 1, não subtrair
btnProximo.addEventListener('click', () => {
    mudarSlide(slideAtual + 1);
});

pontos.forEach((ponto, index) => {
    ponto.addEventListener('click',() => {
        mudarSlide(index);
    });
});

mudarSlide(slideAtual);