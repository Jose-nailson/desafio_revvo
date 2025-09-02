document.addEventListener('DOMContentLoaded', () => {
    // Seleciona o modal e os botões
    const modal = document.querySelector('.modal');
    const btnFechar = document.querySelector('.modal-btn-fechar');
    const btnInscrever = document.querySelector('.btn-modal');

    // Verifica se o usuário já visitou o site
    const jaVisitou = localStorage.getItem('jaVisitou');

    if (!jaVisitou) {
        // Se não visitou, exibe o modal
        modal.style.display = 'flex';
    }

    // Função para fechar o modal e salvar o estado no localStorage
    const fecharModal = () => {
        modal.style.display = 'none';
        localStorage.setItem('jaVisitou', 'true');
    };

    btnFechar.addEventListener('click', fecharModal);
    btnInscrever.addEventListener('click', fecharModal);
});