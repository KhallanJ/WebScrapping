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
    
    
    
    def interactionMenu(self, text):
        def count_word():
            word = input("What word are you looking for")
            print(f"\nThe word \"{word}\" appears:" , word_counts.get(word, 0) , "times")
    
        def check_exsistacne():
            word = input("What word are you looking for? ")
            if word in word_counts:
                print(f"\nYes. The word \"{word}\" does exist in the website")
            else:
                print(f"\nNo. The word \"{word}\" does NOT exist in the website")

        
        def queryLookUp():
            query = input("Type Your Question Here: ")
            print("\n")
            query_words = query.lower().split()
            
            # Splits the text into chunks, split by periods
            clean_punctuation = text.replace("!", ".").replace("?", ".")
            sentences_words = clean_punctuation.split(".")
            
            results = []
            ignore_words = ["a", "the", "with", "of", "i", "this", "that", "to", "and", "an", "is", "what"]
            for sentence in sentences_words:
                score = 0
                for word in query_words:
                    if word in ignore_words:
                        continue
                    elif word in sentence.split():
                        score += 1   
                        
                if score > 0:
                    results.append((sentence, score))
                
            results.sort(key=lambda x: x[1], reverse=True)
            
            if score == 0:
                    print("Error 404: Does not exist\n")
                    
            for result in results[:3]:
                print("\"", result[0], "\"", "\tScore:", result[1], "\n")
            
                    
    

        while True:
            print("\n1. Check word frequency")
            print("2. Check if word exists")
            print("3. Ask A Question")
            print("4. Exit")
                        
            choice = input("\nChoose Option: ")
            
            if choice == "1":
                count_word()
            elif choice == "2":
                check_exsistacne()
            elif choice == "3":
                queryLookUp()
            else:
                break
            
if __name__ == "__main__":
    WS = WebScrapping()
    
    text = WS.extract_text_from_URL("https://httpbin.org/html")
    text = WS.to_Lower(text)
    words = WS.split(text)
    
    word_counts = WS.counting_words(words)
    WS.interactionMenu(text)
    
    
    
        
