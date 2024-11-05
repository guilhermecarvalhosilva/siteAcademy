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





document.getElementById('project-filter').addEventListener('change', function() {
    const selectedValue = this.value.toLowerCase();
    const rows = document.querySelectorAll('table tbody tr');

    rows.forEach(row => {
        const projectPhase = row.cells[7].textContent.toLowerCase(); // Obtém a fase do projeto

        // Mostra a linha se a fase do projeto corresponde ao valor selecionado
        if (selectedValue === 'todos' || projectPhase.includes(selectedValue)) {
            row.style.display = ''; // Exibe a linha
        } else {
            row.style.display = 'none'; // Oculta a linha
        }
    });
});