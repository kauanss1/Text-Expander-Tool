// ==========================================
// ESTADO GLOBAL
// ==========================================
let todosOsAtalhos = {};

// ==========================================
// GERENCIAMENTO DE MODAIS
// ==========================================
function abrirModal(idModal) {
    const modal = document.getElementById(idModal);
    const overlay = document.getElementById('overlay');
    if (modal) modal.style.display = 'block';
    if (overlay) overlay.style.display = 'block';
}

function fecharModal(idModal) {
    const modal = document.getElementById(idModal);
    const overlay = document.getElementById('overlay');
    if (modal) modal.style.display = 'none';
    if (overlay) overlay.style.display = 'none';
}

// Funções de atalho para os botões do HTML
const btn_abri = () => {
    abrirModal('cadastro_atalhos');
    atualizarSelectPastas();
};
const btn_fechar = () => fecharModal('cadastro_atalhos');
const confg_abri = () => abrirModal('configuracaoinicial');
const confg_fechar = () => fecharModal('configuracaoinicial');

// ==========================================
// RENDERIZAÇÃO E ATALHOS
// ==========================================
function exibirConteudo(gatilho, elementoClicado) {
    const blocoLaranja = document.querySelector('.bloco-laranja');
    if (!blocoLaranja) return;

    // Atualiza o texto na folha
    const texto = todosOsAtalhos[gatilho] || "(Texto do atalho vazio)";
    blocoLaranja.innerText = texto;

    // Atualiza o destaque visual
    document.querySelectorAll('.item-atalho').forEach(el => el.classList.remove('ativo'));
    if (elementoClicado) {
        elementoClicado.classList.add('ativo');
    }
}

async function carregarListaAtalhos() {
    try {
        const dadosArvore = await window.pywebview.api.carregarjs();
        const container = document.querySelector('.bloco-atalhos');
        if (!container) return;

        container.innerHTML = '';
        mapaConteudoAtalhos = {}; // Limpa o cache

        // Inicia a renderização a partir da pasta raiz
        renderizarEstrutura(dadosArvore, container);
    } catch (erro) {
        console.error("Erro ao carregar atalhos do backend:", erro);
    }
}

// Função recursiva para desenhar pastas e atalhos
function renderizarEstrutura(pastaAtual, elementoPai) {
    if (!pastaAtual) return;

    // 1. Cria a tag expansível para a pasta
    const detalhePasta = document.createElement('details');
    detalhePasta.className = 'pasta-container';
    detalhePasta.open = true; // Mantém aberta por padrão

    const tituloPasta = document.createElement('summary');
    tituloPasta.className = 'pasta-titulo';
    tituloPasta.textContent = `📁 ${pastaAtual.nome}`;
    detalhePasta.appendChild(tituloPasta);

    const corpoPasta = document.createElement('div');
    corpoPasta.className = 'pasta-filhos';

    // 2. Renderiza os atalhos desta pasta
    if (pastaAtual.atalhos && Array.isArray(pastaAtual.atalhos)) {
        pastaAtual.atalhos.forEach(atalho => {
            // Salva o conteúdo no mapa global usando o gatilho como chave
            mapaConteudoAtalhos[atalho.gatilho] = atalho.conteudo;

            const item = document.createElement('div');
            item.className = 'item-atalho';
            item.textContent = atalho.gatilho;
            item.onclick = () => exibirConteudo(atalho.gatilho, item);

            corpoPasta.appendChild(item);
        });
    }

    // 3. Renderiza as subpastas filhas recursivamente
    if (pastaAtual.pastas && Array.isArray(pastaAtual.pastas)) {
        pastaAtual.pastas.forEach(subpasta => {
            renderizarEstrutura(subpasta, corpoPasta);
        });
    }

    detalhePasta.appendChild(corpoPasta);
    elementoPai.appendChild(detalhePasta);
}

// Função para exibir o conteúdo no caderno e destacar o item ativo
function exibirConteudo(gatilho, elementoClicado) {
    const blocoCaderno = document.querySelector('.bloco-laranja');
    if (blocoCaderno) {
        blocoCaderno.innerText = mapaConteudoAtalhos[gatilho] || "";
    }

    // Gerencia o hover/seleção ativa
    document.querySelectorAll('.item-atalho').forEach(el => el.classList.remove('ativo'));
    if (elementoClicado) {
        elementoClicado.classList.add('ativo');
    }
}



