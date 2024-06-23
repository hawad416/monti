from langchain_openai import ChatOpenAI
import openai
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
import streamlit as st
import time 





st.set_page_config(layout="wide")
st.title("lesson 1: hansel & gretel 🍭")

     
def get_comprehension_analysis(excerpt, question, reflection, metric):
    analysis_prompt = f"""
    Role: You are a teacher at a montessori creating questions to foster critical thinking in young readers.  
    Your student has recently read an excerpt from a childrens book & has completed a reflection that you will provide feedback on.
    Only respond to the students reflection. Be honest on where they need improvements. 

    The excerpt that the student read was: {excerpt}
    The critical thinking question you gave to the student was: {question}
    The students reflection is below:
    {reflection}

    Task: 
    - Your task is to generate thoughtful feedback and analysis of the young readers reflection in a way a child aged 8-13 can grasp.Do not be too formal.
    - Your feedback should encourages young readers to keep digging deeper & also be proud of their own imagination.
    - Analyze the given excerpt, the question you originally presented to the student, & the students answer.
    - Provide the student feedback on their ability to fulfill {metric}, & to be creative, logical, and curious.
    - Aim to stimulate critical thinking and reflection.
    - You should only return the question bullet points of your feedback and nothing more. Be sure to also include questions you can leave the student with.
    For example:
         - 'Great work thinking critically about the characters choice'
         - 'What do you think might have happened if the character made the opposite choice?"
         - 'Way to add a creative touch as to why this event occured'
         - etc.
    """
    system_prompt = analysis_prompt
            
    messages = [
                {"role": "system", "content": system_prompt},
        ]

            # Create a completion request to OpenAI
    completion = openai.chat.completions.create(
                model="gpt-4-0125-preview",
                messages=messages,
            )
    preferences = completion.choices[0].message.content
    print(preferences)
            
    return preferences
       

    
    

# takes in a specific story chapter and generates a string based on it.
# also takes in the metric the user would like to improve. 
# uses AI to generate the best questions. 
# for now, hard coding critical thinking, will make a default later based on the metric.
def get_comprehension_question(str_chapter, comprehension_prompt):
        """
        Generates Comprehension Question.
        """
        
        system_prompt = comprehension_prompt
            
        messages = [
                {"role": "system", "content": system_prompt},
        ]

            # Create a completion request to OpenAI
        completion = openai.chat.completions.create(
                model="gpt-4-0125-preview",
                messages=messages,
            )
        preferences = completion.choices[0].message.content
        print(preferences)
            
        return preferences
        


from stories.StoryPage import StoryPage
from stories.StoryBook import Storybook
from audiorecorder import audiorecorder



with st.sidebar:
    st.title("monti 🧸| hawas workspace")
    st.subheader("the montessori experience - at a fraction of the cost")
    st.markdown(
        """feedback of reading progress will be dispalyed here!"""
    )
    st.header("Progress")
    st.success("New Lesson Started", icon="💚")

m = st.markdown("""
    <style>
    div.stButton > button:last-child {
        background-color: rgb(255, 255, 237);
    }
    </style>""", unsafe_allow_html=True)

with st.chat_message("assistant"):
        intro = "hey! i am monti 🧸, your friend for helping you create the most magical stories and improve your reading skills. let's get started!"
        st.markdown(intro)
        imgs = (["https://i.pinimg.com/originals/21/57/5b/21575b799eb661dff318c504dc38798b.gif"])
        st.image(imgs, width=120)



st.subheader("which skill are you practicing today?")





example_prompts = [
    "Imagination",
    "Comprehension",
    "Critical Thinking",
    "Reasoning",
    "Writing Clarity",
]

button_cols = st.columns(6)
button_cols[0].button(example_prompts[0])
button_cols[1].button(example_prompts[1])
button_cols[2].button(example_prompts[2])
button_cols[3].button(example_prompts[3])
button_cols[4].button(example_prompts[4])


