# The script of the game goes in this file.
define neutral = "sound/neutral.mp3"
define good = "sound/good.mp3"
define bad = "sound/bad.mp3"
define ending = "sound/ending.mp3"
define badending = "sound/bad ending.mp3"
define bestending = "sound/best ending.mp3"
# Declare characters used by this game. The color argument colorizes the
# name of the character.
default yellow = False
define s = Character("Squishy")
define r = Character("Robber")
define h = Character("Cashier")
define p = Character("Cop")
define w = Character("Waiter")
define sh = Character("Shark")
define c = Character("Clyde")
define d = Character("'Dawgs'?")
define t = Character("Therapist")
define wo = Character("Woman")
define re = Character("Realtor")
define bb = Character("BillBob")
define j = Character("J'Becky")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    show morning

    "What a beautiful morning! Squishy wakes up with a smile."

    s "Wow, what a beautiful morning! I'm smiling so much."

    "Squishy walks downstairs to the kitchen to get ready for his day."

    show breakfast

    s "Hmmmmm, what should I have for breakfast? So many options..."

    menu: 
        
        "Will Squishy have the blue or the yellow?"

        "The blue.":
            jump blue1

        "The yellow.":
            jump yellow1

label blue1:
    
    play sound neutral

    scene blue

    "Squishy decides to eat the blue!"

    s "How delicious!"

    "After such an incredible breakfast, Squishy decides to go out on an adventure!"

    s "That's right, Narrator! Today, I'm gonna have myself an adventure!"

    s "The only question is..."

    scene first choice

    menu: 
        
        "Where do I start?"

        "The park":
            jump park

        "The beach":
            jump beach

label yellow1:
    
    play sound neutral

    scene yellow

    $ yellow = True

    "Squishy decides to eat the yellow!"

    s "How delectable!"

    "After such an incredible breakfast, Squishy decides to go out on an adventure!"

    s "That's right, Narrator! Today, I'm gonna have myself an adventure!"

    s "The only question is..."

    scene first choice

    menu: 
        
        "Where do I start?"

        "The park":
            jump park

        "The beach":
            jump beach

label park:

    play sound neutral
    
    s "I'll go to the park!"

    show park closed

    "Squishy sets out from his house and walks down the street to the park."

    "But, what's this? The park is closed?"

    s "Gosh darnit! I really wanted to go to the park."

    s "I guess I could go to the mall, it's close by."

    s "Or maybe... I could try to break in..."

    menu: 
    
        "What should I do?"

        "Go to the mall":
            jump mall

        "Break in to the park":
            jump breakin

label mall:

    play sound neutral

    s "I'll go to the mall!"

    "Squishy keeps walking until he winds up at the mall."

    show hot topic start

    "He decides to go to Hot Topic and find himself a new edgy accessory."

    s "I could use a new hat."

    "Squishy leisurely browses the store, hoping for something more interesting to happen."

    "He had really set himself up for an exciting day, and was really bummed about the park being closed."

    s "Shut up, Narrator! This hat is the one."

    show found hat

    "Suddenly - and quite rudely - Squishy finds the perfect hat."

    "He's about to buy it, when someone busts into the store!"

    show robber enter

    r "EVERYBODY ON THE GROUND!"

    "What?!?! Squishy hides in one of the aisles."

    r "Here's how this is going to go."

    "The criminal walks up to the register."

    r "I want every single graphic tee shirt with a vague reference to an anime in this bag."

    h "But sir, there's too many shirts, they'll never fit in that bag."

    r "SHIRTS. BAG. NOW!"

    r "Figure it out, make it work!"

    "Squishy doesn't like the sound of this."

    s "I don't like the sound of this. I need to do something!"

    show square up

    "Squishy springs into action, squaring up against the thief!"

    s "Hey, hotshot! What do you think you're doing?"

    r "Haha, classic. Heroic ball saves store from evil criminal. Nice try."

    "The thief lunges at Squishy, but Squishy rolls out of the way!"

    r "Wuh-what?!?"

    s "Not so cool now, huh? Watch it, pal."

    show beat robber

    "Squishy pins the robber down to the floor and ties his hands behind his back."

    s "Someone call the cops. We need a clean-up on aisle five."

    "The entire store starts clapping."

    "Several minutes later..."

    show cop

    s "I did what anyone would've done. I'm not special."

    p "That's still pretty impressive, son. Say, you ever thought about doing this professionally?"

    s "Hmmm, interesting. Could be pretty cool."

    p "I'd like you to join the CIA, Squish. We could really use someone like you."

    s "Yeah, that sounds pretty great. I'm in!"

    "Squishy is flown out to a special base on the Moon and meets his new partner, Christopher."

    play sound ending

    "He spends the rest of his life fighting crime."

    return

