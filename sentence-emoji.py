#7th edit adds more words, and streamlines the variables


#imports the time module for delays
import time

#these are all of the words that are in the repository, all in different catagories
run=["🏃","run","go","running","ran","walk","walking","walked","jog","jogging","jogged","sprint","sprinting","sprinted"]
hi=["👋","hi","hello","greetings","goodmorning","goodafternoon","whatsup","hey","howdy","hithere","goodday","goodevening","nicetomeetyou"]
late=["🌆","night","evening","late","delayed","behindschedule","tardy","overdue","postponed","deferred","belated","slow","lagging"]
early=["🌅","day","morning","early","aheadoftime","beforehand","premature","prompt","punctual","ontime","sooner","advanced","anticipatory"]
tim=["🕰️","time","hour","minute","second","moment","occasion","period","duration","interval","date","week","month","year","season","era","epoch","age","generation","century","millennium"]
name=["📛","my_name_is","name","my_name","name_is","I_am","I'm","this_is","you_can_call_me","I_go_by","I_introduce_myself_as"]
my=["🧏","my","mine","me","I","i","self","myself","own","personal","individual","private","singular","unique","specific"]
you=["🫵","you","yours","yourself","u","ur","your","thou","thee","thy","thine","ye","y'all","you_guys","you_folks","you_people"]
color=["🌈","rainbow","color","colors","red","green","blue","yellow","black","white","pink","purple","orange","brown"]
animal=["🫎","animals","animal","bird","fish","lion","tiger","elephant","monkey","bear","panda"]
rainbow_flag = ['🏳️‍🌈',"lgbtq+","lgbtq","queer","lesbian","gay","bi","trans","transgender","trans_gender","nonbinary","pride","pride_flag"]
fruit=["🍓","fruit","fruits","apple","banana","orange","grape","strawberry","watermelon","lemon","cherry","mango","pineapple"]
shape=["🔷","shape","shapes","circle","square","triangle","rectangle","pentagon","hexagon","octagon","star","heart","diamond"]
sport=["⚾","sports","sport","soccer","softball","basketball","baseball","tennis","football","hockey","golf","volleyball","cricket","badminton"]
country=["🏴󠁥󠁳󠁰󠁶󠁿","country","countries","usa","china","india","brazil","russia","canada","australia","france","germany","japan"]
food=["🥗","food","dessert","dinner","breakfast","lunch","appetizer","pizza","burger","sushi","salad","pasta","sandwich","soup","cake","ice_cream","chocolate"]
music=["🎼","music","songs","song","rock","pop","jazz","classical","hiphop","country","blues","reggae","metal","folk"]
book=["📖","book","books","read","reading","read","harry_potter","the_lord_of_the_rings","the_hunger_games","the_da_vinci_code","the_catcher_in_the_rye","to_kill_a_mockingbird","nineteen_eighty-four","the_kite_runner","the_girl_with_the_dragon_tattoo","the_chronicles_of_narnia"]
movie=["🎥","movie","movies","the_shawshank_redemption","the_godfather","the_dark_knight","the_lion_king","forrest_gump","titanic","the_matrix","star_wars","the_lord_of_the_rings","inception"]
flower=["🌻","flower","flowers","rose","lily","tulip","orchid","sunflower","daisy","jasmine","lotus","daffodil","lavender"]
planet=["🪐","planet","planets","mercury","venus","earth","mars","jupiter","saturn","uranus","neptune","pluto"]
car=["🚗","car","cars","truck","trucks","toyota","honda","ford","tesla","bmw","audi","hyundai","nissan","chevrolet","volkswagen"]
season=["🍂","season","seasons","spring","summer","autumn","winter"]
today=["📅","today","tomorrow","yesterday","day","calender"]
weather=["☀️","weather","sunny","cloudy","rainy","windy","stormy","foggy","snowy","thunderstorm","hail","drizzle"]
profession=["👩‍⚕️","profession","job","doctor","teacher","engineer","artist","chef","scientist","writer","pilot","firefighter","nurse","lawyer"]
holiday=["🎉","special_day","holiday","christmas","thanksgiving","halloween","easter","valentine's_day","new_year","independence_day","labor_day","hanukkah","diwali"]
hobby=["🎨","hobby","hobbies","for_fun","painting","gardening","photography","playing_an_instrument","cooking","hiking","knitting","dancing","birdwatching"]
beverage=["☕","beverage","coffee","tea","juice","soda","water","smoothie","milkshake","wine","beer","cocktail","lemonade"]
computer=["💻","computer","computers","laptop","laptops","desktop","desktops","python","java","c++","javascript","ruby","swift","rust","php","kotlin","typescript"]
happy=["😀","happy","smile"]
this=["☝️","this","is","are","was"]
star=["⭐","star"]
flame=["🔥","fire","burn","burning"]
look=["👀","look","see","gaze","vision","eye","eyes"]
good=["👍","good","thumbs_up","yeah","yep","yes","definitely","sure","ok"]
bad=["⚠️","bad","warning","notice"]
dog=["🐶","dog","puppy","dogs","puppies"]
cat=["🐱","cat","kitten","cats","kittens"]
down=["👎","no","cant","nope"]
why=["🤷","why","how","when","what","where"]
sleep=["🥱","tired","sleep","sleepy","zzz","asleep","sleeping"]
luck=["🤞","luck","good_luck","hope","cross_your_fingers","hope_so"]
cold=["🥶","cold","freeze","freezing","ice","ice_cube","chilled"]
scared=["😱","scared","terrified","scream","scary","boo","ahh"]
hot=["🥵","hot","fever"]
sick=["🤢","sick","sickly","throwup","throw_up",]
clown=["🤡","clown","clowns","circus"]
disguise=["🥸","disguise","costume"]
robot=["🤖","robot"]
alien=["👽","alien","out_of_this_world","ufo"]
skull=["☠️","skull","skull_and_crossbones","death","poison"]
devil=["😈","devil","hell","evil"]
ear=["👂","listen","hear","ear","listen_up","overhear"]
pumpkin=["🎃","pumpkin","jackolantern","carved_pumpkin","halloween","jack_o_lantern","carvedpumpkin"]
present=["🎁","present","christmas","birthday","gift"]
backpack=["🎒","backpack","bag","totebag","tote_bag","luggage"]
dice=["🎲","dice","die","random","dnd","d&d","ttrpg","rpg","random_number"]
medal=["🥇","reward","medal","award","good_job"]
card=["🃏","card","cards","joker","spades","hearts","diamonds","clubs"]
sun=["☀️","sun","the_sun","light","bright","daytime"]
moon=["🌙","moon","nighttime"]
laughing = ['😂',"laughing","silly","funny"]
crying = ['😭',"crying","cry"]
please = ['🙏',"please","plead"]
nervous = ['😅',"nervous",]
slap = ['🤦',"slap","slap_in_the_face","dang_it","oh_no","not_good","ahh","ah","ahhh"]
rolled = ['🙄',"eyes_rolled","rolled","of_course","sarcastic","sarcasm"]
wink = ['😉',"wink","winking","winked"]
cake = ['🎂',"cake","birthday_cake","treat","surprise"]
thinking = ['🤔',"thinking","thought","hm","hmm","hmmm","interesting","what_if","whatif","however"]
clap = ['👏',"clap","clapping","clapping","claps","great_job","greatjob"]
right = ['👉',"right","go_right","turn_right","look_right"]
onehundred = ['💯',"onehundred","one_hundred","100","100%","hundred"]
mad = ['😡',"mad","frustrated","angry","furious","frown"]
down = ['👇',"down","look_down","turn_down","go_down",]
upsidedown = ['🙃',"silly","upside_down","upsidedown","flipped","flip"]
neutral = ['😐',"neutral","fine"]
peace = ['✌️',"peace","peace_sign"]
sad = ['😞',"sad","upset",]
boom = ['💥',"boom","explosion","explode","crash"]
left = ['👈',"left","go_left","turn_left","look_left"]
wow = ['❗',"wow"]
electricity = ['⚡',"electricity"]
huh = ['🤨',"huh","huh?","suspicious","sus",""]
monocle = ['🧐',"monocle"]
paint = ['👩‍🎨',"painter","paint","paints","artist","art","draw"]
siren = ['🚨',"siren","sirens","lights_and_sirens"]
tv = ['📺',"tv","television","show"]
phone = ['📱',"phone","telephone","smartphone","smart_phone","call","ring"]
camera = ['📷',"camera","picture","photo","photographer"]
mushroom = ['🍄',"mushroom","mushrooms","shroom","fungi","fungus"]
chocolate = ['🍫',"chocolate","sweets","sweet","treat","sweet_treat"]
guitar_not_really = ['🎸',"guitar","bass","electric_guitar","acoustic_guitar"]
headphones = ['🎧',"headphones","headphone","earbud","earbuds","listen_to"]
mind_blown = ['🤯',"mind_blown","head_exploded","head_explode"]
mask = ['😷',"covid","mask","pandemic"]
rocket = ['🚀',"rocket","space"]
plant = ['🌱',"plant","seedling","plants","garden"]
plane = ['✈️',"plane","planes","fly"]
trophy = ['🏆',"trophy"]
printer = ['🖨️',"printer","print","evil_machine","does_not_work"]
mailbox = ['📭',"mailbox","mail_box","mail","message"]
cabinet = ['🗄️',"cabinet","drawer","storage","storage_space","cabinets","storagespace"]


