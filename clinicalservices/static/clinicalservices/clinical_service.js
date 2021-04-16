window.onload = () =>{

    // DOM objects
    let addButton = document.getElementById("add");
    let service_form = document.querySelectorAll('.service-form');
    let total_form = document.querySelector('#id_form-TOTAL_FORMS');
    const form_container = document.querySelector('#service-group');
    let formNumber = service_form.length - 1; // used for the prefix
    let totalFormNumber = formNumber;
   

    // Listen for click event on "Add" button
    addButton.onclick = () => cloneForm();

    const cloneForm = () =>{
      // create a remove button
      let removeBtn = document.createElement('input');
      removeBtn.setAttribute('type','button');
      removeBtn.setAttribute('class','removeBtn btn btn-sm m-2 btn-danger');
      removeBtn.setAttribute('value','Remove');

      // Clone the rx-form
      let newForm = service_form[0].cloneNode(true);
      let formRegx = RegExp(`form-(\\d){1}-`,'g');

      formNumber ++;    
      totalFormNumber ++;   
      // set id of remove btn to formNumber
      removeBtn.setAttribute('id',`remove-${formNumber}`);

      removeBtn.onclick = (e) =>{removeElement(newForm,totalFormNumber,e)};

      newForm.innerHTML = newForm.innerHTML.replace(formRegx,`form-${formNumber}-`);  
      newForm.appendChild(removeBtn);     

      form_container.insertBefore(newForm,addButton);

      total_form.setAttribute("value",`${totalFormNumber + 1}`);
      
      return;

    }

    const removeElement = (element,totalForms,e) =>{
      // remove the parent element the button belongs to
      element.remove();
      // decrement totalForms
      totalForms--;
      // Update the total forms value
      totalFormNumber = totalForms;
      
      total_form.setAttribute("value",`${totalForms + 1}`);
    }
}