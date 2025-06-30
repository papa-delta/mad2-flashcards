<template>
    <div id="secure" style="margin-left:20px;margin-right:20px;margin-top:20px">

        <!-- {{username}} -->
		
    <h2><b> Hello, {{this.$store.getters.getcurrusername}}!</b></h2>
		<br>
		<h3><u> Card Decks:</u></h3>
		
    <table class="mb-3 table table-striped table-hover table-bordered" style="padding:3px;" >
<thead>
		<tr>
      <th>Deck No</th>
      <th>Deck Name</th>
      <th>Deck Description</th>
      <th>Deck Average Difficulty</th>
      <th>Last Reviewed</th>
      <th>Actions</th>
    </tr>
</thead>
<tbody>
    <tr v-for="i in cardinfolist" v-bind:key="i[0]">
        <td>{{i[0]}}</td>
        <td>{{i[1]}}</td>
        <td>{{i[3]}}</td>
        <td v-if="i[2]==1">Easy</td>
        <td v-else>Hard</td>

        <td v-if="i[4]!=NULL">{{i[4]}}</td>
        <td v-else>None</td>

        <td>
          
          <button @click.prevent="reviewDeck(i[0])" type="submit" class="btn btn-primary flex-wrap"> Review</button>
          
          <button @click.prevent="editDeck(i[0])" class="btn btn-outline-dark">Edit</button>

          <button @click.prevent="deleteDeck(i[0])" class="btn btn-outline-danger">Delete</button>
        </td>

    </tr>		
</tbody>		
    </table>
  
    <button class="btn btn-outline-dark" @click.prevent="deckCreate">Create New Deck</button>
    <button class="btn btn-outline-dark" @click.prevent="cardCreate">Create New Card</button>
    <button class="btn btn-outline-danger" @click.prevent="cardDelete">Delete Existing Card</button>
    <button class="btn btn-danger" @click.prevent="logoutUser">Logout</button><br>
<br><h4>Other actions: </h4><hline/>
    <button class="btn btn-outline-dark" @click.prevent="exportData">Export Decks</button>
    <button class="btn btn-outline-dark" @click.prevent="importData">Import Decks</button>
    <button class="btn btn-danger" @click.prevent="deleteUser">Delete Account</button>


        
    </div>
</template>

<script>

  export default {
      name: 'dashboard',
      data() {          

        var info=this.$store.getters.getdeckinfo
        var cardinfolist=[];
        return{cardinfolist}

        // for(var i in info){
        // console.log("Iteration in dshborard:",i)
        //   console.log(info[i][1])
        //   cardinfolist.push(info[i])
        //   console.log("Iteration:",i,"Over")
        // }
        // for(var i in cardinfolist){
        //   console.log(cardinfolist[i])
        // }
      
      },
      
      methods:{

        // async reviewDeck(x){

        //   const reviewcall
          
          
        // },

        async deleteDeck(x){

          const delcall=await fetch("http://localhost:5000/api/v1/deck/"+`${x}`,{
          method:'DELETE',
          headers:{
            'Content-Type':'application/json;charset=utf-8',
          },
        })
    if(delcall.ok){

     await console.log("Deletion success!")
      

      setTimeout(()=>{window.location.reload();},500)

     // this.$forceUpdate();

    }
          

          
          console.log(x)
          return
        },

        async reviewDeck(x){
          
          const reviewcall=await fetch("http://localhost:5000/api/v1/getcardlist/"+`${x}`,{
          method:'GET',
          headers:{
            'Content-Type':'application/json;charset=utf-8',
          },

          })

          if(reviewcall.ok){
            const clist=await reviewcall.json()
            // console.log(clist)
            localStorage.setItem(
              'clist',JSON.stringify(clist))

            localStorage.setItem(
              'currindex',JSON.stringify(0))
            localStorage.setItem(
              'length',JSON.stringify(clist.length))
            localStorage.setItem(
              'deckreviewname',JSON.stringify(this.$store.getters.getdeckinfo[x][1]))

            this.$router.push('/reviewdeck')

            // console.log(clist.length)



            // x=localStorage.getItem('clist')
            // console.log(JSON.parse(x))
          }

        },
        async editDeck(x){

        },

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

    const getdecks=await fetch("http://localhost:5000/api/v1/getdecklist",{
    method:'GET',
    headers:{
      'Content-Type':'application/json;charset=utf-8',
    },
    })
    if(getdecks.ok){
      const deckinfo=await getdecks.json()
 
      this.$store.commit('setdeckinfo',deckinfo)
    }

                  
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
                  this.$store.commit('setdeckinfo',deckinfo)
                }

             
            const info=this.$store.getters.getdeckinfo
            console.log(this.$store.getters.getdeckinfo)
            console.log("info inside refresh",info[1])
            for(var i in info){
              console.log("Iteration in dshboard:",i)
              console.log(info[i][1])
              this.$data.cardinfolist.push(info[i])
              console.log("Iteration:",i,"Over")
            }
          },

          async displayDashboard(){

          },
          cardCreate(){
              this.$router.push('/newcard')
          },
          cardDelete(){
              this.$router.push('/delcard')
          },
          deckCreate(){
              this.$router.push('/newdeck')
          },
          deleteUser(){
              this.$router.push('/deluser')
          },
          async logoutUser(){
              const res = await fetch('http://localhost:5000/logout')
              if (res.ok) {
                  localStorage.clear()
                  this.$router.push('/')
              } else {
                  console.log('could not logout the user')
              }
          },
          
        
      },
      beforeMount(){
          this.refreshinfo()
      },
      mounted(){
          this.refreshlist()
      }
            
          
  }

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
    }
</style>
