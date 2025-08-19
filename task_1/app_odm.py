import argparse
from mongoengine import connect, Document, StringField, IntField, ListField
from bson.objectid import ObjectId
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

uri = "mongodb+srv://evemode:some_password@cluster0.1dv5tt5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
connect(db='ElCato', host=uri)
# Create a new client and connect to the server

parser = argparse.ArgumentParser(description='Cats Entertainment')
parser.add_argument('--action', help='create, read, update, delete')
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age')
parser.add_argument('--features', nargs='+')

arg = vars(parser.parse_args())

action = arg.get('action')
pk = arg.get('id')
namne = arg.get('name')
age = arg.get('age')
features = arg.get('features')


class Cat(Document):
    name = StringField(max_length=120, required=True)
    age = IntField(min_value=1, max_value=15)
    features = ListField(StringField(max_length=150))
    meta = {'collection': 'cats'}
    
def find():
    return Cat.objects.all()
    
def create(name, age, features):
    r = Cat(name=name, age=age, features=features)
    r.save()
    return r

def update(pk, name, age, features):
    cat = Cat.objects(id=pk)
    if cat:
        cat.update(name=name, age=age, features=features)
        cat.reload()
    return cat

def delete(pk):
    try:
        cat = Cat.object.get(id=pk)
        cat.delete()
        return cat
    except DoesNotExist:
        return None


def main():
    match action:
        case 'create':
            r = create(name, age, features)
            print(r.to_mongo().to_dict())
            
        case 'read':
            r = find()
            print([e.to_mongo().to_dict() for e in r])
        
        case 'update':
            r = update(pk, name, age, features)
            if r:
                print(r)
        case 'delete':
            r = delete(pk)
            if r:
                print(r)
        case _:
            print('Unknown command')
            

if __name__ == '__main__':
    main()
