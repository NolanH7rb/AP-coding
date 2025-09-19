#DAY !
# Object breakdown
   #An object is a contruct for story data(booleans, strings, etc) and functions together.
   # self = class
class instaProfile:
    def __init__(self, username, email, profileImg, passWord, bio):
        self.username = username
        self.email = email
        self.profileImg = profileImg
        self.passWord = passWord
        self.bio = bio
    def printInfo(self):
        print('username' + self.username,)

    def resetpassWord(self):
        print('2-step auth...')

    def uploadPicture(self):
        print('instructions')

    def viewFollowers(self):
        print(['list of other followers'])

profile1 = instaProfile('Nolan','nhall255@boyslatin.net','pic.png','Golddust44','Im just an athlete',)
profile2 = instaProfile('Danny','dannyghost99@yahoo,com','pic.png','doggwhip88','DAN THE MAN')
#instaProfile.printInfo()

#DAY 2
 #Notes
 #[When creating an object we start with the vlass keyword,
 #this acts like out object maker/ our blueprint]
class CarMaker:
    def __init__(self, name, color, seating, year, model , miles): #initializes the blueprint
        self.name = name
        self.color = color
        self.seating = seating
        self.year = year
        self.model = model
        self.miles = miles

    def printInfo(self):
        print('heres your car FAQS')
        print('name:   '+ self.name)
        print('year:   '+ str(self.year))
        print('miles:  '+ str(self.miles))
        print('color:  '+ str(self.color))
        print('seating:  '+ str(self.seating))

    def windshieldwippers(self):
        print('when raining turn on')

    def airbag(self):
        print(' when driving a certain spped and a collision occurs; open')

    def turnsignals(self, up, down):
        if up == 1 :
           print("turn left")
        elif down == -1:
            print("turn right")
        else:
            print("dont turn signals on")

    def bluetooth(year):
        if year > 2020:
            print('you have bluetooth')
        else:
            print("no bluetooth on this model")
carOption1 = CarMaker('Carolla', 'Black','4','2024','car','38k')
print(carOption1) #shows the location in computer memory

carOption1.printInfo() # shows me actual data


#DAY 3
class PhoneCompany:
    def __init__(self, name, Model, color, Gb,): #initializes the blueprint
        self.name = name
        self.Model = Model
        self.color = color
        self.Gb = Gb
        self.call = '267-777-3467'

    def callPhone(self):
        numberOfAttempts = 0
        attempts = 3 
        while numberOfAttempts < attempts:
            print("ring, rimg, ring...")
            print(self.call)     
            input('do you want to accept or decline? ')

            if 'yes':
                print('connecting call.')

            else:
                numberOfAttempts +1

            if attempts < 3:
                print("declined")

    def printInfo(self):
        print('heres your phone FAQS')
        print('name:   '+ self.name)
        print('Model:   '+ str(self.Model))
        print('Color:  '+ str(self.color))
        print('GigaBytes:  '+ str(self.Gb))

PhoneA = PhoneCompany ('Iphone Xr','10th Gen','Space Grey','144Gb')

PhoneA.callPhone()

