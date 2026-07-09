function btn_abri() {
    const telaCadastro = document.getElementById('cadastro_atalhos');
    telaCadastro.style.display = 'block'; 
}

function btn_fechar() {
    const telaCadastro = document.getElementById('cadastro_atalhos');
    telaCadastro.style.display = 'none'; 
}







async function exibirGatilhosNaTela() {
    
    const blocoPreto = document.querySelector('.bloco-preto');
    if (!blocoPreto) return;
    
    
    blocoPreto.innerHTML = '';

    try {
       
        const meusGatilhosReais = await window.pywebview.api.carregarjs();

  
        if (!meusGatilhosReais || Object.keys(meusGatilhosReais).length === 0) {
            blocoPreto.innerHTML = '<span style="color: #666; padding: 15px; display: block;">Nenhum atalho cadastrado.</span>';
            return;
        }


        Object.keys(meusGatilhosReais).forEach(gatilho => {
            // Cria uma nova div na memória do navegador
            const itemAtalho = document.createElement('div');
            itemAtalho.className = 'item-atalho';
            itemAtalho.style.color = "white"; 
            

            itemAtalho.innerHTML = `<strong>${gatilho}</strong>`;
            

            blocoPreto.appendChild(itemAtalho);
        });

    } catch (erro) {
        console.error("Erro ao conectar com o Python:", erro);
        blocoPreto.innerHTML = '<span style="color: #ff4d4d; padding: 15px; display: block;">Erro ao carregar os atalhos.</span>';
    }
}


window.addEventListener('DOMContentLoaded', () => {
    
    setTimeout(exibirGatilhosNaTela, 1000);
});