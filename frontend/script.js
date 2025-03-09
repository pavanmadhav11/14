async function generateFlowchart() {
    const code = document.getElementById("codeInput").value;

    const response = await fetch("http://127.0.0.1:8000/generate-flowchart/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: code })
    });

    const data = await response.json();
    if (response.ok) {
        renderFlowchart(data.flowchart);
    } else {
        alert("Error: " + data.detail);
    }
}

async function uploadPythonFile() {
    const fileInput = document.getElementById("fileInput");
    if (!fileInput.files.length) {
        alert("Please select a Python file.");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const response = await fetch("http://127.0.0.1:8000/upload/", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    if (response.ok) {
        renderFlowchart(data.flowchart);
    } else {
        alert("Error: " + data.detail);
    }
}

function renderFlowchart(flowchartData) {
    const chart = flowchart.parse(flowchartData);
    document.getElementById("canvas").innerHTML = "";
    chart.drawSVG("canvas");
}
