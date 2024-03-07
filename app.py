import random
import string
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, NumericField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType

from data import names_options, surnames_options, domain_options, city_options, street_options, document_type_options, person_type_options

def generate_user(max_length=10):
     # Generate random ID
    id = random.randint(1, max_length)

    # Generate random first and last name
    first_name = random.choice(names_options)
    last_name = random.choice(surnames_options)

    # Generate random full name
    full_name = f"{first_name} {last_name}"

    # Generate random email
    domain = random.choice(domain_options)
    email = f"{first_name.lower()}.{last_name.lower()}_{id}@{domain}"

    # Generate random document
    document = f"{random.randint(1000000, 9999999999)}"

    # Generate random phone id
    phone_id = random.randint(1, max_length)

    # Generate random phone number
    phone = f"+57{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(1000, 9999)}"

    # Generate random address
    street = random.choice(street_options)
    city = random.choice(city_options)
    address = f"{street}, {city}"

    billing_data = {
        "id": random.randint(1, max_length),
        "names": first_name,
        "surnames": last_name,
        "email": email,
        "phone": phone,
        "address": address,
        "document": document,
        "responsibility_rent": random.randint(1, 2),
        "responsibility_vat": random.randint(1, 2),
        "person_type_id": random.randint(1, 3),
        "person_type": random.choice(person_type_options),
        "document_type_id": random.randint(1, 4),
        "document_type": random.choice(document_type_options),
    }

    # Generate random membership
    membership = None
    if id % 2 == 0:
        membership = {
            "id": random.randint(1, 9),
            "name": random.choice(["Basic", "Premium", "Gold", "Platinum", "Diamond"]),
            "discount": random.randint(5, 20)
        }

    # Generate random flags
    is_member = membership is not None
    is_locked = random.choice([True, False])
    is_cached = random.choice([True, False])

    return {"id": id, "email": email, "document": document, "phone": phone, "fullname": full_name, "address": address, "billing_data": billing_data, "membership": membership, "is_member": is_member, "is_locked": is_locked, "is_cached": is_cached}


def sendToRedis(r, user):    
    index = "user:" + str(user["id"])
    r.json().set(index, Path.root_path(), user)
    print(f"User {user['id']} sent to Redis")



if __name__ == "__main__":
    max_length = 4000000
    r = redis.Redis(host='localhost', port=6379)
    idx = "idx:customers"

    # Drop index idx:customers if exists
    try:
        r.execute_command('FT.DROPINDEX', idx)
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Index idx:customers not found")
    else:
        print(f"Index idx:customers dropped")

    # Create index idx:customers
    try:
        r.execute_command('FT.CREATE', idx, 'ON', 'HASH', 'PREFIX', '1', 'user:', 'SCHEMA', 'id', 'NUMERIC', 'email', 'TEXT', 'phone', 'TEXT', 'document', 'TEXT', 'fullname', 'TEXT', 'billing_data.names', 'TEXT', 'billing_data.surnames', 'TEXT', 'billing_data.email', 'TEXT', 'billing_data.phone', 'TEXT', 'billing_data.address', 'TEXT', 'billing_data.document', 'TEXT', 'billing_data.responsibility_rent', 'NUMERIC', 'billing_data.responsibility_vat', 'NUMERIC', 'billing_data.person_type_id', 'NUMERIC', 'billing_data.person_type', 'TEXT', 'billing_data.document_type_id', 'NUMERIC', 'billing_data.document_type', 'TEXT', 'membership.id', 'NUMERIC', 'membership.name', 'TEXT', 'membership.discount', 'NUMERIC', 'is_member', 'TAG', 'is_locked', 'TAG', 'is_cached', 'TAG', 'membership.name', 'TAG', 'membership.discount', 'NUMERIC', 'is_member', 'TAG', 'is_locked', 'TAG', 'is_cached', 'TAG')
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Index idx:customers not created")
    else:
        print(f"Index idx:customers created") 

    # Send data to Redis
    for _ in range(max_length):
        try:
            user = generate_user(max_length)
            index = "customers:" + str(user["id"])
            r.json().set(index, Path.root_path(), user)

        except Exception as e:
            print(f"An error occurred: {e}")
            print(f"User {user['id']} not sent to Redis")
        else:           
            print(user)
            print(f"User {user['id']} sent to Redis")



