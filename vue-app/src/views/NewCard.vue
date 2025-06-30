<template>
    
    <div id='newcard' style="margin-left:20px;margin-right:20px;margin-top:20px">
		
		<h2><b> <u>Create New Card</u></b></h2>
		<br>
		
    
    
    <form action=''>

    

  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Card Obverse</label>
    <input type="name" name="cobv" class="form-control" required maxlength="100" v-model="formData.card_obverse">
    
    <div id="emailHelp" class="form-text">This is the data that goes on the front of the card</div>

  </div>

  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Card Reverse</label>
    <input type="description" name="crev" class="form-control" required maxlength="100" v-model="formData.card_reverse">
    
        
    <div id="emailHelp" class="form-text">This is the data that goes on the back of the card</div>
      
  </div>  


  <label class="form-label">Add Card to Decks</label>

<div class="mb-3 form-check">




    
    
     <div class="form-check form-check-inline" v-for="i in deckinfolist" v-bind:key="i[0]">

     <!-- v-model="formData.cardselectlist" -->

      <input class="form-check-input" type="checkbox" name="cardselect" :value="i[0]" id="flexCheckDefault" v-model="deckselectlist" @click="check($event)">
      
			<label class="form-check-label" name="decks" for="flexCheckDefault">
        {{i[0]}}. {{i[1]}}
      </label>
    </div>
</div>		
  
    <br>
<input type="Submit" class="btn btn-primary" value="Submit" @click.prevent="submitData">
</form>

<!-- 
{{formData.card_obverse}}
    {{formData.card_reverse}}  -->

  <!-- <ol><li v-for="i in deckinfolist" v-bind:key="i[0]">{{i[1]}}</li></ol>  -->

</div>

</template>

<script>


export default({

  name:'newcard',

  data(){
    // var deckinfolist=[];
    // var deckselectlist=[];
    return{
      formData: {
        card_reverse:'',
        card_obverse:'',
        deckselectlist:[],
      },
    deckinfolist:[],
    deckselectlist:[],
    }
    
  },
    
    methods:{
      
      check: function(e) {
      if (e.target.checked) {
        console.log(e.target.value)
        var x=e.target.value
        this.$data.deckselectlist.push(parseInt(x))
      }

      console.log(this.$data.deckselectlist)
      },

      async refreshlist(){

        const getdecks=await fetch("http://localhost:5000/api/v1/getdecklist",{
          method:'GET',
          headers:{
            'Content-Type':'application/json;charset=utf-8',
          },
          })
          if(getdecks.ok){
            const deckinfo=await getdecks.json()
            //console.log(curruser.username)
            console.log(deckinfo)
            this.$data.deckinfolist=deckinfo
          }
    
         
      },

      async submitData(){
        
        const res=await fetch("http://localhost:5000/api/v1/card",{
          method:'POST',
          headers:{
            'Content-Type':'application/json;charset=utf-8',
          },
          body: JSON.stringify({"obverse": this.$data.formData.card_obverse,
                  "reverse":this.$data.formData.card_reverse}),
        })
        
        .catch(
          (e)=>{console.log('error')}
          )

/* UPDATE DECK CID BASED ON SELECTIONS HERE!!! */
     

        // for(i in this.$data.deckselectlist){

        //   console.log(i)
        //   var j=parseInt(i)
        //    var p=this.$data.deckinfolist[j];
            
        //    console.log(p[5])
                   
        // }

        // this.$data.deckselectlist.forEach(element => {
        //   console.log(element)
        //   var p=this.$data.deckinfolist[element];
        //    var t=p[5] 
        //    console.log(t[2])
        // });
        
      
        
        //this.$router.push("/dashboard")
      
    
      },

    },

    mounted(){
        this.refreshlist()
    },

    
})


</script>
