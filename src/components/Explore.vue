<template>
    <h2>Explore</h2>
    <form @submit.prevent="searchCar" id="searchForm" method="GET">
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

    <div v-for="car in cars" class="car-view">
        <img :src="`/uploads/${car.photo}`" :alt="car.car_type"><br>
        {{ car.year }} <h4>{{ car.make }}</h4> {{ car.price }}<br>
        {{ car.model }}
        <button v-on:click="viewCar(car.id)" class="btn btn-primary" id="details">View more details</button>
    </div>
</template>
<script>
export default {
    data(){
        return{
            cars: [],
            model:'',
            make: ''
        };
    },
    methods:{
        searchCar(){
            let self = this;
            fetch('/api/search?make='+this.make+'&model='+this.model,{
                method: 'GET',
                headers:{
                    'Accept': 'application/json',
                    'Authorization': `Bearer ${sessionStorage.getItem('token')}`
                }
            }).then((response)=>{
                return response.json();
            })
            .then((data)=>{
                console.log(data);
                self.cars = data;
            })
        },
        viewCar(id){
            this.$router.push('/cars/'+id);
        }
                   
        
    },
    created(){
        fetch('/api/cars',{
            method: 'GET',
            headers:{
                'Accept': 'application/json',
                'Authorization': `Bearer ${sessionStorage.getItem('token')}`
            }
        })
        .then(function(response){
            return response.json();
        })
        .then(function(data){
            console.log(data);
            self.cars = data;
        })
    }
};
</script>
<style>

</style>