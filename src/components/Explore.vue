<template>
    <h2>Explore</h2>
    <form id="searchForm" method="GET">
        <div class="form-group">
            <label for="make">Make</label>
            <input type="text" class="form-control" name="make" id="make">
        </div>
        <div class="form-group">
            <label for="model">Model</label>
            <input type="text" class="form-control" name="model" id="make">
        </div>
        <button type="submit" class="btn btn-success" id="searchBtn">Search</button>
    </form>
    <div class="car-view">
        <ul class="cars__list">
            
        </ul>
    </div>
</template>
<script>
export default {
    
}
</script>
<style>

</style>