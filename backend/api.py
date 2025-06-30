from email import message
from lib2to3.pgen2 import token
from pathlib import PureWindowsPath
from flask_restful import *
from flask_restful import reqparse
from flask_restful import fields,marshal_with
from werkzeug.exceptions import HTTPException
from flask import make_response
from models import *
from flask import *
from helper import * 
from flask_cors import CORS,cross_origin
from flask_security import *
from flask import jsonify
from flask.views import MethodView

# from flask_restplus.api import Swagger




# user = users.query.all()
# x=user[-1].uid
# uid=x+1
# print(x,uid)

# output_fields={
#     "user_id":fields.Integer,
#     "email"
# }

# dks = decks.query.filter_by(did=0).first()
# if(dks==None):
#     print("None")
# else:
#     print(dks.deck_name)

# x = decks.query.filter_by(did=4).first()
# print(x.deck_name,x.deck_description,x.cid,x.last_reviewed)

# x = decks.query.filter_by(did=4).update(dict(deck_name='test1234foo',deck_description='test1234bar',cid='3,1,4',last_reviewed='foobar'))
# db.session.commit()
# x = cards.query.filter_by(cid=4).first()
# print(x.score, "type:", type(x.score))


create_user_parser=reqparse.RequestParser()
create_user_parser.add_argument('username')
create_user_parser.add_argument('name')
create_user_parser.add_argument('email')
create_user_parser.add_argument('password')
create_user_parser.add_argument('decks_owned')

modify_user_parser=reqparse.RequestParser()
modify_user_parser.add_argument('username')
modify_user_parser.add_argument('name')
modify_user_parser.add_argument('decks_owned')

create_deck_parser=reqparse.RequestParser()
create_deck_parser.add_argument('deckname')
create_deck_parser.add_argument('cid')
create_deck_parser.add_argument('deck_description')

modify_deck_parser=reqparse.RequestParser()
modify_deck_parser.add_argument('deckname')
modify_deck_parser.add_argument('cid')
modify_deck_parser.add_argument('deck_score')
modify_deck_parser.add_argument('deck_description')
modify_deck_parser.add_argument('last_reviewed')

create_card_parser=reqparse.RequestParser()
create_card_parser.add_argument('obverse')
create_card_parser.add_argument('reverse')

modify_card_parser=reqparse.RequestParser()
modify_card_parser.add_argument('obverse')
modify_card_parser.add_argument('reverse')
modify_card_parser.add_argument('score')

class DeckAPI(Resource):
    #@auth_required("token") - ADD FOR ALL
    def get(self,did):

        dks = decks.query.filter_by(did=did).first()

        if(dks==None):
            return{"status":404,
            "message":"Deck doesn't exist"},404
        else:
            return {"did":did,
        "deck_name":dks.deck_name,
        "deck_description":dks.deck_description,
        "deck_cid":dks.cid,
        "deck_score":dks.deck_score,
        "deck_lastreviewed":dks.last_reviewed}

    
    def post(self):

        args=create_deck_parser.parse_args()
        deckname_new=args.get("deckname",None)
        cid_new=args.get("cid",'')
        deck_description_new=args.get("deck_description",'')

        if(deckname_new==None or deck_description_new==None):
            return{"status":400,
            "message":"Deck name and deck description are mandatory"},400
                
        deck = decks.query.all()

        for i in deck:
            if i.deck_name==deckname_new:
                return{"status":400,"message":"Deck name already taken!"},400

        x=deck[-1].did
        did_new=x+1
        
        z = decks(did=did_new, deck_name=deckname_new,deck_description=deck_description_new,cid=cid_new)
        db.session.add(z)
        db.session.commit()

        scores(did_new)

        return{"response":"Creation success!"},200


    def delete(self,did):

        x = decks.query.filter_by(did=did).first()

        if(x==None):
            return{"status":404,
            "message":"Deck doesn't exist"},404
        else:
            db.session.delete(x)
            db.session.commit()
            return {"status":200,'message':"Deletion successful!"},200
    
    def put(self,did):
        args=modify_deck_parser.parse_args()
        deckname_new=args.get("deckname",None)
        cid_new=args.get("cid",None)
        deck_description_new=args.get("deck_description",None)
        deck_score_new=args.get("deck_score",None)
        last_reviewed_new=args.get("last_reviewed",'')

        x = decks.query.filter_by(did=did).first()

        if(x==None):
            return{"status":404,
            "message":"Deck doesn't exist"},404
        
        if deckname_new==None:
            deckname_final=x.deck_name
        else:
            deckname_final=deckname_new
        
        if deck_description_new==None:
            deck_description_final=x.deck_description
        else:
            deck_description_final=deck_description_new

        if cid_new==None:
            cid_final=x.cid
        else:
            cid_final=cid_new
        
        if last_reviewed_new=='':
            last_reviewed_final=x.last_reviewed
        else:
            last_reviewed_final=last_reviewed_new
        
        print(deckname_final,deck_description_final,cid_final,last_reviewed_final)

        x = decks.query.filter_by(did=did).update(dict(deck_name=deckname_final,deck_description=deck_description_final,cid=cid_final,last_reviewed=last_reviewed_final))
        db.session.commit()

        scores(did)

        return{"status":200,"message":"Deck updated successfully!"},200


