<template>

<div id="Main" style="margin-left:20px;margin-top:20px">


<h1 align=center><u>Login Page</u></h1>

<br>

<!-- <form v-on:submit.prevent="onSubmit">
<label for="email" style="margin-right:5px">Email:</label> 
<input type="text" id="email" name="email" required style="margin-right:10px" placeholder='email'> 

<label for="password" style="margin-right:5px">Password:</label> 
<input type="password" id="password" name="passsword" required style="margin-right:10px" placeholder='password'> 

v-model??

<input type="submit" value="Submit" v-on:click="loginUser()">
</form> -->

<form action=''>

    <input type='text' name='username' id='username' placeholder='username' style="margin-right:10px" v-model="formData.username"/>
      <input type='text' name='name' id='name' placeholder='name' style="margin-right:10px" v-model="formData.name"/>
      <input type='text' name='email' id='email' placeholder='email' style="margin-right:10px" v-model="formData.email"/>
      <input type='password' name='password' id='password' placeholder='password' style="margin-right:10px" v-model="formData.password"/>
      <button @click.prevent="createUser"> Register </button>
    </form>
</div>

</template>

<script>


export default {
  data(){
    return {
      formData: {
        username:'',
        name:'',  
        email: '',
        password: '',
      },
    }
  },
  name: 'NewUser',
  //emits:['callapi'],
  methods:{
    async createUser(){

  const res=await fetch("http://localhost:5000/api/v1/user",{
  method:'POST',
  headers:{
    'Content-Type':'application/json;charset=utf-8',
  },
  body: JSON.stringify(this.formData),
  }).catch((e)=>{console.log('error')})

//console.log(res)  

  if(res.ok){
    const data=await res.json()
    
    console.log(data)
    console.log("Registration successful! :) ")

    // setTimeout(()=>{window.location.reload();},1000)
    setTimeout(()=>{this.$router.push('/')},2000)
    
    }
else{
    console.log("something went wrong")
  }
    


  }
  
  
  },


}



</script>


<style scoped>
/* h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
} */
</style>
