

<script>
import Registration from '@/components/Registration.vue'
    export default {
        data() {
            return {};
        },
        components: { Registration }
    };
</script>


<template>
    <div class="form-container">
        <Registration />
    </div>
</template>

<style>
.form-container{
    background: rgb(242,242,242);
    background: linear-gradient(90deg, rgba(242,242,242,1) 33%, rgba(240,232,255,1) 100%); 
    height: calc(100vh - 60px);
}
</style>
