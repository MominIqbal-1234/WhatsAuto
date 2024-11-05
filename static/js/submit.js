
console.log("Working...")



function clearAllInputFields() {
    // Get all input elements in the document
    const inputs = document.querySelectorAll('input');

    // Iterate over each input and set its value to an empty string
    inputs.forEach(input => {
        input.value = '';
    });
}




document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("userForm");
    let server_ip = document.getElementById('sessionData').getAttribute('data-user-name');

    spinner = `<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>`
    create_button = document.getElementById('create_button')




    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission
        console.log("call again")
        
        const username = document.getElementById("username").value;
        create_button.innerHTML = spinner


            // const url = 'http://127.0.0.1:8000/api/user/';
            const url = `http://${server_ip}/api/user/`;
            const formData = new FormData(form);

            fetch(url, {
                method: 'POST',
                body: formData, // automatically sets the multipart/form-data headers
            })



                .then(response => {
                    console.log('Status Code:', response.status);
                    const userData = response.data;
                    console.log('User Data:', userData);
                    if (response.status === 201) {
                        const alert = document.getElementById("alert").innerHTML = `
                    
                    <div class="alert alert-success alert-dismissible fade show" role="alert">
                    <strong>Success ! </strong> Data Insert Successful
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>
                    `
                    create_button.innerText = "Create User"
                    window.location.href = `/create_user_machine/${username}`
                    // window.location.reload('/');
                    clearAllInputFields()
                    }


                    // if (response.status === 500) {
                    //     const alert = document.getElementById("alert").innerHTML = `
                        
                    //     <div class="alert alert-danger alert-dismissible fade show" role="alert">
                    // <strong>Success ! </strong> Machine is Offline
                    // <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    // </div>
                    
                    // `
                    // create_button.innerText = "Create User"
                    // // window.location.reload('/');
                    // // clearAllInputFields()
                    // }


                    // else if (response.status === 404) {
                    //     const alert = document.getElementById("alert").innerHTML = `
                    
                    // <div class="alert alert-danger alert-dismissible fade show" role="alert">
                    // <strong>Error ! </strong> Machine is Offline
                    // <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    // </div>
                    // `
                    // create_button.innerText = "Create User"
                    //
                    // }
                    else { 
                        // window.location.reload('/');
                        // response.json(); // Send Data
                        // console.log(response.json(),"response.json();")

                        return response.json(); // Send Data
                        // window.location.reload('/');
                    }
                })
                .then(data => {
                    console.log(data)
                    for (const key in data) {
                        if (Object.hasOwnProperty.call(data, key)) {
                            const value = data[key];
                            console.log(`${key}:`, value);

                            if (key == 'username') {


                                const alert = document.getElementById("alert").innerHTML = `
                    
                        <div class="alert alert-danger alert-dismissible fade show" role="alert">
                        <strong>Error ! </strong> ID is Already Exist
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                        </div>
                        `
                        create_button.innerText = "Create User"

                            }


                            else if (key == 'cnic') {
                                const alert = document.getElementById("alert").innerHTML = `
                    
                        <div class="alert alert-danger alert-dismissible fade show" role="alert">
                        <strong>Error ! </strong> ${key} : ${value}
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                        </div>
                        `
                        create_button.innerText = "Create User"
                            }




                        else if (key == 'phone_number') {
                                const alert = document.getElementById("alert").innerHTML = `
                    
                        <div class="alert alert-danger alert-dismissible fade show" role="alert">
                        <strong>Error ! </strong> ${key} : ${value}
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                        </div>
                        `
                        create_button.innerText = "Create User"
                            }




                            else {
                                const alert = document.getElementById("alert").innerHTML = `
                    
                        <div class="alert alert-danger alert-dismissible fade show" role="alert">
                        <strong>Error ! </strong> ${value}
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                        </div>
                        `
                        create_button.innerText = "Create User"
                            }

                        }
                    }

                })



        
    });




});






console.log("userFormUpdate Working...")

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("userFormUpdate");
    const id = document.getElementById("id").value;
    let server_ip = document.getElementById('sessionData').getAttribute('data-user-name');
    
    spinner = `<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>`
    create_button = document.getElementById('create_button')


    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission
        create_button.innerHTML = spinner

        // const url = `http://127.0.0.1:8000/api/user/${id}/`;
        const url = `http://${server_ip}/api/user/${id}/`;
        const formData = new FormData(form);

        fetch(url, {
            method: 'PATCH',
            body: formData, // automatically sets the multipart/form-data headers
        })
            // -------------------------------------
            .then(response => {
                console.log('Status Code:', typeof response.status);
                console.log('Data:',  response.data);
                
                if (response.status === 200) {
                    const alert = document.getElementById("alert").innerHTML = `
                        
                        <div class="alert alert-success alert-dismissible fade show" role="alert">
                        <strong>Success ! </strong> Data Update Successful
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                        </div>
                        `
                        create_button.innerText = "Create User"
                        // window.location.reload('/');
                }
                else { return response.json(); }
            })
            .then(data => {
                console.log(data)
                for (const key in data) {
                    if (Object.hasOwnProperty.call(data, key)) {
                        const value = data[key];
                        console.log(`${key}:`, value);

                        if (key == 'username') {


                            const alert = document.getElementById("alert").innerHTML = `
                        
                            <div class="alert alert-danger alert-dismissible fade show" role="alert">
                            <strong>Error ! </strong> ID is Already Exist
                            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                            </div>
                            `
                            create_button.innerText = "Create User"


                        }
                        else {
                            const alert = document.getElementById("alert").innerHTML = `
                        
                            <div class="alert alert-danger alert-dismissible fade show" role="alert">
                            <strong>Error ! </strong>${value}
                            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                            </div>
                            `
                            create_button.innerText = "Create User"
                        }

                    }
                }

            })
        //   ---------------------------
    });
});





document.addEventListener("DOMContentLoaded", function () {
    const imageForm = document.getElementById("imageForm"); // Make sure to give your image upload form an ID of 'imageForm'
    let server_ip = document.getElementById('sessionData').getAttribute('data-user-name');
    imageForm.addEventListener("submit", function (event) {
        const id = document.getElementById("id").value;
        event.preventDefault(); // Prevent the default form submission

        const formData = new FormData(imageForm);
        const url = `http://${server_ip}/api/user/${id}/`; // Adjust URL to your image upload endpoint

        fetch(url, {
            method: 'PATCH',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            console.log('Image upload response:', data);
            window.location.reload(`/updateUser/${id}`);
            // Update your UI accordingly
        })
        .catch(error => console.error('Error uploading image:', error));
    });
});
