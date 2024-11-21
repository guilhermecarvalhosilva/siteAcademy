//elements
console.log("teste2"); 

const btnToggler = window.document.querySelector(".navbar-toggler"); 
const inputSearch = window.document.querySelector(".navbar-search"); 
const navbar = window.document.querySelector(".navbar");

//events
btnToggler.addEventListener('click', () => {
    navbar.classList.toggle('active'); 
});

inputSearch.addEventListener('click', () => {
    if(!navbar.classList.contains("active")) {
        navbar.classList.add('active'); 
    }
});
  // Barra de Pesquisa 
document.getElementById('project-search').addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();
    const rows = document.querySelectorAll('table tbody tr');

    rows.forEach(row => {
        const projectName = row.cells[1].textContent.toLowerCase(); // Obtém o nome do projeto

        // Mostra a linha se o nome do projeto contém o termo de pesquisa
        if (projectName.includes(searchTerm)) {
            row.style.display = ''; // Exibe a linha
        } else {
            row.style.display = 'none'; // Oculta a linha
        }
    });
});

