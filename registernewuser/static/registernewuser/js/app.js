window.onload = () =>{
    console.log("JS Working!!!");

    let addButton = document.getElementById('add');
    let prescription = document.getElementById('prescription-group');

    addButton.onclick = () => {
        let span = document.getElementById("id_rx");

        prescription.appendChild(span);
    };
}