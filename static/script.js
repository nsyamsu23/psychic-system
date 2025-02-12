function fetchNews() {
    fetch("/datafbnews")
        .then(response => response.json())
        .then(data => {
            const table = document.getElementById("news-table");
            table.innerHTML = ""; // Kosongkan tabel sebelum update

            data.forEach(news => {
                const row = document.createElement("tr");
                if (news.important === 1) row.classList.add("important");
                row.innerHTML = `
                    <td>${news.formatted_date}</td>   
                    <td>${news.newsTitle}</td>
                `;
                table.appendChild(row);
            });
        })
        .catch(error => console.error("Error fetching news:", error));
}

setInterval(fetchNews, 1000); // Update setiap 1 detik
