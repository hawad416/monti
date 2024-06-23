from stories.StoryPage import StoryPage
from stories.StoryBook import Storybook

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