class CardAPI(Resource):
    def get(self,cid):

        cds = cards.query.filter_by(cid=cid).first()

        if(cds==None):
            return{"status":404,
            "message":"Card doesn't exist"},404
        else:
            return {"cid":cid,
        "obverse":cds.obverse,
        "reverse":cds.reverse,
        "score":cds.score}

    def post(self):

        args=create_card_parser.parse_args()
        obverse_new=args.get("obverse",None)
        reverse_new=args.get("reverse",None)
        score_new=args.get("score",1)

        if(obverse_new==None or reverse_new==None):
            return{"status":400,
            "message":"Data for both card obverse and reverse is mandatory"},400
                
        card = cards.query.all()

        for i in card:
            if i.obverse==obverse_new and i.reverse==reverse_new:
                return{"status":400,"message":"Card already exists!"},400

        x=card[-1].cid
        cid_new=x+1
        
        z = cards(cid=cid_new, obverse=obverse_new,reverse=reverse_new,score=score_new)
        db.session.add(z)
        db.session.commit()

        return{"response":"Creation success!"},200


    def delete(self,cid):

        x = cards.query.filter_by(cid=cid).first()

        if(x==None):
            return{"status":404,
            "message":"Card doesn't exist"},404
        else:
            db.session.delete(x)
            db.session.commit()
            return {"status":200,'message':"Deletion successful!"},200
            
    def put(self,cid):

        args=modify_card_parser.parse_args()
        obverse_new=args.get("obverse",None)
        reverse_new=args.get("reverse",None)
        score_new=args.get("score",1)        

        x = cards.query.filter_by(cid=cid).first()

        if(x==None):
            return{"status":404,
            "message":"Card doesn't exist"},404
        
        if obverse_new==None:
            obverse_final=x.obverse
        else:
            obverse_final=obverse_new

        if reverse_new==None:
            reverse_final=x.reverse
        else:
            reverse_final=reverse_new
        
        score_final=score_new
        

        x = cards.query.filter_by(cid=cid).update(dict(obverse=obverse_final,reverse=reverse_final,score=score_final))
        db.session.commit()

        return{"status":200,"message":"Deck updated successfully!"},200