label breakin:

    play sound neutral

    s "I'm feeling risky. I'll break in to the park!"

    show park tree

    "Squishy spots a tree with a long branch that hangs over the park."

    "He climbs up, rolls across the branch, and drops into the park."

    show broken in
    
    "Squishy stands up and brushes himself off."

    s "Well, I'm here! What should I do..."

    show slide

    "..."

    show slide bottom

    "Squishy mundanely uses the park facilities, realizing that the park isn't very fun without other people there."

    show alone sad park
    
    s "Man. I sure wish there was someone else here to play with. Hey, what's that?"

    "Squishy notices a ball of clay in the corner of the park."

    show clay blob

    s "I could MAKE a friend! But what to make?"

    menu: 
    
        "Should I make..."

        "a dog?":
            jump dog

        "another ball?":
            jump ball

label dog:

    play sound good

    s "Ball's best friend! I'll make a dog!"

    show made dog

    "Squishy molds the clay into a little pup and it springs to life!"

    show dog head
    
    s "Hey, buddy!"

    show dog swing
    
    "The dog runs around the park excitedly, ready to play with his new owner."

    show dog slide top
    
    s "Let's go, buddy!"

    show dog slide
    
    "The pair of friends have a wonderful day together, filled with adventure."

    play sound ending

    "Later, they turn in for the night, excited for what the future will bring."
    
    return

label ball:

    play sound bad

    s "I'll make myself a friend. Another ball, like me!"

    "Squishy spends the entire day molding the clay into a masterpiece sculpture."

    show looking man
    
    "The ball he creates rivals the likes of the David and the Thinker."

    "When he finally is finished, he takes a step back to admire his work and wait for it to come to life."

    s "...what's wrong? Why isn't it coming to life?"

    "Squishy is disappointed as it dawns on him."

    s "Oh."

    s "This is just clay."

    s "..."

    show sad alone

    s "Not a person."

    play sound badending

    "Squishy goes home sad."

    return

label beach:

    play sound neutral

    s "It's a beautiful day outside. I'll head to the beach!"

    "Squishy excitedly rolls all the way to the beach."

    show beach start

    "The beach is busy today. It seems like everyone else wants to have an adventure too!"

    s "This looks like a good place to set up."

    "Squishy sets up an umbrella and a towel about 30 feet from the shore."

    show beach hang out
    
    s "Ahhhhh, this is nice."

    "Squishy relaxes."

    "HEEEEEEEELLLLLLP!"

    s "What was that?"

    show hear shark

    "Squishy jumps up to investigate."

    "What is that?"

    "Out in the water..."

    "A..."

    "A..."

    s "SHARK!"

    "Out in the water, a shark is terrorizing the beach-goers."

    s "I need to do something, I need to help out!"

    menu:

        "How should Squishy handle the shark?"

        "Fight it!":
            jump fight

        "Talk to it to calm it down.":
            jump convo

label fight:

    play sound bad

    s "I'll fight the shark!"

    "Squishy jumps into the water to save the beach, like the hero he is."

    show see shark

    "He fights the shark!"

    show fight shark

    "He-"

    "Well."

    "Oh, that doesn't look very good."

    "Oof."

    "Well, I guess in retrospect..."

    "It is a shark..."

    "..."

    show dead

    play sound badending

    "Squishy was a very noble ball."

    return

