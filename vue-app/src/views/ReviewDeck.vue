<template>
    
	<div id='review' style="margin-left:20px;margin-right:20px;margin-top:20px">
		
		<h2><u><b> Deck Review - {{deckname}}</b></u></h2>
		<br>
		
    <div class="card">
    <div class="card-header">

      Card ID {{cardinfo.cid}}
    </div>
    <div class="card-body">
      <h3 class="card-title">{{cardinfo.obverse}}</h3><br>
      
				<span id="back_content">
		
			<button type="button" @click.prevent="flip()" class="btn btn-warning">Flip!</button>
    </span>
		 </div>
		
		</div>

  <br>

		
          <button type="submit" class="btn btn-primary" name="diff" value=1>Easy</button>


          <button type="submit" class="btn btn-primary" name="diff" value=2>Hard</button>
      <!--<a href="#" class="btn btn-primary">Easy</a>
      <a href="#" class="btn btn-primary">Hard</a>-->
<br><br>
    <a href="/exitdeck" class="btn btn-danger" align="right">Exit Deck</a>




</div>



</template>


<script>

export default({

  name:'delcard',
  data(){
    
    var cardinfo=[];
    var cardinfolist=[];
    var deckname=JSON.parse(localStorage.getItem('deckreviewname'));
    return{
      formData: {
        cardselectlist:[],
      },
        deckname,cardinfolist,cardinfo
    }
  },
    
    methods:{

        flip(){

          var x=this.$data.cardinfo.reverse

        document.getElementById("back_content").innerHTML = "<h2 style=color:red;>"+`${x}`+"</h2>";
      
		},
		

      async refreshlist(){

        var currindex=JSON.parse(localStorage.getItem('currindex'))
        var clist=JSON.parse(localStorage.getItem('clist'))

        var currcid=clist[currindex]



        const getcardata=await fetch("http://localhost:5000/api/v1/card/"+`${currcid}`,{
          method:'GET',
          headers:{
            'Content-Type':'application/json;charset=utf-8',
          },
          })
          if(getcardata.ok){
            const cardinfo=await getcardata.json()
            //console.log(curruser.username)
            console.log(cardinfo)
            console.log(cardinfo.cid)
            this.$data.cardinfo=cardinfo
          }
    
         
      },


    },

    mounted(){
        this.refreshlist()
    },

    
})

</script>


<style scoped>
button{
      margin-left:1px;margin-right:5px;
    }

</style>