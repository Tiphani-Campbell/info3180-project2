<template>
    <div class="form-container">
        <Explore />
    </div>
</template>
<script>
import Explore from '@/components/Explore.vue'
export default {
    data(){
        return{};
    },
    components: { Explore }
}
</script>
<style>
.form-container{
    background-color: rgb(240, 240, 240);
    padding:10px;
    height: fit-content;
    min-height: calc(100vh - 60px);
}
</style>
