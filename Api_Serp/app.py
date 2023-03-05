# Import modules
import pickle
from deep_translator import GoogleTranslator as transaltor
import warnings
def feel_ing(input_ar):
    warnings.filterwarnings('ignore')

    # Load the model 
    model = pickle.load(open("model.pickle", "rb"))

    # Get input sentence
    input_ar = input_ar 

    # Translate input to english
    input_en = transaltor(source="ar", target="en").translate(input_ar) 

    # Pass the input to model and get output
    output_en = model.predict([input_en])[0]

    # Translate output back to arabic
    output_ar = transaltor(source="en", target="ar").translate(output_en) 

    # Print output in english and arabic
    return output_en,output_ar
    print(f"Output EN : {output_en}\nOutput AR : {output_ar} \n ")

str = "انا اشعر بالخوف"
en ,ar = feel_ing(str)
print(en)
print(ar)