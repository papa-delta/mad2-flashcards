<template>
    <div id="secure" style="margin-left:20px;margin-right:20px;margin-top:20px">

        <!-- {{username}} -->
		
    <h1 align="center"><b> CAUTION, {{this.$store.getters.getcurrusername}}!</b></h1>
		<br>

		
    <p>The action you are about to perform will delete your account from this app.<b> Account deletion is <u>irreversible and permanent</u>, and all data associated solely with your account will be lost!</b></p>

    <button  class="btn btn-danger" @click.prevent="deleteUser">Yes, delete my account!</button>
    <button  class="btn btn-success" @click.prevent="goBack">No, go back!</button>


        
    </div>
</template>


<script>


export default ({
    name:'deluser',
    date() {
        
    },
    methods:{
        async refreshinfo(){


            const getuser=await fetch("http://localhost:5000/api/v1/getuser/"+`${localStorage.getItem('email')}`,{
            method:'GET',
            headers:{
            'Content-Type':'application/json;charset=utf-8',
            },
             })
            if(getuser.ok){
            const curruser=await getuser.json()
            this.$store.commit('setcurruser',curruser.username)
            this.$store.commit('setcurrusername',curruser.name)
            this.$store.commit('setcurruserid',curruser.uid)
            }
        },
        async deleteUser(){

            const delcall=await fetch("http://localhost:5000/api/v1/user/"+`${this.$store.getters.getcurruser}`,{

                method:'DELETE',
                headers:{
                'Content-Type':'application/json;charset=utf-8',
                },
            })
            
            .catch(
            (e)=>{console.log('error')}
            )

            if(delcall.ok){

            await console.log("Deletion success!")
            
            setTimeout(()=>{this.$router.push("/")},1000)

            }

        },

        goBack(){
            this.$router.push("/dashboard")
        }


    },
    beforeMount(){
        this.refreshinfo()
    }
})
</script>







<style scoped>
    #secure {
        background-color: #FFFFFF;
        border: 3px solid #CCCCCC;
        padding: 20px;
        margin-top: 10px;
    }
    button{
      margin-left:1px;margin-right:5px;
      text-align:center;
      
        
        
    }
</style>