class UserAPI(Resource):    
    def get(self,username):

        user = User.query.filter_by(username=username).first()

        if(user==None):
            return{"status":404,
            "message":"User doesn't exist"},404
        else:
            return {"uid":user.uid,
        "username":user.username,
        "name":user.name,
        "decks_owned":user.decks_owned}
    
    def delete(self,username):
        
        x = User.query.filter_by(username=username).first()

        if(x==None):
            return{"status":404,
            "message":"User doesn't exist"},404
        else:
            db.session.delete(x)
            db.session.commit()
            return {"status":200,'message':"Deletion successful!"},200

    def post(self):
        args=create_user_parser.parse_args()
        username_new=args.get("username",None)
        name_new=args.get("name",None)
        email_new=args.get("email",None)
        password_new=args.get("password",None)
        decks_owned_new=args.get("decks_owned",'')

        if(username_new==None or name_new==None or email_new==None or password_new==None):
            return{"status":400,
            "message":"Username, email, password and name are mandatory"},400
        
        user = User.query.all()

        for i in user:
            if i.username==username_new:
                return{"status":400,"message":"Username already taken!"},400
            if i.email==email_new:
                return{"status":400,"message":"Email already taken!"},400


        x=user[-1].uid
        uid_new=x+1
        
        #pw=hash_password(password_new)

        #decks_owned=decks_owned_new,

        # z = User(uid=uid_new, username=username_new, name=name_new,email=email_new, password=pw)
        # db.session.add(z)
        # db.session.commit()

        if not user_datastore.find_user(email=email_new):
            user_datastore.create_user(
                username=username_new, name=name_new, email=email_new, password=hash_password(password_new))
            db.session.commit()

        return{"response":"Creation success!"},200

    def put(self,username):
        args=modify_user_parser.parse_args()
        username_new=args.get("username",None)
        name_new=args.get("name",None)
        decks_owned_new=args.get("decks_owned",'')

        x = User.query.filter_by(username=username).first()

        if(x==None):
            return{"status":404,
            "message":"User doesn't exist"},404
        
        if username_new==None:
            username_final=x.username
        else:
            username_final=username_new
        
        if name_new==None:
            name_final=x.name
        else:
            name_final=name_new

        if decks_owned_new=='':
            decks_owned_final=x.decks_owned
        else:
            decks_owned_final=decks_owned_new
        
        x = User.query.filter_by(username=username).update(
		    dict(username=username_final,name=name_final,decks_owned=decks_owned_final))
        db.session.commit()

        return{"status":200,"message":"User updated successfully!"},200
        

class DeckListAPI(Resource):    
    def get(self):

        deck = decks.query.all()

        s=[]
        d={}

        # for i in deck:
        #     s=s+'{did:'+str(i.did)+','+'deck_score:'+str(i.deck_score)+','+'deck_description:'+str(i.deck_description)+','+'last_reviewed:'+str(i.last_reviewed)+'},'
        
        # for i in deck:
        #     s.append([i.did,i.deck_name,i.deck_score,i.deck_description,i.last_reviewed])
        # p=jsonify(s)

        for i in deck:
            d[i.did]=[i.did,i.deck_name,i.deck_score,i.deck_description,i.last_reviewed,convint(i.cid)]

        return d,200

class CardListAPI(Resource):
    def get(self,did):

        # if did==None:
        #     return{"status":400,
        #     "message":"Deck ID missing!"},400

        x = decks.query.filter_by(did=did).first()

        if(x==None):
            return{"status":404,
            "message":"Deck doesn't exist"},404

        p=x.cid

        l=convint(p)

        return l,200

# l=[]
# x = cards.query.all()
# for i in range(len(x)):
#     l.append([x[i].cid,x[i].obverse,x[i].reverse,x[i].score])
# print(l)

class CardListAPIAll(Resource):
    def get(self):

        # if did==None:
        #     return{"status":400,
        #     "message":"Deck ID missing!"},400

        x = cards.query.all()

        l=[]

        for i in range(len(x)):
            l.append([x[i].cid,x[i].obverse,x[i].reverse,x[i].score])


        return l,200

class UserDetailsAPI(Resource):
    def get(self,email):

        x = User.query.filter_by(email=email).first()

        if(x==None):
            return{"status":404,
            "message":"User doesn't exist"},404
        
        return {'username':x.username,'uid':x.uid, 'name':x.name,},200

class ScoreUpdateAPI(Resource):
    def get(self,did):
        scores(did)
        return{"status":200,"message":"Updation complete"},200

# class Test:
#     def get(self):
        
#         return{"status":200,"message":"Updation complete"},200
        

api=Api(app)
api.add_resource(DeckAPI,"/api/v1/deck","/api/v1/deck/<int:did>")
api.add_resource(DeckListAPI,"/api/v1/getdecklist")
api.add_resource(CardListAPIAll,"/api/v1/getallcardlist")
api.add_resource(UserDetailsAPI,"/api/v1/getuser/<string:email>")
api.add_resource(CardListAPI,"/api/v1/getcardlist/<int:did>")
api.add_resource(CardAPI,"/api/v1/card","/api/v1/card/<int:cid>")
api.add_resource(UserAPI,"/api/v1/user","/api/v1/user/<string:username>")
api.add_resource(ScoreUpdateAPI,"/api/v1/updatescore/<int:did>")
# api.add_resource(Test,"/api/v1/test")




# swag = Swagger(api)
# print(swag.as_dict.__doc__)