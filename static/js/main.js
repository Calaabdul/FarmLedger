
const searchInput = document.getElementById("produce-search");
const tableBody = document.getElementById("produce-table-body");
const searchStatus = document.getElementById("search-status");

const previousButton = document.getElementById("previous-page");
const nextButton = document.getElementById("next-page");
const pageInfo = document.getElementById("page-info");

if (searchInput && tableBody) {

    let nextUrl = null;
    let previousUrl = null;
    let currentPage = 1;
    let totalRecords = 0;

    // Retrieve a page of records from the API
    function loadRecords(url = "/api/produce/") {

        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error("Could not retrieve produce records.");
                }

                return response.json();
            })
            .then(data => {

                nextUrl = data.next;
                previousUrl = data.previous;
                totalRecords = data.count;

                displayRecords(data.results);

                nextButton.disabled = !nextUrl;
                previousButton.disabled = !previousUrl;

                pageInfo.textContent =
                    `Page ${currentPage} | ${totalRecords} records`;

                searchStatus.textContent = "";
            })
            .catch(error => {
                searchStatus.textContent = error.message;
            });
    }

    // Display records in the table
    function displayRecords(records) {

        tableBody.replaceChildren();

        if (records.length === 0) {
            const row = document.createElement("tr");
            const cell = document.createElement("td");

            cell.colSpan = 6;
            cell.textContent = "No produce records found.";
            cell.className = "text-center text-muted";

            row.appendChild(cell);
            tableBody.appendChild(row);
            return;
        }

        records.forEach(record => {

            const row = document.createElement("tr");

            const values = [
                record.name,
                record.category_name || "—",
                record.quantity,
                record.unit,
                record.price_per_unit || "—"
            ];

            values.forEach(value => {
                const cell = document.createElement("td");
                cell.textContent = value;
                row.appendChild(cell);
            });

            const actionCell = document.createElement("td");
            actionCell.textContent = "Use the Edit/Delete links above for changes.";
            row.appendChild(actionCell);

            tableBody.appendChild(row);
        });
    }

    // Move to the next page
    nextButton.addEventListener("click", function () {
        if (nextUrl) {
            currentPage++;
            loadRecords(nextUrl);
        }
    });

    // Move to the previous page
    previousButton.addEventListener("click", function () {
        if (previousUrl) {
            currentPage--;
            loadRecords(previousUrl);
        }
    });

    // Load the first page
    loadRecords();
}
