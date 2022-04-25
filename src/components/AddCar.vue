<template>
    <div class="registration-message">
        <div v-if="flag=='true'" class="alert alert-danger" role="alert">
            <ul>
                <li v-for="error in errors"> {{ error }} </li>
            </ul>
        </div>
        <div v-if="flag=='false'" class="alert alert-success" role alert>Registered Successfully</div>
    </div>

      <h2>Add New Car</h2>
        <form @submit.prevent="addCar" method="POST" id="carForm" enctype = "multipart/form-data">
            <div class="form-group">
                <label for="make" class="form-label">Make</label>
                <input type="text" class="form-control" name="make" id="make" >
            </div>
            <div class="form-group">
                <label for="model" class="form-label">Model</label>
                <input type="text" class="form-control"  name="model" id="model">
            </div>

                <div class="form-group">
                    <label for="colour" class="form-label">Colour</label>
                    <input type="text" class="form-control"  name="colour" id="colour" >
                </div>

                <div class="form-group">
                    <label for="year" class="form-label">Year</label>
                    <input type="year" class="form-control"  name="year" id="year" >
                </div>

                <div class="form-group">
                    <label for="colour" class="form-label">Price</label>
                    <input type="text" class="form-control"  name="price" id="price" >
                </div>

                <div class="form-group">
                    <label class="form-label" for="type">Car Type</label>
                    <select class="form-control" id="type" name="type">
                    <option>Hatchback</option>
                    <option>Sedan</option>
                    <option>SUV</option>
                    <option>Truck</option>
                    </select>
                </div>

            <div class="form-group">
                <label class="form-label" for="transmission">Transmission</label>
                <select class="form-control" id="transmission" name="transmission">
                <option>Automatic</option>
                <option>Manual</option>
                </select>
            </div>
            <div class="form-group">
                    <label for="description" class="form-label">Description</label>
                    <textarea  class="form-control"  name="description" id="description" ></textarea>
            </div>
            <div class="form-group">
                <label for="photo" class="form-label">Upload Photo</label> 
                <input type="file" class="form-control" id="photo"  name="photo"> 
            </div>
            <button type="submit" class="btn btn-success">Save</button>
        </form>
</template>

<script>
export default {
    data() {
        return {
            csrf_token: '',
            message: '',
            errors: [],
            flag: ''
        };
    },
    methods: {
        addCar(){
            let carForm = document.getElementById('carForm');
            let form_data = new FormData(carForm);
            let self = this;
            let status = 0;
            fetch('/api/cars', {
                method: 'POST',
                body: form_data,
                headers: {
                    "Accept": "application/json",
                    'X-CSRFToken': this.csrf_token,
                    'Authorization': `Bearer ${sessionStorage.getItem('token')}`
                }
              })
              .then((response)=>{
                  status= response.status;
                  return response.json();
              })
              .then((data)=>{
                console.log(sessionStorage.getItem('token'));
                console.log(data);
                self.message = data;
                if (status == 201){
                    self.flag = 'false';
                }else{
                    self.errors = self.message.error;
                    self.flag = 'true';
                }
              })
        },
         getCsrfToken() {
                let self = this;
                fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    self.csrf_token = data.csrf_token;
                })
            
        },
    
    },
    created() {
        this.getCsrfToken();
    },
};
</script>

<style>
.hide{
    display:none;
}
.show{
    display: block;
}
.width{
  width: 36rem;
  padding-right: 0.75rem;
  padding-left: 0.75rem;
  margin-right: auto;
  margin-left: auto;
}
.space_between{
    margin-right: 10px;
}
.w_full{
    width:100%;
}
.btn_{
    margin-top: 1em;
    padding:4px 24px;
    border: none;
    border-radius: 4px;
}
.card_{
    margin-top:2em;
    padding:1em;
    border-radius: 6px;
    box-shadow: 2px 2px 10px 4px  rgba(0,0,0,.1);
    border: 2px solid transparent;
}
h3{
    font-weight: bold;
}
@media screen and (max-width:800px){
  .width{
    width: 100%;
  }
  
}
</style>