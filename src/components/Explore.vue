<template>
    <h2 id="exploreh">Explore</h2>
    <form @submit.prevent="searchCar" id="searchForm" method="GET">
        <div class="row">
            <div class="form-group col-md-5">
                <label for="make">Make</label>
                <input type="text" class="form-control" v-model="searchMake" name="make" id="make">
            </div>
            <div class="form-group col-md-5">
                <label for="model">Model</label>
                <input type="text" class="form-control" v-model="searchModel" name="model" id="make">
            </div>
            <button type="submit" class="btn btn-success col-md-3" id="searchBtn">Search</button>
        </div>
    </form>

    <div class="car-cards">
        <div v-for="car in cars" class="car-view">
            <div class="car-item">
                <div class="img-con">
                    <img :src="car.photo" :alt="car.car_type" class="car-image">
                </div>
            <div class="car-info">
                <div class="card-title">
                    <div class="title">{{ car.year }} {{ car.make }}</div>
                    <div class="price"><img alt="price-tag" class="tag" src="@/assets/price-tag.png" />{{ car.price }}</div>
                </div>
                <h6>{{ car.model }}</h6>
            
            <button v-on:click="viewCar(car.id)" class="btn btn-primary" id="details">View more details</button>
            </div>
            </div>
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
#searchForm{
    width: 70%;
    margin:0 15% 50px 15%;
    background-color: white;
    border-radius: 10px;
    box-shadow: 4px 4px 5px 1px rgb(177, 177, 177);
    padding: 30px 50px 50px 50px;
}

#searchForm label{
    margin-bottom: 5px 0;
    font-weight: 600;
}
#searchForm .form-control{
    height: 45px;

}
.form-group{
    margin: 2px 0px;
}
#exploreh{
    margin:0 15% 0 15%;
    padding: 20px 0px 20px 0px;
}

#searchBtn{
    margin: 35px 0px 0px 0px;
    height: 45px;
    width: 140px;
}
.car-cards{
    width: 70%;
    overflow: hidden;
    padding-bottom: 20px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
    margin:0 15% 50px 15%;
}
.car-view{
    width: 25%;
    min-width: 300px;
    overflow: hidden;
    height:360px;
    background-color: white;
    box-shadow: 0px 1px 5px 1px rgb(177, 177, 177);
    border-radius: 5px;
    margin: 5px;
}
.img-con{
    width: 320px;
    height:180px;
    overflow: hidden;
    
}
.car-image{
    width:110% !important;
    min-height: 180px;
    max-height: 350px;
}
.car-info{
    margin:1.5%;
    margin-top:15px;
    width: 85%;

}
.car-info .title{
    width: fit-content;
    margin: 5px;
    font-weight: 600;
    font-size: large;
} 
.car-info .price{
    background-color: rgb(0, 206, 107);
    color:white;
    padding-right: 8px;
    padding-top:5px;
    border-radius: 10px;
 
}
.car-info .price img{
    height: 20px;
    margin:5px 8px;
}
.car-info h6{
    margin: 5px;
    color:rgb(104, 104, 104);
}

.card-title{
    display: flex;
    justify-content: space-between;
}
.car-view button{
    margin-top:40px;
    width: 100%;
    box-shadow: 0px 1px 5px 1px rgb(177, 177, 177);
}

</style>