st.write("")
st.write("")
st.write("")

story_pages = [
    StoryPage("Hansel and Gretel lived in a damp little cottage on the dark side of Long Lost Wood. Their mother had died one frosty day, so their father had married a new wife who was NOT as sweet as she seemed. In fact, she was as bad as a rotten apple."),
    StoryPage("“Your children eat too much,” she grumbled one day to her husband, as Hansel and Gretel shared a single slice of stale bread. “You must lose them in the wood and let the wild creatures care for them.”"),
    StoryPage("Their father was shocked. “If I do that, the wolves will eat them,” he protested. “And if you don’t, we will all die of hunger,” snapped the nasty stepmother. “Take them away tonight.”"),
    StoryPage("As soon as the first star shone, the children’s father led them along tangled pathways to a crooked tree. “My dears,” he groaned, “wait here while I search for firewood.” Then away he stumbled, back to his damp little cottage and his cruel wife. Quite soon, wolves began to howl and the children shivered."),
    StoryPage("“We have walked too far,” sighed Gretel. “Our father is lost, and so are we.” “Cheer up, little sister,” said Hansel with a smile. “I heard our Stepmother’s horrid plan, so I have marked every twist of the path with a pure white pebble.” And there in the starlight Gretel saw a line of shining stones!", is_pause=True),
    StoryPage("The children followed the white trail, and by sunrise they were safely home – but their stepmother’s smile was as cold as winter rain. “Husband,” she hissed. “See how your two pests torment me. Tonight you must lose them forever.”"),
    StoryPage("She gave each child a morsel of stale bread, and when their father led them through Long Lost Wood they followed him sadly. After many miles, he mopped his eyes and said, “Wait here, my dears, while I search for ripe blackberries.”"),
    StoryPage("They knew he would never come back, but when the wolves howled, Hansel smiled and said, “Cheer up, little sister. This time I have scattered a trail of small white breadcrumbs.”"),
    StoryPage("Alas! There was no trail to be seen – hungry birds had stolen EVERY crumb. So the two children slept on a bed of brown leaves, and in their dreams they saw a white dove who circled above them, calling: “Follow me! Follow me!”", is_pause=True),
    StoryPage("When they woke in the misty morning, there was the white dove fluttering away! “Let’s follow her,” said Hansel. “Things can’t get any worse.”"),
    StoryPage("Almost at once, the children saw a wonderful cottage made from gingerbread and sweeties. Their mouths watered, and soon they were nibbling delicious chunks of wall and windowsill. Suddenly, a sugar-sweet voice said, “Come in my dears and warm yourselves.” An old lady stood by the door, and the children forgot to be frightened. In they skipped, and BANG went the door. They were trapped inside a witch’s house!"),
    StoryPage("Now her voice became as hard as a seaside rock. “Got you!” she cackled, locking Hansel inside an iron cage. “Boy, you will grow plump and juicy. Girl, you will be my slave.”"),
    StoryPage("Poor Hansel. The witch fattened him up until he was as round as a gobstopper. Poor Gretel. She ate nothing but scraps from the cat’s saucer."),
    StoryPage("At last the witch shrieked, “Girl! Build up the fire. I want Boy Pie for my tea.”", is_pause=True),
    StoryPage("“I’m very sorry,” said Gretel politely, “but I have never cooked a Boy Pie before. Do you think the oven is hot enough?”"),
    StoryPage("The witch stamped her foot and peered into the oven. “It’s HOT, HOT, HOT!” she screamed, and no wonder… Gretel had pushed her inside and slammed the door!"),
    StoryPage("In moments, Hansel was free. The two children grabbed the witch’s treasure and raced outside, to find the white dove waiting for them. Of course, she led them home by the shortest way, and when their father saw them, his smile was as warm as the summer sun."),
    StoryPage("(Astonishingly, Hansel and Gretel’s horrible stepmother had vanished that very day – while all that remained of the wicked witch was one smoky gingerbread biscuit.) The end.")
]

