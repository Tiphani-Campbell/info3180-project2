<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark bg-primary fixed-top">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/"><img alt="auto logo" class="logo" src="@/assets/icons8-car-90.png" width="30" height="30" />United Auto Sales</router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent" >
          <ul class="navbar-nav">
            <li  id="addcar" v-if="`${isauth}` == 'true'" class="nav-item" >
              <RouterLink class="nav-link" to="/cars/new">Add Car</RouterLink>
            </li>

            <li id="explore" v-if="`${isauth}` == 'true'" class="nav-item" >
              <RouterLink class="nav-link" to="/explore">Explore</RouterLink>
            </li>

            <li id="profile" v-if="`${isauth}` == 'true'" class="nav-item">
              <RouterLink class="nav-link" :to="{path: '/users/'+ uid}" >My Profile</RouterLink>
            </li>
            <li id="logout" v-if="`${isauth}` == 'true'" class="nav-item">
              <RouterLink class="nav-link" to="/logout">Logout</RouterLink>
            </li>
            <li id="login" v-else>
             <RouterLink class="nav-link" to="/login">Login</RouterLink>
            </li>

            <li id="logout" v-if="`${isauth}` == 'true'" class="nav-item">
            </li>
            <li id="login" v-else>
            <RouterLink class="nav-link" to="/register">Register</RouterLink>
            </li>
            
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { RouterLink } from "vue-router";
export default {
    data() {
        return {
          uid: sessionStorage.getItem('uid'),
          isauth: localStorage.getItem('authed')
        };
    },
    created(){
    let self = this;
    setInterval(()=>{
       self.isauth = localStorage.getItem('authed');
    }, 4000);
    
    }
}
</script>

<style>
/* Add any component specific styles here */
.collapse{
  margin:0 0% 0% 71%;

}
.logo{
  margin:0 20px;
}
</style>