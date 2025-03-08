document.addEventListener("DOMContentLoaded", function() {
    function fetchMetrics() {
        fetch("http://127.0.0.1:5000/metrics")
            .then(response => response.json())
            .then(data => {
                document.getElementById("cpu").textContent = `${data.cpu}%`;
                document.getElementById("ram").textContent = `${data.ram}%`;
                document.getElementById("disk").textContent = `${data.disk}%`;
                
                updateAlerts(data);
            })
            .catch(error => console.error("Error fetching metrics:", error));
    }

    function updateAlerts(data) {
        const alertList = document.getElementById("alert-list");
        alertList.innerHTML = ""; // Clear previous alerts

        if (data.cpu > 80) alertList.innerHTML += `<li class="alert-cpu">⚠️ High CPU usage: ${data.cpu}%</li>`;
        if (data.ram > 85) alertList.innerHTML += `<li class="alert-ram">⚠️ High RAM usage: ${data.ram}%</li>`;
        if (data.disk > 90) alertList.innerHTML += `<li class="alert-disk">⚠️ High Disk usage: ${data.disk}%</li>`;

        if (alertList.innerHTML === "") alertList.innerHTML = "<li>No alerts</li>";
    }

    setInterval(fetchMetrics, 5000); // Fetch every 5 seconds
});
