<template>
<div class="car-container">
    <div class="card-container">
        <div class="image">
            <img :src="car.photo" :alt=car.car_type >
        </div>
        <div class="content"> 
            <h3> {{car.year}} {{car.make}}</h3>
            <br>
            {{car.model}}
            <p>{{car.description}}</p>
            <div class="info">
                <div><label>Color</label> <div id="colour">{{car.colour}}</div></div>
                <div><label>Body Type</label> <div id="type">{{car.car_type}}</div></div>
            </div>
            <div class="info">
                <div><label>Price</label> <div id="price"> {{car.price}} </div></div>
                <div><label>Transmission</label> <div id="transmission">{{car.transmission}}</div></div>
            </div>

            <div  id="email" class="info">
                <button type="submit" class="btn btn-success" >Email Owner</button>
                <button id="faveBtn" type="submit" v-on:click="addfave" class="btn" ><img class="unfavourited" src="../assets/heart.svg"></button>
            </div>
        </div>
    </div>
 </div>
</template>
<script>
export default {
    data() {
        return {
            csrf_token: '',
            car: '',
            favourited: false,
        };
    },
    methods: {
        addfave(){
            let self = this;
            let status = 0;
            fetch(`/api/cars/${this.$route.params.car_id}`,
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
                self.car = data;
                console.log(data);
            });
          
            fetch(`/api/cars/${this.$route.params.car_id}/favourite`,
            {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'X-CSRFToken': this.csrf_token,
                    'Authorization': `Bearer ${sessionStorage.getItem('token')}`
                }
            })
            .then(function(response) {
                status = response.status
                return response.json();
            })
            .then(function(data) {
                let like =  document.querySelector("button#faveBtn img");
                if (status == 200){
                    like.classList.remove("unfavourited");
                    like.classList.add("favourited");
                }
                else{
                    like.classList.remove("favourited");
                    like.classList.add("unfavourited");
                }
            });
        },
        getCsrfToken() {
                let self = this;
                fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                    self.csrf_token = data.csrf_token;
                })
            
        }
    },
    created() {
        this.getCsrfToken();
        let self = this;
        let status = 0;
       
        fetch(`/api/cars/${this.$route.params.car_id}`,
        {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Authorization': `Bearer ${sessionStorage.getItem('token')}`
            }
        })
        .then(function(response) {
            status = response.status;
            return response.json();
        })
        .then(function(data) {
            self.car = data;
        });
        fetch(`/api/viewfavourite/${this.$route.params.car_id}`,
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
            self.favourited = data.message;
            let like =  document.querySelector("button#faveBtn img");
            if(self.favourited){
                like.classList.remove("unfavourited");
                like.classList.add("favourited");
            }
            else{
                like.classList.remove("favourited");
                like.classList.add("unfavourited");
            }
        });
        
    },
};
</script>
<style>

.favourited{
    filter: invert(19%) sepia(83%) saturate(7219%) hue-rotate(358deg) brightness(111%) contrast(122%);
    width: 2em;
}
.unfavourited{
    filter: grayscale(100%);
    width: 2em;
}

.car-container{
    background-color: rgb(232, 232, 232);
    padding:10px;
    height: fit-content;
    min-height: calc(100vh - 60px);
    display: flex;
    
}
.card-container{
    margin:5vh 15%;
    width:70%;
    height: calc(100vh - 200px);
    background-color: white;
    display: flex;
    overflow: hidden;
    border-radius: 10px;
    box-shadow: 0px 1px 5px 1px rgb(128, 128, 128);
}
.card-container .image{
    height:100%;
    width: 50%;
    overflow: hidden;
}
.card-container .content{
    height:100%;
    width: 50%;
    overflow: hidden;
}
.card-container img{
    min-width: 100%;
    min-height: 100%;
}
</style>