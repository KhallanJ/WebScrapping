import requests
from bs4 import BeautifulSoup
import re

class WebScrapping:
    def extract_text_from_URL(self, url):  
        # Deter Wiki from thinking this program is a bot
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        text = ""

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
    
    
    
    def interactionMenu(self, text, word_counts):
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
            
            # Convert all ending punctuaiton to periods, then splits on them
            clean_punctuation = text.replace("!", ".").replace("?", ".").replace(",", " ")
            sentences_words = clean_punctuation.split(".")
                        
            results = []
            # Filler words are exempt from Search
            ignore_words = ["a", "the", "with", "of", "i", "this", "that", "to", "and", "an", "is", "what"]
            query_words = [w for w in query_words if w not in ignore_words] # Ignore the word, if it is found in ingore_words
            
            total_possible_weight = sum(1 / word_counts[w] for w in query_words if w in word_counts)

            for sentence in sentences_words:
                # Normalize Punctuation
                sentences_words = re.sub(r'[^\w\s]', '', text)
                matches = 0
                # Find the amount of matches between query and sentance
                for word in query_words:
                    if word in sentence.split() and word in word_counts:
                        matches += 1 / word_counts[word]
                  
                # Determine score for revelance      
                score = 0
                if total_possible_weight > 0:          
                    score = matches / total_possible_weight
                else:
                    print("Cannot divide by Zero")
       
                # Append scores to the results list
                if score > 0:
                    results.append((sentence, score))
                
            results.sort(key=lambda x: x[1], reverse=True)
            print(sentence)
            print(matches) 
            
            # If results[] is empty (no words have been found) print error 
            if not results:
                print("Error 404: Does not exist\n")
                    
            # Print formatting
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
    
    text = WS.extract_text_from_URL("https://en.wikipedia.org/wiki/Lego")
    text = WS.to_Lower(text)
    words = WS.split(text)
    
    word_counts = WS.counting_words(words)
    WS.interactionMenu(text, word_counts)
    
    #https://www.britannica.com/topic/LEGO
    #https://httpbin.org/html
    
        
