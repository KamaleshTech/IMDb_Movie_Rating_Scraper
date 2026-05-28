fetch('../movies.csv')
    .then(response => response.text())
    .then(data => {

        let rows = data.split('\n');
        let tableBody = document.querySelector('#movieTable tbody');

        for (let i = 1; i < rows.length; i++) {

            let cols = rows[i].split(',');

            if (cols.length >= 4) {

                let row = `
                    <tr>
                        <td>${cols[0]}</td>
                        <td>${cols[1]}</td>
                        <td>${cols[2]}</td>
                        <td>${cols[3]}</td>
                    </tr>
                `;

                tableBody.innerHTML += row;
            }
        }
    });
    document.getElementById("searchBox").addEventListener("keyup", function () {

    let filter = this.value.toLowerCase();
    let rows = document.querySelectorAll("#movieTable tbody tr");

    rows.forEach(function (row) {

        let movieName = row.cells[1].textContent.toLowerCase();

        if (movieName.includes(filter)) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
});