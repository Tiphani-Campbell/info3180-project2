<template>
    <div class="registration-message">
        <div v-if="flag=='true'" class="alert alert-danger" role="alert">
            <ul>
                <li v-for="error in errors"> {{ error }} </li>
            </ul>
        </div>
        <div v-if="flag=='false'" class="alert alert-success" role alert>Registered Successfully</div>
    </div>


   
    <h2>Register New User</h2>
    <form @submit.prevent="registerForm" method="POST" id="registerForm" enctype = "multipart/form-data">
                <div class="row">
                    <div class="form-group col-md-6">
                        <label for="username" class="form-label">Username</label>
                        <input type="text" class="form-control" name="username" id="username" >
                    </div>
                    <div class="form-group col-md-6">
                        <label for="password" class="form-label">Password</label>
                        <input type="password" class="form-control"  name="password" id="password">
                    </div>
                </div>
                <div class="row">
                    <div class="form-group col-md-6">
                        <label for="name" class="form-label">Fullname</label>
                        <input type="text" class="form-control"  name="name" id="name" >
                    </div>

                    <div class="form-group col-md-6">
                        <label for="email" class="form-label">Email Address</label>
                        <input type="email" class="form-control"  name="email" id="email" >
                    </div>
                </div>

               <div class="form-group col-md-6">
                    <label for="location" class="form-label">Location</label>
                    <input type="text" class="form-control"  name="location" id="location" >
                </div>

            <div class="form-group" >
                    <label for="Biography" class="form-label">Biography</label>
                    <textarea  class="form-control"  name="biography" id="Biography" ></textarea>
            </div>
            <div class="form-group">
                <label for="photo" class="form-label">Photo</label> <br>
                <input type="file" class="form-control" id="photo"  name="photo" > 
            </div>
            <button type="submit" class="btn btn-success" >Register</button>
    </form>
</template>

<script>
export default{
    data(){
        return{
            csrf_token: '',
            message: '',
            errors: [],
            flag: ''
        };
    },
    methods: {
        registerForm(){
            let registerForm = document.getElementById('registerForm');
            let form_data = new FormData(registerForm);
            let self = this;
            fetch('/api/register', {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRFToken': this.csrf_token
                }
              })
              .then((response)=>{
                  return response.json();
              })
              .then((data)=>{
                  
                self.message = data;
               if (self.message.hasOwnProperty('error')){
                   self.errors = self.message.error;
                   self.flag = 'true';
               }else{
                   self.flag = 'false';
               }
              })
              .catch(function(error){
               console.log(error);
           });
        },
         getCsrfToken() {
                let self = this;
                fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    self.csrf_token = data.csrf_token;
                })
            
        },
    
    },
    created() {
        this.getCsrfToken();
    },   
}  ;  
</script>

<style>

form{
    width: 650px;
    margin:0 30% 0 30%;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0px 0px 10px 2px rgb(106, 106, 106);
    padding: 30px;
}
label{
    margin-top: 5px;
}
.form-group{
    margin: 5px 0px;
}
h2{
    margin:0 30% 0 30%;
    padding: 20px 0px 20px 0px;
}

</style>