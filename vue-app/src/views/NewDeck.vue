<template>
    
    <div id='newdeck' style="margin-left:20px;margin-right:20px;margin-top:20px">
		
	<h2><b> <u>Create New Deck</u></b></h2>
		<br>
		
    
    
    <form action="">
<!-- 
      <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Deck ID</label>
    <input type="name" name="did" class="form-control" required>
    
    <div id="emailHelp" class="form-text">Must be unique and not match any previous deck ID</div>
  </div> -->

  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Deck Name</label>
    <input type="name" name="dname" class="form-control" required maxlength="100" v-model="formData.deck_name">
    
    <!--<div id="emailHelp" class="form-text">*required</div>-->
  </div>

  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Deck Description</label>
    <input type="description" name="ddesc" class="form-control" required maxlength="100" v-model="formData.deck_description">
    <div id="emailHelp" class="form-text">Please add a small description of the new deck</div>
  </div>
  

  <label class="form-label">Add Cards</label>
    <div id="emailHelp" class="form-text">Select at least one</div>


  <div class="mb-3 form-check">



  <!-- <ol><li v-for="i in cardselectlist" v-bind:key="i[0]">{{i[3]}}</li></ol> -->

    
    
     <div class="form-check form-check-inline" v-for="i in cardinfolist" v-bind:key="i[0]">

     <!-- v-model="formData.cardselectlist" -->

      <input class="form-check-input" type="checkbox" name="cardselect" :value="i[0]" id="flexCheckDefault" v-model="cardselectlist" @click="check($event)">
      
			<label class="form-check-label" name="cards" for="flexCheckDefault">
        {{i[0]}}. {{i[1]}}
      </label>
    </div>
		
    <!-- {{formData.deck_description}}
    {{formData.deck_name}} -->
  
  </div>


<!-- <button @click.prevent="submitData"> Submit </button> -->
<br>
    
<input type="submit" class="btn btn-primary" value="Submit" @click.prevent="submitData">

</form>

  <br>


    </div>

</template>



<script>


export default({
    name:'newdeck',

  data(){
    
    var cardinfolist=[];
    var cardselectlist=[];
    return{
      formData: {
        deck_name:'',
        deck_description:'',
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
        
        const res=await fetch("http://localhost:5000/api/v1/deck",{
          method:'POST',
          headers:{
            'Content-Type':'application/json;charset=utf-8',
          },
          body: JSON.stringify({"deckname": this.$data.formData.deck_name,
                  "deck_description":this.$data.formData.deck_description,
                  "cid":this.$data.cardselectlist}),
        })
        
        .catch(
          (e)=>{console.log('error')}
          )


        
        
        
        this.$router.push("/dashboard")
      },
    },

    beforeMount(){
      
      },
      mounted(){
              //console.log("TREST");

        this.refreshlist()
      }

    
})
</script>
