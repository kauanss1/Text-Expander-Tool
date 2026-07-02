
function btn_abri() {
    
    const menuPrincipal = document.getElementById('pagina_inicial');
    const telaCadastro = document.getElementById('cadastro_atalhos');


    menuPrincipal.style.display = 'none';

    
    telaCadastro.style.display = 'flex'; 
}

function btn_fechar() {
    const menuPrincipal = document.getElementById('pagina_inicial');
    const telaCadastro = document.getElementById('cadastro_atalhos');

    menuPrincipal.style.display = 'flex'; 
    telaCadastro.style.display = 'none'; 
}