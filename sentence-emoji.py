import time
run = ["🏃","run", "running", "ran", "walk", "walking", "walked", "jog", "jogging", "jogged", "sprint", "sprinting", "sprinted"]
hi = ["👋","hi", "hello", "greetings", "good morning", "good afternoon", "whats up", "hey", "howdy", "hi there", "good day", "good evening", "nice to meet you"]
late = ["🌆","late", "delayed", "behind schedule", "tardy", "overdue", "postponed", "deferred", "belated", "slow", "lagging"]
early = ["🌅","early", "ahead of time", "beforehand", "premature", "prompt", "punctual", "on time", "sooner", "advanced", "anticipatory"]
tim = ["🕰️","time", "hour", "minute", "second", "moment", "occasion", "period", "duration", "interval", "date", "day", "week", "month", "year", "season", "era", "epoch", "age", "generation", "century", "millennium"]
name = ["📛","my_name_is", "name", "my_name", "name_is", "I_am", "I'm", "this_is", "you_can_call_me", "I_go_by", "I_introduce_myself_as"]
my = ["🧏","my", "mine", "me", "I", "i", "self", "myself", "own", "personal", "individual", "private", "singular", "unique", "specific"]
you = ["🫵","you", "yours", "yourself", "u", "ur", "your", "thou", "thee", "thy", "thine", "ye", "y'all", "you_guys", "you_folks", "you_people"]
color = ["🏳️‍🌈","color","colors","red", "green", "blue", "yellow", "black", "white", "pink", "purple", "orange", "brown"]
animal = ["🫎","animals","animal","dog", "cat", "bird", "fish", "lion", "tiger", "elephant", "monkey", "bear", "panda"]
fruit = ["🍓","fruit","fruits","apple", "banana", "orange", "grape", "strawberry", "watermelon", "lemon", "cherry", "mango", "pineapple"]
shape = ["🔷","shape","shapes","circle", "square", "triangle", "rectangle", "pentagon", "hexagon", "octagon", "star", "heart", "diamond"]
sport = ["⚾","sports","sport","soccer", "softball", "basketball", "baseball", "tennis", "football", "hockey", "golf", "volleyball", "cricket", "badminton"]
country = ["🏴󠁥󠁳󠁰󠁶󠁿","country","countries","USA", "China", "India", "Brazil", "Russia", "Canada", "Australia", "France", "Germany", "Japan"]
food = ["🥗","food","dessert","dinner","breakfast","lunch","appitizer","pizza", "burger", "sushi", "salad", "pasta", "sandwich", "soup", "cake", "ice_cream", "chocolate"]
music = ["🎵","music","songs","song", "rock", "pop", "jazz", "classical", "hip hop", "country", "blues", "reggae", "metal", "folk"]
book = ["📖","book","books","Harry_Potter", "The_Lord_of_the_Rings", "The_Hunger_Games", "The_Da_Vinci_Code", "The_Catcher_in_the_Rye", "To_Kill_a_Mockingbird", "Nineteen_Eighty-Four", "The_Kite_Runner", "The_Girl_with_the_Dragon_Tattoo","The_Chronicles_of_Narnia"]
movie = ["🎥","movie", "movies", "The_Shawshank_Redemption", "The_Godfather", "The_Dark_Knight", "The_Lion_King", "Forrest_Gump", "Titanic", "The_Matrix", "Star_Wars", "The_Lord_of_the_Rings", "Inception"]
flower = ["🌻","flower","flowers","rose", "lily", "tulip", "orchid", "sunflower", "daisy", "jasmine", "lotus", "daffodil", "lavender"]
planet = ["🪐","planet","planets","Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
car = ["🚗","car","cars","truck","trucks","Toyota", "Honda", "Ford", "Tesla", "BMW", "Audi", "Hyundai", "Nissan", "Chevrolet", "Volkswagen"]
season = ["🍂","season","seasons","spring", "summer", "autumn", "winter"]
today = ["📅","today","tommorow","yesterday","day"]
weather = ["☀️", "sunny", "cloudy", "rainy", "windy", "stormy", "foggy", "snowy", "thunderstorm", "hail", "drizzle"]
profession = ["👩‍⚕️","proffesion","job", "doctor", "teacher", "engineer", "artist", "chef", "scientist", "writer", "pilot", "firefighter", "nurse", "lawyer"]
holiday = ["🎉","special_day", "holiday", "Christmas", "Thanksgiving", "halloween", "easter", "valentine's_day", " new_year", "independence_day", "labor_day", "hanukkah", "diwali"]
hobby = ["🎨","hobby","hobbies","for_fun", "painting", "gardening", "photography", "playing_an_instrument", "cooking", "hiking", "knitting", "dancing", "birdwatching"]
beverage = ["☕","beverage", "coffee", "tea", "juice", "soda", "water", "smoothie", "milkshake", "wine", "beer", "cocktail", "lemonade"]
computer = ["💻", "computer","computers","laptop","laptops","desktop","desktops","python", "java", "c++", "javascript", "ruby", "go", "swift", "rust", "php", "kotlin", "typescript"]

a = 0

s = input("Please Type In A Sentence, If There Are Spaces In One Thing Like 'New Year' Use _ Instead 'New_Year'  ")
l = s.split()
list = l
print(list)
how_many = len(list)

def test(
    
):

    if list[a].lower() in season: 
        print(season[0])
    
        
   
    elif list[a].lower() in car:
        print(car[0])
    
        
    
    elif list[a].lower() in planet:
        print(planet[0])
    
         
   
    elif list[a].lower() in flower:
        print(flower[0])
    
          
   
    elif list[a].lower() in movie:
        print(movie[0])
    
            
    
    elif list[a].lower() in book:
        print(book[0])
    
            
   
    elif list[a].lower() in music:
        print(music[0])
    
            
   
    elif list[a].lower() in food:
        print(food[0])
    
            
  
    elif list[a].lower() in country:
        print(country[0])
    
        
   
    elif list[a].lower() in sport:
        print(sport[0])
    
        
   
    elif list[a].lower() in shape:
        print(shape[0])
    
        
    
    elif list[a].lower() in fruit:
        print(fruit[0])
    
        
   
    elif list[a].lower() in animal:
        print(animal[0])
    
        
   
    elif list[a].lower() in color:
        print(color[0])
    
        
   
    elif list[a].lower() in you:
        print(you[0])
    
        
   
    elif list[a].lower() in my:
        print(my[0])
    
        
   
    elif list[a].lower() in name:
        print(name[0])
    
        
   
    elif list[a].lower() in tim:
        print(tim[0])
    
        
   
    elif list[a].lower() in early:
        print(early[0])
    
        
   
    elif list[a].lower() in late:
        print(late[0])
    
        
   
    elif list[a].lower() in hi:
        print(hi[0])
    
        
   
    elif list[a].lower() in run:
        print(run[0])
    
    
    elif list[a].lower() in today:
        print(today[0])
        
        
    elif list[a].lower() in profession:
        print(profession[0])
        
    
    elif list[a].lower() in holiday:
        print(holiday[0])
        
    
    elif list[a].lower() in hobby:
        print(hobby[0])
        
        
    elif list[a].lower() in beverage:
        print(beverage[0])
        
        
    elif list[a].lower() in computer:
        print(computer[0])
            
        
    else:
        print("?")
   
   
    time.sleep(1)
    


check_num = 0
while check_num < 9:    
    test()
    a += 1
    if a == how_many:
        break


print("Complete")
