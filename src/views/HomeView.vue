<script>
export default {
    data() {
        return {
            message: "Hello World! This is Project 2"
        };
    },
}
</script>

<template>
    <div class="home-container">
      <div class="text">
        <div id="text">
        <h1>Buy and Sell <br> Cars Online</h1>
          <p>United Auto Sales provies the fastest easiest firendly way to buy or sell cars online. 
            Find a Great Price on the Vehicle on the Vehicle You Want.</p>
            <RouterLink to="/register" type="button" class="btn btn-primary">Register</RouterLink>
            <RouterLink to="/login" type="button" class="btn btn-success">Login</RouterLink>
          </div>
        </div>
      <div class="car-img-con">
        
      </div>
    </div>
    
</template>

<style>
/* Add any component specific styles here */
.home-container{
  display: flex;
  align-items: center;
  background-color: white;
  justify-content: center;
  text-align: center;
  margin:0px;
}
.text{
  width: 50%;
}
p{
  width:400px;
  margin: 0px 25% 0 25%
}
.btn{
  margin:10px;
  width:130px;
  border-radius: 5px;
}
h2{
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-weight: 700;
  
}
.car-img-con{
 background-image: url("@/assets/car.jpg");
 width: 50%;
 height: calc(100vh - 60px);
background-repeat: no-repeat;
background-size: cover;
background-position: bottom left; 
}

</style>