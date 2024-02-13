import calendar
import sys
class menstrual_cycle:

    def __init__(self,year,month):
        self._year = year
        self._month = month

    def days_of_month(self,the_year,the_month,days):
        new_calender = calendar.monthrange(the_year,the_month)

        return  list(range(1,new_calender + 1))




    def welcome_message(self):
        print("""Hi welcome to Female lulu menstrual tracking application, thank you for choosing us.
            """)
    def get_user_name(self):
        user_name = str(input("What is your?."))
        print("Hello "+user_name)

    def get_user_age(self):
        user_age = int(input("How old?."))
        average_menstrual_age = 12
        if user_age < average_menstrual_age:
            print("""
             Hello! This app is designed for users who have started menstruating and may contain sensitive content related to menstrual health.
             If you're under 12 years of age and have questions, consider talking to a trusted adult or healthcare provider for guidance. Take care!
                    """)

            response = str(input("Would you like to continue with the app? enter yes/no"))
            if response.casefold() == "yes":
                print("""
                    Hello welcome to Female Lulu Menstrual cycle tracking app!.
                    Track and monitor your menstrual cycle with ease.
                    Get insights, predictions, and helpful reminders.
                    Let's get started!""")

            elif response.casefold() == "no":
                print("Goodbye, thank you for choosing us.")
                sys.exist()


def display_menstrual_information():
    print("""
             What is menstruation?
             Menstruation is one part of a woman's cycle when the lining of the uterus (endometrium) is shed.
             This occurs throughout a woman's reproductive life. With each monthly cycle, the endometrium prepares itself to nourish a fetus.
             Increased levels of estrogen and progesterone help thicken its walls.
             If fertilization does not occur, the endometrium, along with blood and mucus from the vagina and cervix make up the menstrual flow that leaves the body through the vagina during the period.

             When does menstruation start?
             On average, a young woman in the world has her first menstrual period at about age 12.
             This is generally 2 to 3 years after her breasts start to grow. This is also soon after she notices pubic and underarm hair.
      
             Stress, strenuous exercise, and diet can affect when a girl first has her period.
             The American College of Obstetricians and Gynecologists recommends that a young woman consult her healthcare provider if she has not started to menstruate by the age of 15, or if she has not begun to develop breast buds, pubic hair, or underarm hair by the age of 13.
                    
             What is ovulation?
             Ovulation is a phase of the female menstrual cycle that involves the release of an egg (ovum) from one of the ovaries.
             It generally occurs about two weeks before the start of the menstrual period.
                """)
    print("""
    
        """)

def calculate_menstrual_cycle():
    last_day_of_flow = int(input("When was the last day of your menstrual flow?"))
    last_flow_month = int(input("What moth did you experience your last flow?."))
    year_of_last_flow = int(input("What year was that the last flow?."))

    days_of_the_month = 30

    valid_answer = True
    while valid_answer:
        if last_day_of_flow < 1 and last_day_of_flow > days_of_the_month:
            print("Enter a valid date")


