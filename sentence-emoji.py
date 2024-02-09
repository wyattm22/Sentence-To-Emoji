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
animal = ["🫎","animals","animal", "bird", "fish", "lion", "tiger", "elephant", "monkey", "bear", "panda"]
fruit = ["🍓","fruit","fruits","apple", "banana", "orange", "grape", "strawberry", "watermelon", "lemon", "cherry", "mango", "pineapple"]
shape = ["🔷","shape","shapes","circle", "square", "triangle", "rectangle", "pentagon", "hexagon", "octagon", "star", "heart", "diamond"]
sport = ["⚾","sports","sport","soccer", "softball", "basketball", "baseball", "tennis", "football", "hockey", "golf", "volleyball", "cricket", "badminton"]
country = ["🏴󠁥󠁳󠁰󠁶󠁿","country","countries","usa", "china", "india", "brazil", "russia", "canada", "australia", "france", "germany", "japan"]
food = ["🥗","food","dessert","dinner","breakfast","lunch","appetizer","pizza", "burger", "sushi", "salad", "pasta", "sandwich", "soup", "cake", "ice_cream", "chocolate"]
music = ["🎵","music","songs","song", "rock", "pop", "jazz", "classical", "hip hop", "country", "blues", "reggae", "metal", "folk"]
book = ["📖","book","books","harry_potter", "the_lord_of_the_rings", "the_hunger_games", "the_da_vinci_code", "the_catcher_in_the_rye", "to_kill_a_mockingbird", "nineteen_eighty-four", "the_kite_runner", "the_girl_with_the_dragon_tattoo","the_chronicles_of_narnia"]
movie = ["🎥","movie", "movies", "the_shawshank_redemption", "the_godfather", "the_dark_knight", "the_lion_king", "forrest_gump", "titanic", "the_matrix", "star_wars", "the_lord_of_the_rings", "inception"]
flower = ["🌻","flower","flowers","rose", "lily", "tulip", "orchid", "sunflower", "daisy", "jasmine", "lotus", "daffodil", "lavender"]
planet = ["🪐","planet","planets","mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]
car = ["🚗","car","cars","truck","trucks","toyota", "honda", "ford", "tesla", "bmw", "audi", "hyundai", "nissan", "chevrolet", "volkswagen"]
season = ["🍂","season","seasons","spring", "summer", "autumn", "winter"]
today = ["📅","today","tommorow","yesterday","day"]
weather = ["☀️", "sunny", "cloudy", "rainy", "windy", "stormy", "foggy", "snowy", "thunderstorm", "hail", "drizzle"]
profession = ["👩‍⚕️","proffesion","job", "doctor", "teacher", "engineer", "artist", "chef", "scientist", "writer", "pilot", "firefighter", "nurse", "lawyer"]
holiday = ["🎉","special_day", "holiday", "christmas", "thanksgiving", "halloween", "easter", "valentine's_day", " new_year", "independence_day", "labor_day", "hanukkah", "diwali"]
hobby = ["🎨","hobby","hobbies","for_fun", "painting", "gardening", "photography", "playing_an_instrument", "cooking", "hiking", "knitting", "dancing", "birdwatching"]
beverage = ["☕","beverage", "coffee", "tea", "juice", "soda", "water", "smoothie", "milkshake", "wine", "beer", "cocktail", "lemonade"]
computer = ["💻", "computer","computers","laptop","laptops","desktop","desktops","python", "java", "c++", "javascript", "ruby", "go", "swift", "rust", "php", "kotlin", "typescript"]
happy = ["😀","happy","smile","laugh"]
this = ["☝️","this","is","are","was","what"]
star = ["⭐","star"]
flame = ["🔥","fire"]
look = ["👀","look","see","gaze","vision","eye","eyes"]
good = ["👍","good","thumbs_up","yeah","yep","yes","definitly","sure"]
bad = ["⚠️","bad","warning","notice"]
dog = ["🐶","dog","puppy","dogs","puppies"]
cat = ["🐱","cat","kitten","cats","kittens"]
down = ["👎","no","cant","nope"]


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
            
            
    elif list[a].lower() in happy:
        print(happy[0])
        
        
    elif list[a].lower() in this:
        print(this[0])
        
        
    elif list[a].lower() in star:
        print(star[0])
        
        
    elif list[a].lower() in flame:
        print(flame[0])
        
        
    elif list[a].lower() in look:
        print(look[0])
        
        
    elif list[a].lower() in good:
        print(good[0])
        
        
    elif list[a].lower() in bad:
        print(bad[0])
        
        
    elif list[a].lower() in dog:
        print(dog[0])
        
        
    elif list[a].lower() in cat:
        print(cat[0])
        
        
    elif list[a].lower() in down:
        print(down[0])
        
    else:
        print("?")
   
   
    time.sleep(.05)
    


check_num = 0
while check_num < 9:    
    test()
    a += 1
    if a == how_many:
        break


print("Complete")
