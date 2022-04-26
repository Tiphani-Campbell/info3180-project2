<script>
import Profile from "../components/Profile.vue";
export default {
    data() {
      return[]; 
    },
    components: {Profile}        
};
</script>

<template>
<div class="full-container">
  <Profile/>  
</div>
 
</template>
<style>
.full-container{
    background: rgb(242,242,242);
    background: rgb(240, 240, 240);
    padding:10px;
    height: fit-content;
    min-height: calc(100vh - 60px);
}
</style>
