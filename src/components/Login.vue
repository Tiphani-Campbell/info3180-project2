<template>
    <h2 id="loginh">Login to your account</h2>
    <form @submit.prevent="login" id="loginForm" method = 'POST'>
        <div class="form-group">
            <label for="username" class="form-label">Username</label>
            <input type="text" class="form-control" name="username" id="username">
        </div>
        <div class="form-group">
            <label for="password" class="form-label">Password</label>
            <input type="password" class="form-control" name="password" id="password">
        </div>
        <button type="submit" class="btn btn-success" id="login">Login</button>
    </form>
</template>
<script>
import { useRoute } from 'vue-router';
export default {
    data(){
        return{
            message: ''
        };
    },
    methods:{
        login(){
            let loginForm = document.getElementById('loginForm');
            let form_data = new FormData(loginForm);
            let self = this;
            let status = 0;
            fetch('/api/auth/login', {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRFToken': this.csrf_token
                }
              })
              .then((response)=>{
                  status = response.status;
                  return response.json();
              })
              .then((data)=>{
                  self.message=data;
                  if (status == 200){
                      console.log(self.message.token);
                      sessionStorage.setItem('token', self.message.token);
                      sessionStorage.setItem('isauth', 'true');
                       fetch('/api/user_id', {
                        method: 'GET',
                        headers: {
                            'Accept': 'application/json',
                            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
                        }
                        })
                        .then(function(response) {
                            return response.json();
                        })
                        .then(function(data) {
                            sessionStorage.setItem('user_id', data.message);
                            localStorage.setItem('user_id', data.message);
                        });
                        this.$router.push('/explore')

                  }
              })
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
    
}
</script>

<style>
    #loginForm{
        width: 400px;
        margin:0 35% 0 35%;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 0px 10px 2px rgb(106, 106, 106);
        padding: 30px;
    }
    label{
        margin-top: 5px;
    }
    #login{
        margin: 5%;
        width: 90%;
    }
    #loginForm .form-group{
        margin: 15px 0px;
    }
   #loginh{
        margin:0 35% 0 35%;
        padding: 20px 0px 20px 0px;
    }
</style>