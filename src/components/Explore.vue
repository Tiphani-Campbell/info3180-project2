<template>
    <h2>Explore</h2>
    <form @submit.prevent="searchCar" id="searchForm" method="GET">
        <div class="form-group">
            <label for="make">Make</label>
            <input type="text" class="form-control" v-model="searchMake" name="make" id="make">
        </div>
        <div class="form-group">
            <label for="model">Model</label>
            <input type="text" class="form-control" v-model="searchModel" name="model" id="make">
        </div>
        <button type="submit" class="btn btn-success" id="searchBtn">Search</button>
    </form>

    <div v-for="car in cars" class="car-view">
        <div class="car-item">
        <img :src="car.photo" :alt="car.car_type" class="car-image">
        <div class="car-info">
        {{ car.year }} <h4>{{ car.make }}</h4> {{ car.price }}
        {{ car.model }}
        </div>
        <button v-on:click="viewCar(car.id)" class="btn btn-primary" id="details">View more details</button>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            cars: [],
            searchMake: '',
            searchModel: ''
        };
    },
    methods: {
       searchCar(){
            let self = this;
            fetch('/api/search?make='+this.searchMake+'&model='+this.searchModel,{
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
    created() {
        let self = this;
        fetch('/api/cars',
        {
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
            console.log(data);
            self.cars = data;
        });
    },
};
</script>

<style>
form{
    width: max-width;
    margin:0 30% 0 30%;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0px 0px 10px 2px rgb(106, 106, 106);
    padding: 30px;
}
label{
    margin-top: 5px;
}
.form-group{
    margin: 2px 0px;
}
h2{
    margin:0 30% 0 30%;
    padding: 20px 0px 20px 0px;
}
.car-view{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-column-gap: 16px;
}
</style>