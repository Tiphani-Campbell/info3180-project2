<template>
    <h2>Login to your account</h2>
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
                      this.$router.push('/explore');
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

#login-form{
    width: fit-content;
    margin:0 30% 0 30%;
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
.form-group{
    margin: 5px 0px;
}
h2{
    margin:0 30% 0 30%;
    padding: 20px 0px 20px 0px;
}
</style>