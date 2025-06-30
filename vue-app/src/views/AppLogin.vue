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
      <input type='text' name='email' id='email' placeholder='email' style="margin-right:10px" v-model="formData.email"/>
      <input type='password' name='password' id='password' placeholder='password' style="margin-right:10px" v-model="formData.password"/>
      <button @click.prevent="loginUser"> Login </button><br><br>
      <p><input type="submit" value="Register" @click.prevent="newUser"> </p>
    </form>
</div>

</template>

<script>


export default {
  data(){
    return {
      formData: {
        email: '',
        password: '',
      },
    }
  },
  name: 'AppLogin',
  //emits:['callapi'],
  methods:{
    async newUser(){
      this.$router.push('/newuser')
    },
    async loginUser(){

    // this.$store.commit('setcurruser','testuser')
    // console.log(this.$store.getters.getcurruser, "direct")
    // const x= this.$store.getters.getcurruser
    // console.log(x)
  
  //console.log(this.formData.email)
    
    // const usset= await fetch("http://localhost:5000/api/v1/getuser/"+`${this.formData.email}`,{
    // method:'GET',
    // headers:{
    //   'Content-Type':'application/json;charset=utf-8',
    // },
    // })
    // if(usset.ok){
    //   const curruser=await usset.json()
    //   console.log(curruser.username)}
      

  const res=await fetch("http://localhost:5000/login?include_auth_token",{
  method:'POST',
  headers:{
    'Content-Type':'application/json;charset=utf-8',
  },
  body: JSON.stringify(this.formData),
  }).catch((e)=>{console.log('error')})

//console.log(res)  

  if(res.ok){
    const data=await res.json()
    
    //console.log(data.response.user.authentication_token)

    localStorage.setItem(
      'auth-token',

      data.response.user.authentication_token
    )

    localStorage.setItem(
      'email',

      this.formData.email
    )


    //console.log(this.formData.email)
    
    const getuser=await fetch("http://localhost:5000/api/v1/getuser/"+`${this.formData.email}`,{
    method:'GET',
    headers:{
      'Content-Type':'application/json;charset=utf-8',
    },
    })
    if(getuser.ok){
      const curruser=await getuser.json()
      //console.log(curruser.username)
      this.$store.commit('setcurruser',curruser.username)
      this.$store.commit('setcurrusername',curruser.name)
      this.$store.commit('setcurruserid',curruser.uid)
      console.log(this.$store.getters.getcurrusername)
      //console.log(this.$store.getters.getcurruserid)
    }

    const getdecks=await fetch("http://localhost:5000/api/v1/getdecklist",{
    method:'GET',
    headers:{
      'Content-Type':'application/json;charset=utf-8',
    },
    })
    if(getdecks.ok){
      const deckinfo=await getdecks.json()
      //console.log(curruser.username)
      this.$store.commit('setdeckinfo',deckinfo)
      const info=this.$store.getters.getdeckinfo

      // for(var i in info){
      //   console.log("Iteration:",i)
      //     console.log(info[i][1])
      //     console.log("Iteration:",i,"Over")
      // }

      //console.log(info[1])
      //console.log(this.$store.getters.getcurruserid)
    }

   this.$router.push('/dashboard')

  }
  else{
    console.log("something went wrong")
  }
  //   .then(response=>response.json())
  //   .then(data=>console.log(data))
  
  },
}

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
