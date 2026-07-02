
function btn_abri() {
    
    const menuPrincipal = document.getElementById('pagina_inicial');
    const telaCadastro = document.getElementById('cadastro_atalhos');


    menuPrincipal.style.display = 'none';

    
    telaCadastro.style.display = 'block'; 
}

function btn_fechar() {
    const menuPrincipal = document.getElementById('pagina_inicial');
    const telaCadastro = document.getElementById('cadastro_atalhos');

    menuPrincipal.style.display = 'block'; 
    telaCadastro.style.display = 'none'; 
}