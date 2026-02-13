function askAI(){

    let q = document.getElementById("question").value;

    fetch("/assistant",{
        method:"POST",
        headers:{ "Content-Type":"application/json"},
        body:JSON.stringify({question:q})
    })
    .then(r=>r.json())
    .then(d=>{
        document.getElementById("reply").innerText=d.reply;
    });

}

async function analyzeUser() {

    let username = document.getElementById("username").value;

    let response = await fetch("/analyze", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username: username})
    });

    let data = await response.json();

    let strengthsDiv = document.getElementById("strengths");

    strengthsDiv.innerHTML = "<h3>Strengths</h3>";

    data.strengths.forEach(s => {
        strengthsDiv.innerHTML += `<p>✔ ${s}</p>`;
    });
}
