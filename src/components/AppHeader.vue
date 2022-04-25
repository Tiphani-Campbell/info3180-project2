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
            <li class="nav-item">
              <RouterLink class="nav-link active" to="/register">Register</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/login">Login</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { RouterLink } from "vue-router";
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