label convo:

    play sound good

    s "I'll talk to it! There's nothing a mature conversation can't fix."

    "Squishy approaches the shark and calls out..."

    s "You there! You heathen! Come here this instant!"

    "The shark swims closer..."

    s "Y-you, uh, you there..."

    show see shark

    "The shark stands up and walks towards Squishy?"

    sh "What do you want?"

    show talk to shark

    s "Uhhhhhhhhhh"

    "..."

    s "I'm a little confused..."

    sh "You've never seen a Shark before?"

    "..."

    s "No, it's not that..."

    s "Whatever, let's get to it."

    s "Why are you attacking all of these nice people?"

    sh "This is MY home! They're bothering ME! It's only fair."

    s "That's a good point, I never thought about it that way."

    sh "Why would you, you're one of them."

    "Squishy tries to think of a solution."

    s "How about this? I'll talk to the beach administration, we can cut a deal so you get some money when people hang out at the beach."

    sh "I'm listening..."

    s "And we can set a regulation that people don't swim past a certain mark."

    sh "...that sounds pretty good."

    sh "Thanks."

    s "No problem, I'm happy to help out. You seem like a good shark, just misunderstood."

    s "I would hate to see you be seen as a villain here."

    sh "You're very kind. What's your name?"

    s "Squishy. What's yours?"

    sh "Shark."

    s "Very straight-forward."

    sh "Are you free right now?"

    s "What?"

    sh "How's that for straight-forward?"

    s "Uh, yeah, I guess I am. Want to grab dinner?"

    sh "I'd love to."

    "The couple makes their way to a local fine dining spot."

    show date start

    s "Hahaha, what a funny story, Shark!"

    sh "Haha, yes it is so funny!"

    "As you can tell, they're really hitting it off."

    show order

    w "Are you two ready to order?"

    sh "I'll have the sushi, please."

    s "Hmmmmmm..."

    menu:

        "What should Squishy get?"
    
        "The chicken":
            jump chicken

        "The salad":
            jump salad

    label chicken:

        play sound bad

        s "I'll have the chicken, please."

        w "Sounds good, sir. I'll get that right away for you two."

        sh "Thank you."

        "The two continue their conversation for a bit while waiting for the food."

        w "Here you go. The sushi and the chicken."

        show get chicken

        sh "Thank you so much, this looks great."

        s "Yeah, thank you."

        "Squishy looks at his food."

        s "{i}This looks a little...undercooked?{/i}"

        s "...{i}I'm sure it's fine. It'll be great!{/i}"

        "Squishy takes a bite."

        "..."

        "Squishy swallows..."

        s "Uh oh."

        "The chicken does NOT sit well. Squishy starts to feel pretty queasy."

        s "*gulp*"

        if yellow:

            show yellow puke

            "Squishy vomits his yellow breakfast all over the floor of the restaurant!"

        else:

            show blue puke

            "Squishy vomits his blue breakfast all over the floor of the restaurant!"

        sh "Uhhh..."

        s "I am SO sorry! The chicken wasn't sitting well."

        "Squishy is overcome with embarassment."

        sh "It's okay...um, I think this isn't working out though...I really need to get home."

        s "What?"

        sh "Yeah, I need to...uh..."

        sh "Pet...uhhh..."

        sh "...my dog."

        "..."

        s "Okay, I guess. I really thought this was going well."

        sh "..."

        "Shark leaves, abandoning Squishy."

        show stood up

        s "I can't believe it. I thought we were really getting along."

        "Squishy glumly walks out of the restaurant and starts on his way back home."

        "He passes the park wondering what could have been different if he went there instead of the beach."

        "He passes by a movie theater."

        s "Maybe a movie will lift my spirits. It looks like they have two movies starting soon."

        show sad ticket

        menu:

            "What should I watch?"

            "The Kissing Booth 3":
                jump booth

            "Dances With Wolves":
                jump wolves

        label booth:

            play sound neutral

            s "I'll go see The Kissing Booth 3! A silly comedy will cheer me up."

            show sad movie

            "A few miserable hours later..."

            s "Ugh, that sucked! That movie was terrible."

            s "Now I feel even worse."

            "Squishy heads home, disappointed."

            s "What a day. Kind of disappointing, ultimately."

            "Squishy has a lot of feelings, so he starts to write them all down in a journal."

            "He writes and writes and writes until the journal is full."

            show therapist

            "The next day, he goes to see his therapist like he always does. He shows her the journal."

            t "Wow, Squishy. This is amazing writing! We'll dive into how you feel and the actual writing, but you're really talented."

            t "If you like writing, you should look into publishing. Any company would jump at the chance to work with you."

            s "Thank you, that's very kind. I'll think on it."

            "Squishy thinks on this for quite a while."

            menu:

                "Should he become a writer?"

                "Yes":
                    jump publish

                "No":
                    jump party

            label publish:

                play sound neutral

                "Squishy decides to publish his journal and become a writer!"

                "He writes and writes and writes."

                show meet exec

                "He meets with publishers and companies."

                show read book

                "He goes on tours, speaking and signing his books."

                "He becomes hugely successful, even getting picked up by a movie studio to write a feature film based on his life."

                "Several years later, it's the night of the premiere!"

                show publish movie

                "{i}Wow, I guess I really did have a 'Squishy's Big Day'.{/i}"

                "*STANDING OVATION*"

                show standing ovation

                s "Thank you! Thank you all!"

                "Squishy exits the theater happy. On the street, he runs into an old friend."

                show hey there

                sh "Squishy? Is that you? It's really good to see you!"

                show meet again

                "..."

                show walk away

                play sound badending

                "Squishy turns and walks away."

                return

            label party:

                play sound neutral

                s "Hmmm, I don't know if that's the right path for me."
            
                "Squishy politely declines the idea, as the life of super stardom has never appealed to him."
                
                "He feels much better, however, and greets the next day with a smile."

                s "I'm feeling much better and am ready for another adventure! Maybe this time I'll go to the park!"

                "Squishy heads to the park and finds that it's packed with patrons!"

                show meet clyde

                s "Woah! The park is pretty busy today! Maybe I can make some friends."

                "Squishy walks up to a group of youths and introduces himself."

                s "Hey, my name is Squishy. How are you guys doing?"

                c "Heh. Squish."

                c "Call me Clyde. These are my dawgs."

                s "Hello, Clyde. Hello, dawgs."

                d "Hey."

                c "Say, Squish. You like the swings?"

                s "Uh, yeah, I guess so."

                c "Walk with me."

                show slide clyde

                "Clyde leads Squishy over to the swings."

                c "Push me."

                "Clyde sits on the swing, waiting."

                "Squishy approaches the swing hesitantly, unsure of what's going on."

                s "Okay..."

                "He starts to push."

                c "Cool."

                "Squishy pushes Clyde in silence for about two hours."

                "It starts to get dark so Clyde jumps off of the swing."

                c "Hey, Squish. You seem pretty cool. Why don't you follow us back to our house?"

                s "Wow, thanks for the invite! That sounds awesome!"

                show couch

                "Squishy heads back to the Dawg House with Clyde and sits on their couch."

                show drug choice

                "Suddenly, Clyde takes something out of his pocket."

                "A cigarette!"

                s "Woah."

                c "Want a hit, Squish?"

                s "Uhhh, I don't know. I've never done that before."

                c "It'll be fine, Squish, don't worry so much."

                menu:

                    "What should {i}Squish{/i} do?"

                    "Succumb to peer pressure and smoke":
                        jump smoke

                    "Stand his ground":
                        jump decline

                label smoke:

                    play sound bad

                    "Out of fear of not seeming cool in front of the Dawgs, Squishy takes the cigarette and smokes!"

                    show smoke

                    s "I guess one hit can't hurt..."

                    show trip 1

                    "..."

                    show trip 2

                    s "Woah..."

                    "Squishy passes out!"

                    show wake up drug

                    "The next morning Squishy wakes up with little memory of the previous night."

                    s "...what happened..."

                    show morning talk

                    c "Morning, Squish!"

                    s "morning..."

                    c "Cheer up, bud! Want some breakfast?"

                    show friend choice

                    menu:

                        "Clyde shows you two options:"

                        "Blue":
                            jump friendblue

                        "Yellow":
                            jump friendyellow

                    label friendblue:

                        show friend choose blue

                        if yellow:

                            "Squishy takes the blue."

                            show restaurant talk

                            play sound good

                            "The blue is delicious! Clyde is an incredible cook."

                            s "Wow, Clyde. This is really great! Have you ever thought about becoming a chef?"

                            c "Actually, I think about it a lot. It could never happen, though. Some one like me?"

                            s "Don't sell yourself short, Clyde! You've got a lot of talent, you could really be successful."

                            c "...heh, yeah. Maybe I could..."

                            "The two go in on a restaurant together, and become incredibly renowned in the food world."

                            play sound ending

                            "Clyde got to realize his dream of cooking professionally and Squishy made a lifelong friend."

                            return

                        else:

                            "Squishy hesitantly takes the blue..."

                            s "*gulp*"

                            "Having thrown up his blue a few days ago, Squishy is very worried."

                            "He takes a bite."

                            "..."

                            play sound bad

                            show friend puke blue

                            "And throws it all up again!"

                            c "Ew! What the freak, Squish!"

                            s "...ugh...sorry..."

                            c "Get the freak out!"

                            play sound badending

                            "Squishy is kicked out of the Dawg House and walks home sad."

                            return

                    label friendyellow:

                        show friend choose yellow

                        if yellow:

                            "Squishy hesitantly takes the yellow..."

                            s "*gulp*"

                            "Having thrown up his yellow a few days ago, Squishy is very worried."

                            "He takes a bite."

                            "..."
                            
                            play sound bad

                            show friend puke yellow

                            "And throws it all up again!"

                            c "Ew! What the freak, Squish!"

                            s "...ugh...sorry..."

                            c "Get the freak out!"

                            play sound badending

                            "Squishy is kicked out of the Dawg House and walks home sad."

                            return

                        else:

                            "Squishy takes the yellow."

                            show restaurant talk

                            play sound good

                            "The yellow is delicious! Clyde is an incredible cook."

                            s "Wow, Clyde. This is really great! Have you ever thought about becoming a chef?"

                            c "Actually, I think about it a lot. It could never happen, though. Some one like me?"

                            s "Don't sell yourself short, Clyde! You've got a lot of talent, you could really be successful."

                            c "...heh, yeah. Maybe I could..."

                            "The two go in on a restaurant together, and become incredibly renowned in the food world."

                            play sound ending

                            "Clyde got to realize his dream of cooking professionally and Squishy made a lifelong friend."

                            return

                label decline:

                    play sound good

                    s "I'm sorry, but I really don't feel comfortable smoking."

                    c "All good, Squish! Glad you clearly let me know what your boundaries are!"

                    "Squishy decides to head home, but gets Clyde's number and makes a plan to go to the park again."

                    c "See you around, Squish!"

                    s "See ya!"

                    play sound ending

                    "Squishy heads home with a lot of hope for the future of his new friendship."

                    return
        
        label wolves:

            play sound neutral

            s "One ticket for {i}Dances With Wolves{/i}, please!"

            show sad movie

            "Squishy takes his seat in the theater and the lights dim."

            "3 hours later..."

            s "Wow."

            "Squishy was so moved by the movie."

            s "What an incredible film! I wish I could move people like that."

            s "..."

            s "Hmm..."

            s "Maybe I'll become a screenwriter!"

            show writing

            "Squishy buys a typewriter on the way home and pulls an all nighter working on his masterpiece."

            menu:

                "What genre is Squishy's movie?"

                "Sci-Fi epic":
                    jump scifi

                "Romantic drama":
                    jump romance

            label scifi:

                play sound bad

                "Squishy spends every waking moment over the next six months writing and writing."

                "He crafts an incredible world with mythical creatures and incredible technology."

                "He designs fully-fledged languages for his characters to speak in."

                "Three years later, his movie is premiering."

                show captain discuss

                "{i}But Captain Fillibuster! Without the geiger-drawn Gos-made antipeter, we'll never be able to make the gash-ho by 34 knocks!"

                "{i}Well, Gloris. If that's the case, then it sure was great travelling the 42nd Hydroverse with you."

                show alien
                
                "{i}GLAAS, gor wim ba dortis."

                scene captain
                
                "{i}Heh, I guess you're right, Bondis. Let's do this!"

                "{b}FIN{/b}"

                "..."

                "The audience is confused."

                "The lights come back on and Squishy realizes no one really liked his movie."

                play sound badending

                "Squishy heads home to find a new career tomorrow."

                return
            
            label romance:

                play sound good

                "Squishy distills every emotion he's ever experienced into the words he puts on the page."

                "A year and a half later, the movie is premiering."

                show romance discuss

                "{i}No matter what happens, I won't forget you.{/i}"

                "{i}I know you won't, Gladys.{/i}"

                show romance 1

                "{i}Well, you better get going. A wedding won't wait forever.{/i}"

                "{i}When am I going to see you again?{/i}"

                show romance turn away

                "{i}At your next one.{/i}"

                "The audience laughs."

                show standing ovation

                "The lights come back on as the whole theater stands up and erupts in applause."

                s "Thank you all so much for coming!"

                play sound ending

                "Squishy heads out celebrate, happy with his successful career."
                
                return

    label salad:

        play sound good

        s "I'll have the salad, please."

        w "Sounds good, sir. I'll get that right away for you two."

        sh "Thank you."

        "The two continue their conversation for a bit while waiting for the food."

        show salad
        
        w "Here you go. The sushi and the salad."

        sh "Thank you so much, this looks great."

        s "Yeah, thank you."

        "Squishy looks at his food."

        "It looks great!"

        s "Wow, this is delicious."

        sh "Mine, too."

        scene date continue

        "The couple finish out their meal, getting along great on the way. Squishy foots the bill, like the gentleball he is."
        
        s "I had a lot of fun tonight."

        sh "Oh. You're heading home?"

        s "I mean, I thought the date was over since dinner was."

        sh "...I don't have anywhere to be."

        s "Me neither."

        sh "What should we do now?"

        s "We could go see a movie?"

        sh "Yeah, that sounds great!"

        show happy ticket

        "They walk up to the box office at the theater."

        s "Two tickets, please!"

        sh "Wait, what movie are we seeing?"

        menu:

            s "Oh, right. Our options are:"

            "The Kissing Booth 3":
                jump booth2

            "Dances With Wolves":
                jump wolves2

        label wolves2:

            play sound bad

            s "Two tickets for {i}Dances with Wolves{/i}, please!"

            "They take their seats and the lights dim."

            show happy movie

            "Three hours later..."

            s "Well."

            sh "Yeah...that was a pretty long movie..."

            s "Good!"

            s "But very long."

            sh "Yeeeeaaaaaah..."

            s "Well, I had a good time tonight."

            sh "Uh."

            "..."

            sh "Oh, uh- yeah, I did too."

            "..."

            s "Am I going to see you again?"

            sh "Um, maybe."

            "..."

            sh "I'll see you around."

            s "Okay."

            play sound badending

            "The two part ways after what wound up being an awkward night, and they don't see each other again."

            return

        label booth2:

            play sound good

            s "Two ticket for {i}The Kissing Booth 3{/i}, please!"

            show happy movie

            "The two take their seats in the theater as the lights dim."

            "A few hours later..."

            s "That was super fun!"

            sh "Yeah, it was actually pretty cute. Stupid, but in a good way."

            s "Yeah, exactly."

            "This was the perfect movie!"

            s "I had a really great time tonight."

            sh "Me too."

            s "Am I going to see you again?"

            sh "Yeah, you will."

            s "Great."

            sh "Good night."

            s "Good night."

            "The two part ways for the night."

            show housing market

            "They continue dating for a few years!"

            "Now, they're looking to move in together."

            sh "Wow, the housing market is so tough to manage."

            s "Yeah, I know."

            menu:

                sh "Do we want to move into an apartment in the city or a house in the suburbs?"

                "Apartment":
                    jump apartment

                "House":
                    jump house

            label apartment:

                play sound neutral

                s "Let's move into an apartment!"

                sh "Great! I have an open house for us to go to."

                show apartment

                re "This is a very beautiful apartment. 3 bedrooms, 2 bathrooms."

                sh "Yeah, this is really amazing. These bay windows are beautiful."

                sh "What do you think, Squishy?"

                s "I really love it, too. We'll take it!"

                re "Well, it's not as simple as that. We've got a lot of other bids, it might be smart to have some other options."

                sh "Oh, that's disappointing."

                re "You could go all in on getting this apartment, if you really have your heart set on it."

                menu:

                    sh "What do you want to do, Squish?"

                    "Go all in on the apartment":
                        jump allin

                    "Settle for something else":
                        jump settle

                label allin:

                    play sound bad

                    s "Let's go for it! We'll get this apartment, it'll be totally fine!"

                    "This was wishful thinking."

                    "The urban housing market is WAY too competitive and the places are just too darn expensive!"

                    "They get the apartment, but the fight for it drains Squishy."

                    show break up

                    s "Finally! The apartment is ours!"

                    sh "Squishy, we need to talk."

                    s "Talk can wait, we need to move!"

                    sh "Squishy."

                    "..."

                    s "What? What's wrong, we got the apartment."

                    sh "And you've become a different person because of it."

                    sh "You're not the sweet ball I met on the beach that day anymore."

                    s "What?"

                    sh "You're cold. I'm sorry but this is over."

                    scene apartment alone

                    s "..."

                    play sound badending

                    "Squishy goes to bed alone his brand new apartment."

                    return

                label settle:

                    play sound bad

                    s "We can look for other places. As long as we're together, I don't care where we live."

                    "After a brief search, the couple winds up in a boat house."

                    show boat house

                    sh "I don't really understand why this is the place we chose."

                    s "Why not?"

                    sh "Because I'm a shark. Why would I live ON the water, when I can just live IN the water?"

                    s "Shark, it's okay. It's a nice place, it'll feel like home before you know it."

                    "It doesn't."

                    "The place is nice, it's just a little uncomfortable."

                    play sound badending

                    "The two are together forever, but the awkwardness of the house creates distance and they live unhappily."
                    
                    return

            label house:

                play sound good

                s "Let's move into a house!"

                sh "Great! I have an open house we can go to."

                show house

                "The couple move into a beautiful home in the suburbs with a great yard."

                show public school

                "A few years later, they're married and have children! Squishy is wearing glasses, to show that time has passed."

                "They're touring schools, trying to decide where to send the kids."

                sh "Do you like this place BillBob?"

                bb "I like all the dirt!"

                j "Yeah, it's very dirty."

                s "I just got out of meeting with some of the teachers, they seem great."

                sh "That's good, I'm just worried it's not {i}prestigious{/i} enough or something. I don't know."

                s "Well, we could always send them to a private school."

                menu:

                    "What should they do?"

                    "Private school":
                        jump private

                    "Public school":
                        jump public

                label private:

                    play sound bad
                    
                    s "Let's send them to private school."

                    sh "Okay, I trust you."

                    "They send their kids to a private school, from elementary to high school."

                    "The kids are both incredibly smart. BillBob becomes a doctor and J'Becky becomes a lawyer."

                    "They're both very successful!"

                    "But..."

                    show nursing home

                    "Being at strict boarding schools their whole lives kind of stunted them."

                    "They're not entirely {i}available{/i} for their parents."

                    "Several decades later, they don't want to care for their elderly parents."

                    play sound badending

                    "Squishy spends his last years in an old age home."

                    return

                label public:

                    play sound good

                    s "Let's send them to public school."

                    sh "Okay, I trust you."

                    "They send their kids to the local public school system."

                    "The schools are nice, if a bit rundown. The kids don't get excellent grades or go to excellent colleges..."

                    "But they're happy. BillBob is a plumber and J'Becky is a teacher at her former elementary school!"

                    show grown old
                    
                    "Several decades later, Squishy and Shark are in their 80's. Their children's families are visiting them."

                    "They sit together on the porch of the house they bought so many years ago, watching their swaths of grandchildren run around."

                    "Squishy realizes he had a pretty great adventure."

                    play sound bestending

                    "{b}BEST ENDING{/b}"

                    return