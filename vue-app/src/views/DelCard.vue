<template>
    
    <div id='delcard' style="margin-left:20px;margin-right:20px;margin-top:20px">
	
		<h2><b> <u>Delete Existing Card</u></b></h2>
		<br>
    
    <form method="POST">
   

  <label class="form-label">Delete Card(s)</label>
    <div id="emailHelp" class="form-text">Select at least one. Also, kindly ensure that the selected cards are not currently part of any decks.</div><br>


  <div class="mb-3 form-check">

    <div class="form-check form-check-inline" v-for="i in cardinfolist" v-bind:key="i[0]">

     <!-- v-model="formData.cardselectlist" -->

      <input class="form-check-input" type="checkbox" name="cardselect" :value="i[0]" id="flexCheckDefault" v-model="cardselectlist" @click="check($event)">
      
			<label class="form-check-label" name="cards" for="flexCheckDefault">
        {{i[0]}}. {{i[1]}}
      </label>
    </div>
		

  
  </div>
  
    
<input type="submit" class="btn btn-primary" value="Submit" @click.prevent="submitData">

</form>

  <br>


    </div>

</template>



<script>

export default({

  name:'delcard',
  data(){
    
    var cardinfolist=[];
    var cardselectlist=[];
    return{
      formData: {
        cardselectlist:[],
      },
    cardinfolist,cardselectlist
    }
  },
    
    methods:{

        check: function(e) {
      if (e.target.checked) {
        console.log(e.target.value)
        var x=e.target.value
        this.$data.cardselectlist.push(parseInt(x))
      }

      console.log(this.$data.cardselectlist)
    },


      async refreshlist(){

        const getcards=await fetch("http://localhost:5000/api/v1/getallcardlist",{
          method:'GET',
          headers:{
            'Content-Type':'application/json;charset=utf-8',
          },
          })
          if(getcards.ok){
            const cardinfo=await getcards.json()
            //console.log(curruser.username)
            console.log(cardinfo)
            this.$data.cardinfolist=cardinfo
          }
    
         
      },

      async submitData(){

        for(var element in this.$data.cardselectlist) {
        
        // const res=await fetch("http://localhost:5000/api/v1/card/"+`${this.element}`,{

      const delcall=await fetch("http://localhost:5000/api/v1/card/"+`${this.$data.cardselectlist[element]}`,{

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
        }
    }         
        
      // setTimeout(()=>{window.location.reload();},1000)
      this.$router.push("/dashboard")
      
    
      },

    },

    mounted(){
        this.refreshlist()
    },

    
})

</script>
