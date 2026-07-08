function btn_abri() {
    const telaCadastro = document.getElementById('cadastro_atalhos');
    telaCadastro.style.display = 'block'; 
}

function btn_fechar() {
    const telaCadastro = document.getElementById('cadastro_atalhos');
    telaCadastro.style.display = 'none'; 
}


function exibirGatilhosNaTela() {
    // 1. Seleciona a sua div bloco-preto
    const blocoPreto = document.querySelector('.bloco-preto');
    
    // Limpa a div para não duplicar os itens caso a função rode mais de uma vez
    blocoPreto.innerHTML = '';

    // 2. Simulando uma lista de gatilhos (depois isso virá do seu JSON)
    const meusGatilhos = {
        ";nfe": "Nota Fiscal emitida com sucesso",
        ";obs": "Verificar observações no sistema",
        ";vlw": "Muito obrigado pela sua atenção!"
    };

    // 3. Passa por cada gatilho e adiciona dentro da div
    Object.keys(meusGatilhos).forEach(gatilho => {
        const textoExpandido = meusGatilhos[gatilho];

        // Cria a estrutura visual de cada linha de atalho
        const itemAtalho = document.createElement('div');
        itemAtalho.className = 'item-atalho'; // Classe para estilizar no CSS
        
        // Coloca o texto lá dentro
        itemAtalho.innerHTML = `<strong>${gatilho}</strong>`;

        // Coloca o novo item dentro da sua div bloco-preto
        blocoPreto.appendChild(itemAtalho);
    });
}

// Executa a função assim que o script carregar para você ver o resultado
exibirGatilhosNaTela();