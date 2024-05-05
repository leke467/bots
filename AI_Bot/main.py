import PIL.Image
import google.generativeai as genai

# Generating Gemini Model for Bot
# Keep your API Key in Double Quotes
YOUR_API_KEY = ""
genai.configure(api_key=YOUR_API_KEY)

while True:
    # Asking for Text Search or Image Search
    textOrImage = input("What you want to give in input Text[T] or Image[I] : ")
    
    # If Text[T] Selected
    if textOrImage == 'T':
        # Asking for Prompt
        text = input("Enter Prompt to Search : \n")
        
        # Creating Gemini Model Object
        model = genai.GenerativeModel('gemini-1.0-pro-latest')
        response = model.generate_content(text)
        
        # Printing Output
        print('\n' + response.text)
    
    # If Image[I] Selected
    if textOrImage == 'I':
        # Asking for Prompt
        imagePath = input("Enter Path of Image to Search : \n")

        # Creating Gemini Model Object
        model = genai.GenerativeModel('gemini-pro-vision')

        # Opening Image using PIL
        image = PIL.Image.open(imagePath)
        response = model.generate_content(image)

        # Printing Output
        print('\n' + response.text)
    
    searchAgain = input('Do you want to search again [y/n] ?? ')
    if searchAgain == 'n':
        break