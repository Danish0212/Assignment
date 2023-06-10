import streamlit as st
from src.model import generate_response3

def foo():
    doc1= "Document 1: THE WINDOW On a windy winter morning, a woman looked out of the window.The only thing she saw, a garden. A smile spread across her face as she spotted Maria, her daughter, in the middle of the garden enjoying the weather. It started drizzling. Maria started dancing joyfully.She tried to wave to her daughter, but her elbow was stuck, her arm hurt, her smile turned upside down. Reality came crashing down as the drizzle turned into a storm. Maria's murdered corpse consumed her mind.On a windy winter morning, a woman looked out of the window of her jail cell."
    doc2= '''Document 2: A BROKEN PROMISE
    Hearing a knock on the door,  she hustled towards it with her  little feet, her lips uncloaking the cutest smile and her voice singing, "Daddy's home!" Her mum, glued to the news channels for the past week, approached the door hesitantly and opened it with trepidation.Two men in military uniform were standing at the doorstep. One of them handed her an envelope with a mournful expression, adding plaintively, "We're sorry, Mrs Bhatt.""Where's my dad, Uncle? He promised we'll celebrate Diwali together this time," exclaimed the girl. They stared helplessly, with a lump in their throats and moistened eyes.'''
    doc3 = '''Document 3: ALL'S FAIR IN LOVE
    As a married couple, they led a charmed life. Jantu had his own circle of friends and Tulu had hers. And every morning they exchanged and savoured their previous day's experiences over breakfast. Jantu was not immune to the seven-year-itch, though. The days he strayed were few and far between. Faithful Tulu was quietly accommodating. On the nights he slipped, Jantu would indicate it by skipping his daily apple at breakfast.That morning, Jantu was devastated to see Tulu's favourite pear was left untouched.'''

    w1,col1,col2,w2=st.columns((2,5.5,5.5,.5))
    with col1:
        st.write("### ")
        st.write("### ")
        st.markdown("### Enter a Question")
    with col2:
        st.write("### ")
        qn = st.text_input("")
        if st.button("Submit"):
            documents= doc1 + doc2 + doc3 + qn
            response=generate_response3(documents)
            st.info(response)

            
