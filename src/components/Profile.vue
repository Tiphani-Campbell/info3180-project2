<template>
 <div class="parentcard">
        <div class="photo"> 
            <img :src=user.photo :alt=user.username >
        </div>
        <div class="content"> 
            <h3>{{user.name}}</h3>
            <div id="username">@{{user.username}}</div>
            <p>{{user.biography}}</p>
            <div class="info">
                <div><label>Email</label> <div id="email">{{user.email}}</div></div>
            </div>
            <div class="info">
                <div><label>Location</label> <div id="location">{{user.location}}</div></div>
            </div>

            <div class="info">
                <div><label>Joined</label> <div id="date">{{user.date_joined}}</div></div>
            </div>
            
        </div>
 </div>

    <h3>Cars Favourited</h3>
        <div v-for= "car in cars" class="car__view">
            <img class="car-photo" :src="`/uploads/${car.photo}`" :alt=car.car_type>
                <div class="car-info"> <div>{{ car.year }} {{car.make}}</div> <div id="pricespan"><img src="../assets/price-tag.png" /> {{car.price}}</div></div>
                <p class="card-model">{{car.model}}</p>
                <button class="btn btn-primary" > <RouterLink :to="{path: '/cars/'+ car.id}" class="nav-link ">view more details</RouterLink> </button>
            </div>

</template>

<script>
export default {
    data() {
        return {
            cars: [],
            user:''
        };
    },
    created() {
        let self = this;
        fetch(`/api/users/${sessionStorage.getItem('uid')}`,
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
            self.user = data;
        });
        fetch(`/api/users/${sessionStorage.getItem('uid')}/favourites`,
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
            self.cars = data;
        });
    },
};
</script>
<style>

</style>