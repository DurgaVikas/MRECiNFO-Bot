from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("2113561298:AAF84TUgXZkZJjXvpXAh90uWxblg4bGilxM",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello sir, Welcome to the MRECiNfo Bot.Please write\
		/help to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/BlockInfo
	/DepartmentInfo
	/StaffInfo""")


def BlockInfo(update: Update, context: CallbackContext):
	update.message.reply_text("""/Humanites_and_Sciences
	           /Knowledge_Resource_Centre 
	           /Admin_Block
	           /Mechanical_and_Mining_Engineering_Block
	           /CSE_Block
	           /Civil_Engineering_Block
	           /MBA_Block
	           /Pharmacy_Block""")

	
def Humanites_and_Sciences(update: Update, context: CallbackContext):
	         update.message.reply_text(" This Block Consists of B.Tech\
 First Year Students and their respective Faculty members. To Know more /help")

	         
def Knowledge_Resource_Centre(update: Update, context: CallbackContext):
	         update.message.reply_text(" This Block Consists of Library\
 and Computer Labs,To Know more /help")

	         
def Admin_Block(update: Update, context: CallbackContext):
	         update.message.reply_text(" This Block Consists of B.Tech\
 ECE,EEE Students and Faculty. It has Admistration office and Examination Cell where you can pay\
 your fees and ask fees and Exams related queries. To Know more /help")


def Civil_Engineering_Block(update: Update, context: CallbackContext):
	         update.message.reply_text(" This Block Consists of B.Tech\
 Civil Engineering Students and their respective Faculty members. To Know more /help")
	         
def Mechanical_and_Mining_Engineering_Block(update: Update, context: CallbackContext):
	         update.message.reply_text(" This Block Consists of B.Tech\
 Mechanical and Mining Engineering Students and their respective Faculty members. To Know more /help")
	         
def CSE_Block(update: Update, context: CallbackContext):
	         update.message.reply_text("""This Block Consists of B.Tech\
 CSE Students and their respective Faculty members. To Know more /help
 /Ground_floor\n 
 /First_floor\n   
 /Second_floor\n 
 /Third_floor\n 
 /Fourth_floor\n 
 """)

def Ground_floor(update: Update, context: CallbackContext): 
	         update.message.reply_text("""Ground floor:\n 
 ROOM.NO-G01: Java Programming Lab\n 
 ROOM.No-G02: Operating Systems Lab\n 
 ROOM.No-G03: Python Programming Lab\n 
 ROOM.No-G05: Big Data Analysis Lab\n 
 ROOM.NO-G06: Data Mining Lab\n 
 ROOM.No-G07: Project Lab\n 
 ROOM.NO-G04: Gent's Washroom\n""")  
 
def First_floor(update: Update, context: CallbackContext):
	         update.message.reply_text("""First Floor:\n 
 ROOM.NO-101: HOD Cabin\n 
 ROOM.NO-102: Conference room\n 
 ROOM.NO-103: Class room\n 
 ROOM.NO-104: Class room\n 
 ROOM.NO-105: Girl's Waiting Hall\n 
 ROOM.NO-107: Staff room\n 
 ROOM.NO-108: Class room\n 
 ROOM.NO-109: Research and Development Lab\n 
 ROOM.NO-110: Staff room\n
 ROOM.NO-106: Ladie's Washroom\n""")
 
def Second_floor(update: Update, context: CallbackContext):
	         update.message.reply_text("""Second Floor:\n 
 ROOM.NO-201: Ladie's Staff room\n 
 ROOM.NO-202: Class room\n 
 ROOM.NO-203: Class room\n 
 ROOM.NO-204: Class room\n 
 ROOM.NO-206: Class room\n 
 ROOM.NO-207: Class room\n 
 ROOM.NO-208: Class room\n 
 ROOM.NO-205: Gent's Washroom\n""")

def Third_floor(update: Update, context: CallbackContext):
	         update.message.reply_text("""Third Floor:\n 
 ROOM.NO-301: Staff room\n 
 ROOM.NO-302: Class room\n 
 ROOM.NO-303: Class room\n 
 ROOM.NO-304: Computer Network Lab\n 
 ROOM.NO-305: Class room\n
 ROOM.NO-306: English Lab\n 
 ROOM.NO-307: P.G Class room\n""")
 
def Fourth_floor(update: Update, context: CallbackContext):
	         update.message.reply_text("""Fourth Floor:\n 
 ROOM.NO-401: Data Structures Advanced Lab\n 
 ROOM.NO-402: Seminar Hall\n 
 ROOM.NO-404: Data Base Managament Lab\n 
 ROOM.NO-405: Data Base Managament Lab\n 
 ROOM.NO-406: Design and Analysis of Algorithums Lab\n
 ROOM.NO-403: Gent's Washroom\n""")
 
def MBA_Block(update: Update, context: CallbackContext):
	         update.message.reply_text(" This Block Consists of \
MBA Students and their respective Faculty members. To Know more /help")

	         
def Pharmacy_Block(update: Update, context: CallbackContext):
	         update.message.reply_text(" This Block Consists of \
Pharmacy Students and their respective Faculty members. To Know more /help")

def DepartmentInfo(update: Update, context: CallbackContext):
	update.message.reply_text("""/CSE
	           /Mechanical
	           /Mining
	           /IT
	           /Civil
	           /ECE
	           /EEE
	           /MBA
	           /Pharmacy""")
	           
def CSE(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def Mechanical(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def Mining(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def IT(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def EEE(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def ECE(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def MBA(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def Pharmacy(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def Civil(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)

def StaffInfo(update: Update, context: CallbackContext):
	update.message.reply_text("""/UG_Staff
	/PG_Staff
	/Admin_Staff
	/Sports_Staff""")

def UG_Staff(update: Update, context: CallbackContext):
	update.message.reply_text("""
	/CSE_STAFF
	/CSE_STAFF_A
	/CSE_STAFF_B
	/CSE_STAFF_C
	/CSE_STAFF_D
	/CSE_CS
	/CSE_AI
	/CSE_DS
	/CSE_IOT
	/IT_STAFF
	/ECE_STAFF
	/EEE_STAFF
	/CIVIL_ENGG
	/MECHANICAL_ENGG 
	/MINING_ENGG
	/PHARMACY_STAFF""")
	
def PG_Staff(update: Update, context: CallbackContext):
	update.message.reply_text("""/MACHINE_DESING
	/ELECTRICAL_POWER_SYSTEMS
	/STRUCTURAL_ENGINEERING
	/THERMAL_ENGINEERING
	/CSE_PG
	/VLSI_AND_EMBEDDED_SYSTEMS
	/MBA_STAFF""")
	
def Admin_Staff(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def Sports_Staff(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)	
	
def CSE_STAFF(update: Update, context: CallbackContext):
	update.message.reply_text("""Name: Dr.N.LakshmiPathi Anantha(HOD)\n
	""")
def CSE_STAFF_A(update: Update, context: CallbackContext):
	update.message.reply_text("""Name: Dr.N.LakshmiPathi Anantha(HOD)\n
	Subject: Object Oriented Programming\n
	Phone number: *********\n 
	
	Name: Dr.K.Venu Gopal Reddy(CSE-A)\n
	Subject: Discrete Mathematics\n
	Phone number: *********\n
	
	Name: Ms.J.Kavitha Reddy(CSE-A)\n
	Subject: Computer Organization and Architecture\n
	Phone number: *********\n 
	
	Name: Mr.V.Rja Shekar(CSE-A)\n
	Subject: Data Structures\n
	Phone number: *********\n
	
	Name: Mr.M.Srikanth(CSE-A)\n
	Subject: Object Oriented Programming\n
	Phone number: *********\n
	
	Name: Mr.P.Sanjeeva(CSE-A)\n
	Subject: Operating Systems\n
	Phone number: *********\n
	
	Name: Mr.M.Prashanth(CSE-A)\n
	Subject: Gender Sensitization\n
	Phone number: *********\n
	""")

def CSE_STAFF_B(update: Update, context: CallbackContext):
	update.message.reply_text("""Name: Dr.N.LakshmiPathi Anantha(HOD)\n
	Subject: Object Oriented Programming\n
	Phone number: *********\n 
	
	Name: Mr.G.Gangadhar(CSE-B)\n
	Subject: Discrete Mathematics\n
	Phone number: *********\n
	
	Name: Dr.J.Anitha(CSE-B)\n
	Subject: Computer Organization and Architecture\n
	Phone number: *********\n 
	
	Name: Dr.D.Madhuri(CSE-B)\n
	Subject: Data Structures\n
	Phone number: *********\n
	
	Name: Ms.S.Viharika(CSE-B)\n
	Subject: Object Oriented Programming\n
	Phone number: *********\n
	
	Name: Dr.B.Hari Krishna(CSE-B)\n
	Subject: Operating Systems\n
	Phone number: *********\n
	
	Name: Mr.S.Bhoomesh(CSE-B)\n
	Subject: Gender Sensitization\n
	Phone number: *********\n """)
	
def CSE_STAFF_C(update: Update, context: CallbackContext):
	update.message.reply_text("""Name: Dr.N.LakshmiPathi Anantha(HOD)\n
	Subject: Object Oriented Programming\n
	Phone number: *********\n 
	
	Name: Dr.K.Venu Gopal Reddy(CSE-C)\n
	Subject: Discrete Mathematics\n
	Phone number: *********\n
	
	Name: Dr.J.Anitha(CSE-C)\n
	Subject: Computer Organization and Architecture\n
	Phone number: *********\n 
	
	Name: Mr.V.Raja Sekhar(CSE-C)\n
	Subject: Data Structures\n
	Phone number: *********\n
	
	Name: Ms.M.Srikanth(CSE-C)\n
	Subject: Object Oriented Programming\n
	Phone number: *********\n
	
	Name: Mr.P.Sanjeeva(CSE-C)\n
	Subject: Operating Systems\n
	Phone number: *********\n
	
	Name: Mr.Sohang Debnath(CSE-C)\n
	Subject: Gender Sensitization\n
	Phone number: *********\n  """)
	
def CSE_STAFF_D(update: Update, context: CallbackContext):
	update.message.reply_text("""Name: Dr.N.LakshmiPathi Anantha(HOD)\n
	Subject: Object Oriented Programming\n
	Phone number: *********\n 
	
	Name: Mr.M.Venkata Ramana Reddy(CSE-D)\n
	Subject: Discrete Mathematics\n
	Phone number: *********\n
	
	Name: Ms.J.Kavitha Reddy(CSE-D)\n
	Subject: Computer Organization and Architecture\n
	Phone number: *********\n 
	
	Name: Dr.D.Madhuri(CSE-D)\n
	Subject: Data Structures\n
	Phone number: *********\n
	
	Name: Ms.A.Rasagnya(CSE-D)\n
	Subject: Object Oriented Programming\n
	Phone number: *********\n
	
	Name: Dr.B.Hari Krishna(CSE-D)\n
	Subject: Operating Systems\n
	Phone number: *********\n
	
	Name: Mr.G.Pradeep Kumar(CSE-D)\n
	Subject: Gender Sensitization\n
	Phone number: *********\n
	""")
	
def CSE_CS(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def CSE_AI(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def CSE_DS(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)

def CSE_IOT(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def IT_STAFF(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def ECE_STAFF(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def EEE_STAFF(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def CIVIL_ENGG(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def MECHANICAL_ENGG(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def MINING_ENGG(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def MACHINE_DESING(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def ELECTRICAL_POWER_SYSTEMS(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def STRUCTURAL_ENGINEERING(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def THERMAL_ENGINEERING(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
	
def CSE_PG(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def VLSI_AND_EMBEDDED_SYSTEMS(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def MBA_STAFF(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def PHARMACY_STAFF(update: Update, context: CallbackContext):
	update.message.reply_text(""" No Data """)
	
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('BlockInfo', BlockInfo))
updater.dispatcher.add_handler(CommandHandler('DepartmentInfo', DepartmentInfo))
updater.dispatcher.add_handler(CommandHandler('StaffInfo',StaffInfo))
updater.dispatcher.add_handler(CommandHandler('Knowledge_Resource_Centre', Knowledge_Resource_Centre))
updater.dispatcher.add_handler(CommandHandler('Admin_Block', Admin_Block))
updater.dispatcher.add_handler(CommandHandler('CSE_Block', CSE_Block))
updater.dispatcher.add_handler(CommandHandler('Civil_Engineering_Block', Civil_Engineering_Block))
updater.dispatcher.add_handler(CommandHandler('MBA_Block', MBA_Block))
updater.dispatcher.add_handler(CommandHandler('Pharmacy_Block', Pharmacy_Block))
updater.dispatcher.add_handler(CommandHandler('Humanites_and_Sciences', Humanites_and_Sciences))
updater.dispatcher.add_handler(CommandHandler('CSE_STAFF', CSE_STAFF))
updater.dispatcher.add_handler(CommandHandler('CSE_STAFF_A', CSE_STAFF_A))
updater.dispatcher.add_handler(CommandHandler('CSE_STAFF_B', CSE_STAFF_B))
updater.dispatcher.add_handler(CommandHandler('CSE_STAFF_C', CSE_STAFF_C))
updater.dispatcher.add_handler(CommandHandler('CSE_STAFF_D', CSE_STAFF_D))
updater.dispatcher.add_handler(CommandHandler('CSE_CS', CSE_CS))
updater.dispatcher.add_handler(CommandHandler('CSE_DS', CSE_DS))
updater.dispatcher.add_handler(CommandHandler('CSE_IOT', CSE_IOT ))
updater.dispatcher.add_handler(CommandHandler('IT_STAFF', IT_STAFF))
updater.dispatcher.add_handler(CommandHandler('ECE_STAFF', ECE_STAFF))
updater.dispatcher.add_handler(CommandHandler('EEE_STAFF', EEE_STAFF))
updater.dispatcher.add_handler(CommandHandler('CIVIL_ENGG', CIVIL_ENGG ))
updater.dispatcher.add_handler(CommandHandler('MECHANICAL_ENGG', MECHANICAL_ENGG))
updater.dispatcher.add_handler(CommandHandler('MINING_ENGG', MINING_ENGG))
updater.dispatcher.add_handler(CommandHandler('MACHINE_DESING', MACHINE_DESING))
updater.dispatcher.add_handler(CommandHandler('ELECTRICAL_POWER_SYSTEMS',ELECTRICAL_POWER_SYSTEMS ))
updater.dispatcher.add_handler(CommandHandler('STRUCTURAL_ENGINEERING',STRUCTURAL_ENGINEERING ))
updater.dispatcher.add_handler(CommandHandler('THERMAL_ENGINEERING', THERMAL_ENGINEERING))
updater.dispatcher.add_handler(CommandHandler('CSE_PG', CSE_PG))
updater.dispatcher.add_handler(CommandHandler('VLSI_AND_EMBEDDED_SYSTEMS', VLSI_AND_EMBEDDED_SYSTEMS))
updater.dispatcher.add_handler(CommandHandler('MBA_STAFF', MBA_STAFF))
updater.dispatcher.add_handler(CommandHandler('CSE', CSE))
updater.dispatcher.add_handler(CommandHandler('Mechanical', Mechanical))
updater.dispatcher.add_handler(CommandHandler('ECE', ECE))
updater.dispatcher.add_handler(CommandHandler('EEE', EEE))
updater.dispatcher.add_handler(CommandHandler('Civil', Civil))
updater.dispatcher.add_handler(CommandHandler('Mining', Mining))
updater.dispatcher.add_handler(CommandHandler('IT', IT))
updater.dispatcher.add_handler(CommandHandler('MBA', MBA))
updater.dispatcher.add_handler(CommandHandler('Pharmacy', Pharmacy))
updater.dispatcher.add_handler(CommandHandler('PHARMACY_STAFF', PHARMACY_STAFF))
updater.dispatcher.add_handler(CommandHandler('UG_STAFF', UG_Staff))
updater.dispatcher.add_handler(CommandHandler('PG_STAFF', PG_Staff))
updater.dispatcher.add_handler(CommandHandler('Admin_Staff', Admin_Staff))
updater.dispatcher.add_handler(CommandHandler('Sports_Staff', Sports_Staff))
updater.dispatcher.add_handler(CommandHandler('Ground_floor', Ground_floor))
updater.dispatcher.add_handler(CommandHandler('First_floor', First_floor))
updater.dispatcher.add_handler(CommandHandler('Second_floor', Second_floor))
updater.dispatcher.add_handler(CommandHandler('Third_floor', Third_floor))
updater.dispatcher.add_handler(CommandHandler('Fourth_floor', Fourth_floor))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()