#this list links back to all of the other lists, to automate the checking process               
checks = [
    run,
    hi,
    late,
    early,
    tim,
    name,
    my,
    you,
    color,
    animal,
    fruit,
    shape,
    sport,
    country,
    food,
    music,
    book,
    movie,
    flower,
    planet,
    car,
    season,
    today,
    weather,
    profession,
    holiday,
    hobby,
    beverage,
    computer,
    happy,
    this,
    star,
    flame,
    look,
    good,
    bad,
    dog,
    cat,
    down,
    why,
    sleep,
    luck,
    cold,
    scared,
    hot,
    sick,
    clown,
    disguise,
    robot,
    alien,
    skull,
    devil,
    ear,
    pumpkin,
    present,
    backpack,
    dice,
    medal,
    card,
    sun,
    moon,
    laughing,
    crying,
    please,
    nervous,
    slap,
    rolled,
    wink,
    cake,
    thinking,
    clap,
    right,
    onehundred,
    mad,
    down,
    upsidedown,
    neutral,
    peace,
    sad,
    boom,
    left,
    wow,
    rainbow_flag,
    electricity,
    huh,
    monocle,
    paint,
    siren,
    tv,
    phone,
    camera,
    mushroom,
    chocolate,
    guitar_not_really,
    headphones,
    mind_blown,
    mask,
    rocket,
    plant,
    plane,
    trophy,
    printer,
    mailbox,
    cabinet
]


