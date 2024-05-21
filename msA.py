import time
import random
import sys

def random_quote_generator ():

    listOfRandomQuotes =  [
    "The only way to do great work is to love what you do. Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. Albert Schweitzer",
    "Believe you can and you're halfway there. Theodore Roosevelt",
    "Your time is limited, so don't waste it living someone else's life. Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. Eleanor Roosevelt",
    "Don't watch the clock; do what it does. Keep going. Sam Levenson",
    "The harder you work for something, the greater you'll feel when you achieve it. Anonymous",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. Winston Churchill",
    "You are never too old to set another goal or to dream a new dream.C.S. Lewis",
    "The only limit to our realization of tomorrow will be our doubts of today. Franklin D. Roosevelt",
    "Dream big and dare to fail.Norman Vaughan",
    "It does not matter how slowly you go as long as you do not stop.Confucius",
    "The way to get started is to quit talking and begin doing. Walt Disney",
    "The best time to plant a tree was 20 years ago. The second best time is now. Chinese Proverb",
    "Act as if what you do makes a difference. It does. William James",
    "Success usually comes to those who are too busy to be looking for it. Henry David Thoreau",
    "Don't be afraid to give up the good to go for the great.  John D. Rockefeller",
    "I find that the harder I work, the more luck I seem to have. Thomas Jefferson",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. Zig Ziglar",
    "Do not wait to strike till the iron is hot; but make it hot by striking. William Butler Yeats"
]

    while True:
        time.sleep(1)
        print("Waking Up ...")
        try:
            fileToProcess = open("./quote.txt", "r+") 
        except IOError:
            print("Could not open file! Maybe already open by ui")
            continue
        line = fileToProcess.readline().strip()
        print(line)

        if len(line) > 0 and "run" == line:
            print("Found run replace with random quote")
            randomQuote =  random.choice(listOfRandomQuotes)
            print("Random number is: ", randomQuote)
            fileToProcess.seek(0)  
            fileToProcess.truncate(0)   
            fileToProcess.write(str(randomQuote) + "\n")  

        fileToProcess.close()

random_quote_generator()

