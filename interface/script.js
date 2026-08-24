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
const btn_abri = () => abrirModal('cadastro_atalhos');
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
        todosOsAtalhos = await window.pywebview.api.carregarjs();
        const container = document.querySelector('.bloco-atalhos');
        if (!container) return;

        container.innerHTML = '';

        Object.entries(todosOsAtalhos).forEach(([gatilho]) => {
            const item = document.createElement('div');
            item.className = 'item-atalho';
            item.textContent = gatilho;
            item.onclick = () => exibirConteudo(gatilho, item);
            container.appendChild(item);
        });
    } catch (erro) {
        console.error("Erro ao carregar atalhos do backend:", erro);
    }
}

// ==========================================
// AÇÕES COM A API PYTHON
// ==========================================
async function adicionarNovoGatilho() {
    const inputGatilho = document.getElementById('campo-gatilho');
    const inputTexto = document.getElementById('texto-do-gatilho');

    if (!inputGatilho || !inputTexto) return;

    const gatilho = inputGatilho.value.trim();
    const texto = inputTexto.value.trim();

    if (!gatilho || !texto) {
        alert("Por favor, preencha todos os campos!");
        return;
    }

    try {
        const sucesso = await window.pywebview.api.salvargatilho(gatilho, texto);

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