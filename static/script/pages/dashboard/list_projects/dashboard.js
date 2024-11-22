const projectSearchInput = document.getElementById('project-search');
const tableRows = document.querySelectorAll('#container table tbody tr');

// Adiciona o evento de entrada para capturar o valor digitado
projectSearchInput.addEventListener('input', (event) => {
    const searchValue = event.target.value.toLowerCase(); // Valor digitado no input (em minúsculas)
    console.log('Valor atual do input:', searchValue);

    // Filtra os projetos com base no valor do input
    tableRows.forEach(row => {
        const projectName = row.cells[1].textContent.toLowerCase(); // Obtém o nome do projeto na linha
        if (projectName.includes(searchValue)) {
            row.style.display = ''; // Mostra a linha
        } else {
            row.style.display = 'none'; // Esconde a linha
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    // Seleciona o botão de toggler e o menu lateral
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbar = document.querySelector('.navbar');

    if (navbarToggler && navbar) {
        // Adiciona um evento de clique ao botão
        navbarToggler.addEventListener('click', () => {
            navbar.classList.toggle('active'); // Alterna a classe 'active' no menu lateral
        });
    } else {
        console.error('Navbar toggler ou navbar não foram encontrados no DOM.');
    }
});

// Seleciona o dropdown e as linhas da tabela
const projectFilter = document.getElementById('project-filter');

// Adiciona o evento 'change' ao dropdown
projectFilter.addEventListener('change', (event) => {
    const filterValue = event.target.value; // Obtém o valor selecionado
    console.log('Filtro selecionado:', filterValue);

    // Filtra as linhas da tabela
    tableRows.forEach(row => {
        const status = row.cells[8].textContent.trim(); // Obtém o texto do status na linha
        if (filterValue === "todos" || status === filterValue) {
            row.style.display = ''; // Mostra a linha
        } else {
            row.style.display = 'none'; // Esconde a linha
        }
    });
});


