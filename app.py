import random
import string

def generate_user(max_length=10):
  """Generates a user with random data for each field."""
 
  # Define first and last name options
  first_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Jack", "Karl", "Linda", "Mike", "Nancy", "Oscar", "Paul", "Quincy", "Ruth", "Steve", "Tina", "Ursula", "Victor", "Wendy", "Xavier", "Yvonne", "Zack"]
  last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson", "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes", "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez", "Powell", "Jenkins", "Perry", "Russell", "Sullivan", "Bell", "Cole", "Butler", "Henderson", "Barnes", "Gonzales", "Fisher", "Vasquez", "Simmons", "Romero", "Jordan", "Patterson", "Alexander", "Hamilton", "Graham", "Reynolds", "Griffin", "Wallace", "Moreno", "West", "Coleman", "Hayes", "Bryant", "Herrera", "Gibson", "Ellis", "Tran", "Medina", "Luna", "Sims", "Kennedy", "Wells", "Alvarez", "Woods", "Mendoza", "Castillo", "Olson", "Webb"]

  # Define domain options
  domain_options = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "icloud.com", "aol.com", "protonmail.com", "zoho.com", "yandex.com", "mail.com"]

  # Define city options
  city_options = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "San Francisco", "Indianapolis", "Columbus", "Fort Worth", "Charlotte", "Seattle", "Denver", "El Paso", "Detroit", "Washington", "Boston", "Memphis", "Nashville", "Portland", "Oklahoma City", "Las Vegas", "Baltimore", "Louisville", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Mesa", "Kansas City", "Atlanta", "Long Beach", "Omaha", "Raleigh", "Miami", "Oakland", "Minneapolis", "Tulsa", "Cleveland", "Wichita", "Arlington", "New Orleans", "Bakersfield", "Tampa", "Honolulu", "Aurora", "Anaheim", "Santa Ana", "St. Louis", "Riverside", "Corpus Christi", "Lexington", "Pittsburgh", "Anchorage", "Stockton", "Cincinnati", "St. Paul", "Toledo", "Greensboro", "Newark", "Plano", "Henderson", "Lincoln", "Buffalo", "Fort Wayne", "Jersey City", "Chula Vista", "Orlando", "St. Petersburg", "Norfolk", "Chandler", "Laredo", "Madison", "Durham", "Lubbock", "Winston-Salem", "Garland", "Glendale", "Hialeah", "Reno", "Baton Rouge", "Irvine", "Chesapeake", "Irving", "Scottsdale", "North Las Vegas", "Fremont", "Gilbert", "San Bernardino", "Boise", "Birmingham", "Richmond", "Spokane", "Des Moines", "Montgomery", "Modesto", "Fayetteville", "Tacoma", "Shreveport", "Fontana", "Oxnard", "Aurora", "Moreno Valley", "Akron", "Yonkers", "Columbus", "Augusta", "Little Rock", "Amarillo", "Mobile", "Huntington Beach", "Glendale", "Grand Rapids", "Salt Lake City", "Tallahassee"]

  # Define street options
  street_options = ["Main St", "Elm St", "Oak St", "Maple St", "Pine St", "Cedar St", "Washington St", "Church St", "North St", "South St", "Park St", "High St", "Central St", "School St", "Pleasant St", "Grove St", "River St", "Franklin St", "Pearl St", "Water St", "Union St", "Bridge St", "State St", "Broadway", "Chestnut St", "Market St", "Mill St", "Spruce St", "Front St", "Adams St", "Liberty St", "Spring St", "Court St", "Prospect St", "Meadow St", "Locust St", "Hill St", "Madison St", "Vine St", "Lincoln St", "Jefferson St", "Madison St", "Hillside Ave", "Sunset Dr", "Forest Ave", "Crescent St", "Pleasant Ave", "Cottage St", "Laurel St", "Ridge St", "Highland Ave", "Beech St", "Columbia St", "Harrison St", "Hickory St", "Chestnut St", "Cedar Ave", "Lake St", "Pleasant St", "Riverside Dr", "Broad St", "Hillside Ave", "Pine St", "Hillcrest Ave", "Cedar St", "Crescent St", "Hill St", "Hillcrest Ave"]

  # Generate random ID
  id = random.randint(1, max_length)

  # Generate random email
  first_name = random.choice(first_names)
  last_name = random.choice(last_names)
  domain = random.choice(domain_options)
  email = f"{first_name.lower()}.{last_name.lower()}@{domain}"

  # Generate random document (replace with your document format logic)
  document = f"{random.randint(10000000, 99999999)}-{random.randint(1000, 9999)}"

  # Generate random phone number (replace with your phone number format logic)
  phone = f"+1 ({random.randint(100, 999)}) {random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

  # Generate random full name
  full_name = f"{first_name} {last_name}"

  # Generate random address
  street = random.choice(street_options)
  city = random.choice(city_options)
  address = f"{street}, {city}"

  return {"id": id, "email": email, "document": document, "phone": phone, "fullname": full_name, "address": address}


def sendToRedis(user):
    import redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set(user['id'], user)
    print(f"User {user['id']} sent to Redis")


if __name__ == "__main__":
  max_length = 10
  for _ in range(max_length):
    user = generate_user(max_length)
    print(user)

    sendToRedis(user)
