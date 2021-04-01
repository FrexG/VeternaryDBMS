window.onload = () =>{
  
    let addButton = document.getElementById("add");
    let rx_form = document.querySelectorAll('.rx-form');
    let total_form = document.querySelector('#id_form-TOTAL_FORMS');
    const form_container = document.querySelector('#prescription-group');

    let formNumber = rx_form.length - 1; // used for the prefix

      // listen for click
    addButton.onclick = () =>{
        
        // Clone the rx-form
        let newForm = rx_form[0].cloneNode(true);
        let formRegx = RegExp(`form-(\\d){1}-`,'g');

        formNumber ++;
        
       

        newForm.innerHTML = newForm.innerHTML.replace(formRegx,`form-${formNumber}-`);

       

        form_container.insertBefore(newForm,addButton);

        total_form.setAttribute("value",`${formNumber + 1}`);
        console.log(total_form.getAttribute("value"));
       



    };
    
}