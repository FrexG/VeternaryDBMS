window.onload = () =>{

    // DOM objects
    let addButton = document.getElementById("add");
    let service_form = document.querySelectorAll('.service-form');
    let total_form = document.querySelector('#id_form-TOTAL_FORMS');
    const form_container = document.querySelector('#service-group');

    let formNumber = service_form.length - 1; // used for the prefix

    // Listen for click event on "Add" button
    addButton.onclick = () => cloneForm();

    

    const cloneForm = () =>{
      // Clone the rx-form
      let newForm = service_form[0].cloneNode(true);
      let formRegx = RegExp(`form-(\\d){1}-`,'g');

      formNumber ++;       

      newForm.innerHTML = newForm.innerHTML.replace(formRegx,`form-${formNumber}-`);       

      form_container.insertBefore(newForm,addButton);

      total_form.setAttribute("value",`${formNumber + 1}`);
      console.log(total_form.getAttribute("value"));

    }
}