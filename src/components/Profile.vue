<template>
        <div class="user-info">
                <div class="photo"> 
                    <img :src="`/uploads/${user.photo}`" :alt=user.username >
                </div>
                <div class="content"> 
                    <h3>{{user.name}}</h3>
                    <div id="username">@{{user.username}}</div>
                    <p>{{user.biography}}</p>
                    <div class="info" id="emailc">
                        <div class="label">Email </div>
                        <div id="emailt">{{user.email}}</div>
                    </div>
                    <div class="info">
                        <div class="label">Location</div>
                        <div id="location">{{user.location}}</div>
                    </div>

                    <div class="info" id="date">
                        <div class="label">Joined </div>
                        <div id="date">{{user.date_joined}}</div>
                    </div>
                    
                </div>
        </div>
        
        <h3 id="carh">Cars Favourited</h3>
        <div class="car-cards">
            <div v-for= "car in cars" class="car-view">
                 <div class="car-item">
                     <div class="img-con">
                        <img class="car-image" :src="car.photo" :alt=car.car_type>
                    </div>
                    <div class="car-info"> 
                        <div class="card-title">
                            <div class="title">
                                {{ car.year }} {{car.make}}
                            </div> 
                            <div class="price">
                                <img src="../assets/price-tag.png" alt="price-tag" class="tag"/> {{car.price}}
                            </div>
                        </div>
                    
                    <h6>{{car.model}}</h6>
                    <button class="btn btn-primary" id="details" > <RouterLink :to="{path: '/cars/'+ car.id}" class="link ">View more details</RouterLink> </button>
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
            user:'',
            message:''
        };
    },
    created() {
        let self = this;
        let status = 0;
        fetch(`/api/users/${sessionStorage.getItem('user_id')}`,
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
        fetch(`/api/users/${sessionStorage.getItem('user_id')}/favourites`,
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
            if(status==400){
                self.message=data.message;
                console.log(self.message);
            }else{
                self.cars = data;
            }
            
        });
    },
};
</script>
<style>

.user-info{
    display: flex;
    min-height: 350px;
    height: fit-content;
    background-color: white;
    width: 55%;
    overflow: hidden;
    border-radius: 10px;
    margin: 25px 25%;
    box-shadow: 0px 1px 5px 1px rgb(128, 128, 128);
}
.photo{
    width: 150px;
    height: 150px;
    overflow: hidden;
    border-radius: 100%;
    box-shadow: 0px 0px 4px 2px rgb(80, 80, 80);
    margin: 30px;
}
.photo img{
    width: 200px;
}
.user-info .content{
    margin:20px;
    

}

.user-info .content .info{
    display:flex;
    flex-wrap: wrap;
    gap: 10%;
    font-weight: 600;
    margin-top:2%;
}
.user-info .content #emailc{
    margin-top:10%;
}
.user-info .content .info .label{
    font-weight: 600;
    color: rgb(107, 107, 107);
}
.user-info .content p{
    margin:0px;
    padding: 0px;
    color: rgb(107, 107, 107);
}
.user-info .content #username{
    font-weight: 700;
    color: rgb(107, 107, 107);
    margin-bottom: 5%;
}
.user-info #date{
    margin-bottom: 40px;
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
    width:max-content
 
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
.car-info button{
    margin-top:40px;
    width: 100%;
    padding:5px !important;
    box-shadow: 0px 1px 5px 1px rgb(177, 177, 177);
}
.car-info #details{
    color:white !important;
    height: 40px !important;
}
.link{

color: white !important;
text-decoration: none;
}
#carh{
    margin:50px 15% 50px 15%;
    font-weight: 800;

}
</style>