#Word in input sentence
WordInInput = 0

#checking the number of lists
ListCheck = len(checks)

#number of lists -1 is num_of
NumOfLists = ListCheck - 1

#Input sentence
Input = input("Please Type In A Sentence,  ")

#Providing information when "help" is put into input sentence
if Input.lower() == "help":
    print("If There Are Spaces In One Thing Like 'New Year' Use _ Instead 'New_Year'")
    time.sleep(3)
    exit()

#splitting the input sentence into a list
Sentence = Input.split()

#checking how many words are in the sentence list
NumOfWords = len(Sentence)


def emoji(
    
):
    #list that the list checks is reffering back to
    ListSelector = 0
    
    #infinite loop
    while 1 < 5:
        
        #if the word in question (chosen by the "a" variable) is in the list that "checks" "ListSelector" is referring back to, 
        if Sentence[WordInInput].lower() in checks[ListSelector]:
        
            # print the first entry of that list
            print(checks[ListSelector][0])
            break
        
        else:
            #otherwise either stop if that was the last list in the repository
            if ListSelector == NumOfLists:
                break
            #or add one to "ListSelector" to change what list it is checking
            else:
                ListSelector += 1

    
    
#check_num is just another loop
Loop = 0

#this checks to see if the last check was the last word in the sentence, and if not, keep checking the next words
while Loop < 9:    
    emoji()
    WordInInput += 1
    if WordInInput == NumOfWords:
        break

#This allows you to exit the program without pressing a ctl-c type of shortcut
y = input()

if y.lower() == "":
    exit()
else:
    exit()
