import requests
from bs4 import BeautifulSoup

class WebScrapping:
    def extract_text_from_URL(self, url):     
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML and extract text
            soup = BeautifulSoup(response.text, "html.parser")

            # Removes the CSS and HTML/JS text (like <p> or <div>), so you just recieve the unformatted text
            for script_or_style in soup(["script", "style"]):
                script_or_style.decompose()

            # Joins all text w/o extra whitespaces
            text = soup.get_text(separator=' ', strip=True)
        else: 
            # Print Error message with correct error code
            print(f"Failed to retrieve page. Status code: {response.status_code}")
            
        return text
    
    def to_Lower(self, text):
        text = text.lower()
        return text
    
    def split(self, text):
        words = text.split()
        return words
    
    def counting_words(self, words):
        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        return word_count            

    def printText(self, words):
        print (words)           
    
    
    
    def interactionMenu(self, count_words, text):
        def count_word():
            word = input("What word are you looking for")
            print(f"\nThe word \"{word}\" appears:" , word_counts.get(word, 0) , "times")
    
        def check_exsistacne():
            word = input("What word are you looking for? ")
            if word in word_counts:
                print(f"\nYes. The word \"{word}\" does exist in the website")
            else:
                print(f"\nNo. The word \"{word}\" does NOT exist in the website")

        
        def sentence_search():
            word = input("What word are you looking for? ")
            # Splits the text into chunks, split by periods
            sentences = text.split(".")
    
            # Then searches each and every sentence (s) in sentences array and looks for the word
            # if it appears it prints it
            for s in sentences:
                if word in s.lower():
                    print(s.strip(),".")
        
        while True:
            print("\n1. Check word frequency")
            print("2. Check if word exists")
            print("3. Show sentences containing word")
            print("4. Exit")
                        
            choice = input("\nChoose Option: ")
            
            if choice == "1":
                count_word()
            elif choice == "2":
                check_exsistacne()
            elif choice == "3":
                sentence_search()
            else:
                break;
            
if __name__ == "__main__":
    WS = WebScrapping()
    
    text = WS.extract_text_from_URL("https://httpbin.org/html")
    text = WS.to_Lower(text)
    words = WS.split(text)
    
    word_counts = WS.counting_words(words)
    # WS.printText(word_counts)
    WS.interactionMenu(word_counts, text)
    
    
    
        