function carregarOpcoesPastas(noPasta, selectElement, nivel = 0) {
    if (!noPasta) return;

    // 1. Cria a tag <option> para a pasta atual
    const option = document.createElement('option');
    option.value = noPasta.nome;
    
    // Adiciona traços para mostrar visualmente a hierarquia (ex: "— 📁 Subpasta")
    const prefixo = nivel > 0 ? '— '.repeat(nivel) : '';
    option.textContent = `${prefixo}📁 ${noPasta.nome}`;
    
    selectElement.appendChild(option);

    // 2. Percorre as subpastas filhas recursivamente
    if (noPasta.pastas && Array.isArray(noPasta.pastas)) {
        noPasta.pastas.forEach(subpasta => {
            carregarOpcoesPastas(subpasta, selectElement, nivel + 1);
        });
    }
}


async function atualizarSelectPastas() {
    const select = document.getElementById('seletor-pasta');
    
    // 1. Verifica se a tag <select id="seletor-pasta"> existe no HTML
    if (!select) {
        console.error("❌ ERRO: O elemento <select id='seletor-pasta'> não foi encontrado no HTML!");
        return;
    }

    try {
        // 2. Chama a API do Python
        const dadosArvore = await window.pywebview.api.carregarjs();
        console.log("📦 Dados recebidos do Python:", dadosArvore);

        // 3. Validação do formato
        if (!dadosArvore || typeof dadosArvore !== 'object') {
            console.error("❌ ERRO: Retorno inválido do backend.");
            return;
        }

        select.innerHTML = '';
        carregarOpcoesPastas(dadosArvore, select);
        console.log("✅ Pastas carregadas no select com sucesso!");

    } catch (erro) {
        console.error("❌ ERRO ao comunicar com o Python:", erro);
    }
}

function carregarOpcoesPastas(noPasta, selectElement, nivel = 0) {
    if (!noPasta || !noPasta.nome) return;

    const option = document.createElement('option');
    option.value = noPasta.nome;
    const prefixo = nivel > 0 ? '— '.repeat(nivel) : '';
    option.textContent = `${prefixo}📁 ${noPasta.nome}`;
    selectElement.appendChild(option);

    if (noPasta.pastas && Array.isArray(noPasta.pastas)) {
        noPasta.pastas.forEach(subpasta => {
            carregarOpcoesPastas(subpasta, selectElement, nivel + 1);
        });
    }
}

// ==========================================
// AÇÕES COM A API PYTHON
// ==========================================
async function adicionarNovoGatilho() {
    const inputGatilho = document.getElementById('campo-gatilho');
    const inputTexto = document.getElementById('texto-do-gatilho');
    const seletorPasta = document.getElementById('seletor-pasta');

    if (!inputGatilho || !inputTexto) return;

    const gatilho = inputGatilho.value.trim();
    const texto = inputTexto.value.trim();
    // Pega a pasta selecionada (ou define "gatilhos" como fallback padrão)
    const pastaAlvo = seletorPasta ? seletorPasta.value : "gatilhos";

    if (!gatilho || !texto) {
        alert("Por favor, preencha todos os campos!");
        return;
    }

    try {
        // Envia os 3 argumentos: gatilho, texto e a pasta escolhida
        const sucesso = await window.pywebview.api.salvargatilho(gatilho, texto, pastaAlvo);

        if (sucesso) {
            inputGatilho.value = '';
            inputTexto.value = '';
            btn_fechar();
            await carregarListaAtalhos();
        } else {
            alert("Erro do lado do servidor ao salvar o gatilho.");
        }
    } catch (erro) {
        console.error("Erro ao salvar o gatilho:", erro);
    }
}

async function dados_user() {
    const nome = document.getElementById('campo-nome')?.value.trim();
    const email = document.getElementById('campo-email')?.value.trim();
    const telefone = document.getElementById('campo-telefone')?.value.trim();

    if (!nome || !email || !telefone) {
        alert("Por favor, preencha o nome, o email e o telefone!");
        return;
    }

    try {
        const sucesso = await window.pywebview.api.salvar_dados_user(nome, email, telefone);

        if (sucesso) {
            fecharModal('configuracaoinicial');
        } else {
            alert("Erro ao salvar as informações.");
        }
    } catch (erro) {
        console.error("Erro ao salvar dados do usuário:", erro);
    }
}

// ==========================================
// INICIALIZAÇÃO
// ==========================================
window.addEventListener('DOMContentLoaded', () => {
    if (window.pywebview) {
        carregarListaAtalhos();
    } else {
        window.addEventListener('pywebviewready', carregarListaAtalhos);
    }
});





function toggleMenu() {
      const menu = document.getElementById('googleMenu');
      menu.classList.toggle('active');
    }

    // Fecha ao clicar fora do menu
    document.addEventListener('click', function(event) {
      const menu = document.getElementById('googleMenu');
      const btn = document.getElementById('profileBtn');
      if (menu && btn && !menu.contains(event.target) && !btn.contains(event.target)) {
        menu.classList.remove('active');
      }
    });