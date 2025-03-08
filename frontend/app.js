document.getElementById("fetchData").addEventListener("click", () => {
    fetch("http://127.0.0.1:5000/process", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ key1: "value1", key2: "value2" })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = JSON.stringify(data);
    })
    .catch(error => console.error("Error:", error));
});

document.getElementById("sendAlert").addEventListener("click", () => {
    fetch("http://127.0.0.1:5000/send-alert")
    .then(response => response.json())
    .then(data => {
        alert(data.alert);
    })
    .catch(error => console.error("Error:", error));
});
