<template>
</template>
<script>
export default {
    data() {
        return [];
    },
    methods:{
        logout(){
            fetch('/api/auth/logout', {
            method: 'GET',
            headers: {
                "Accept": "application/json",
                'X-CSRFToken': this.csrf_token,
                'Authorization': `Bearer ${sessionStorage.getItem('token')}`
            }
            })
            .then((response)=>{
                return response.json();
            })
            .then((data)=>{
                this.$router.push('/');
                sessionStorage.clear();
                
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
            
        }
    },
    created(){
        this.getCsrfToken();
        this.logout();
    }
};
</script>
<style>
</style>