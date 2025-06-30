import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    curruser:'',
    currusername:'',
    curruserid:-1,
    deckinfo:""
  },
  getters: {
    getcurruser(state){
      return state.curruser
    },
    getcurruserid(state){
      return state.curruserid
    },
    getcurrusername(state){
      return state.currusername
    },
    getdeckinfo(state){
      return state.deckinfo
    },
  },
  mutations: {
    setcurruser(state,user){
      state.curruser=user
    },
    setcurruserid(state,userid){
      state.curruserid=userid
    },
    setcurrusername(state,username){
      state.currusername=username
    },
    setdeckinfo(state,deckinfo){
      state.deckinfo=deckinfo
    },
    
  },
  actions: {
    // setcurruser({commit},curruser){
    //   commit(setcurruser, curruser)
    // }
  },
  modules: {
  }
})