comprehension_pauses = [4, 8, 13]  # Indices of story_pages where comprehension questions will appear

storybook = Storybook(story_text=story_pages, comprehension_pauses=comprehension_pauses)

has_completed_comprehension = False


# CHAPTER 1 

with st.expander("Chapter 1", icon="🤠"):
    st.subheader("Introduction ")
    # Example of accessing pages and checking for comprehension pauses
    chapter1 = ""
    for i in range(storybook.num_pages()):
        page = storybook.get_page(i)
        chapter1+=page.text + "\n\n"
        if storybook.is_comprehension_pause(i):
            st.markdown(chapter1)
            print(f"Time for a comprehension check {i+1}")
            break
    
    st.code(
        """
        time for a fun comprehension check :)""", language="txt"    
    )

    comprehension_prompt = f"""
    Role: You are a teacher at a montessori creating questions to foster critical thinking in young readers. Do not ask too many leading questions. 
    You ask deep questions to children to see them grow into high impact adults.

    Task: 
    - Your task is to generate a thoughtful question that encourages young readers to analyze the given excerpt from a childrens book. 
    - Encourage exploration of character traits, motivations, and deeper meanings behind the choices taken by the characters.
    - Aim to stimulate critical thinking and reflection on the story's themes.
    - Go a level deeper, ask the children questions about the passage as if they are highly inteligent adults.
    - You should only return the question string eg. "why did you eat today?" and nothing more. 
    

    Make sure your question is ONLY ABOUT THE BELOW EXCERPT the child has just read:

    {chapter1}
    """

    question = ""

    if st.button("Start Comprehension Check"):
        question = get_comprehension_question(chapter1, comprehension_prompt)
        st.code(question,language="txt")

    audio = audiorecorder("🎙️ tell monti what you think!", "click to stop recording")

    if len(audio) > 0:
                    # To play audio in frontend:
                    # To save audio to a file, use pydub export method:
            print("audio file saved!")
            st.audio(audio.export().read()) 
            audio.export("audio.wav", format="wav")

    
    
            with st.spinner("monti 🧸 is listening to your wonderful reflection..."):   
                    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLwTdUz9t_7mbOWxcfT0EPQbCE7Fik5r9d1g&s", width = 50)  
                    import speech_recognition as sr
                    r = sr.Recognizer()

                    hellow=sr.AudioFile('audio.wav')
                    with hellow as source:
                        audio = r.record(source)
                    try:
                        reflection = r.recognize_google(audio)
                        print("Text: "+ reflection)
                    except Exception as e:
                        print("Exception: "+str(e))

                    st.caption("your reflection transcript: " + reflection)

                    metric_to_improve = "critical thinking"
                    analysis = get_comprehension_analysis(chapter1, question, reflection, "Critical Thinking")
                    st.code(analysis, language="txt")
                    has_completed_comprehension = True

    
    if has_completed_comprehension:
        st.image("https://i.pinimg.com/originals/fa/ed/62/faed622a5d07d85ac7a190f0a8c385bc.gif", width=60)
        st.text("Optional Further Reflection Based on Above Analysis")
        st.text_input("")
        st.success("Amazing Job! Next Chapter...")
        # potential feedback analysis here. 


    has_completed_comprehension = False


if has_completed_comprehension:
     # go on to chapter 2 !
     has_completed_comprehension = False
     with st.expander("Chapter 1"):
        st.subheader("Introduction ")
        # Example of accessing pages and checking for comprehension pauses
        chapter1 = ""
        for i in range(storybook.num_pages()):
            page = storybook.get_page(i)
            chapter1+=page.text + "\n\n"
            if storybook.is_comprehension_pause(i):
                st.markdown(chapter1)
                print(f"Time for a comprehension check {i+1}")
                break
        
        st.code(
            """
            time for a fun comprehension check :)""", language="txt"
        
        )

        st.button("")


