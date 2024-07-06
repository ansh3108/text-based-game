print("Welcome to the Haunted Mansion!")
print("You are a distant family member of a rich millionaire who has just passed away, leaving this mansion to you.")
print("As the newfound owner, you decide to pay a visit to the mansion.")
print("The house is dated, creaky, and falling apart. You walk in the front door.")
print("Do you want to enter the living room or the dining room?")

roomChoice = input("> ")

if roomChoice.lower() == "living room":
    print("You enter the living room.")
    print("As you walk in, you see a sleeping pitbull guarding some gold jewelry.")
    print("Do you want to steal the jewelry from the pitbull?")

    pitBullChoice = input("> ")

    if pitBullChoice.lower() == "yes":
        print("You attempt to steal the jewelry, but it wakes up and rips you to shreds.")
        print("You are now dead.")
    elif pitBullChoice.lower() == "no":
        print("You decide not to steal the dog's jewelry.")
        print("Suddenly, you notice a staircase leading down to a basement. Do you want to explore the basement?")
        
        exploreBasement = input("> ")
        
        if exploreBasement.lower() == "yes":
            print("You cautiously descend into the basement.")
            print("It's dimly lit and filled with cobwebs. You hear faint whispers echoing.")
            print("At the far end, there's an old chest. Do you want to open it?")
            
            openChest = input("> ")
            
            if openChest.lower() == "yes":
                print("You open the chest and find ancient scrolls and a mysterious amulet.")
                print("As you examine the items, you feel a chill down your spine.")
                print("Suddenly, the amulet glows brightly and transports you to another realm.")
                print("You find yourself facing a ghostly apparition who offers you a choice.")
                print("Do you accept the ghost's offer or try to escape back through the amulet?")
                
                ghostOffer = input("> ")
                
                if ghostOffer.lower() == "accept":
                    print("You accept the ghost's offer and gain supernatural powers, but lose your humanity.")
                    print("You become bound to the mansion forever, guarding its secrets.")
                elif ghostOffer.lower() == "escape":
                    print("You attempt to escape through the amulet, but it shatters, trapping you in the other realm.")
                    print("You are lost between worlds for eternity.")
                else:
                    print("You hesitate too long, and the ghost's power overwhelms you.")
                    print("You become a specter trapped in the mansion, forever haunting its halls.")
            
            elif openChest.lower() == "no":
                print("You decide not to open the chest.")
                print("You turn to leave the basement, but the staircase suddenly collapses behind you.")
                print("Trapped, you search desperately for another way out.")
                print("Do you look for a hidden passage or try to break through a wall?")
                
                escapeChoice = input("> ")
                
                if escapeChoice.lower() == "hidden passage":
                    print("You discover a hidden passage leading to a forgotten crypt.")
                    print("Inside, you find an old diary detailing the mansion's dark history.")
                    print("Reading it, you learn the truth about your family's curse.")
                    print("You decide to break the curse or embrace its power.")
                elif escapeChoice.lower() == "break through wall":
                    print("You attempt to break through the wall, but trigger a collapse that buries you alive.")
                    print("Your screams echo through the mansion, unheard by the living.")
                else:
                    print("Your indecision leaves you vulnerable.")
                    print("The mansion's malevolent presence consumes your spirit.")
        
        elif exploreBasement.lower() == "no":
            print("You decide not to explore the basement.")
            print("As you turn to leave the living room, you hear a haunting melody coming from upstairs.")
            print("Do you investigate the music or leave the mansion?")
            
            investigateMusic = input("> ")
            
            if investigateMusic.lower() == "investigate":
                print("You cautiously climb the stairs to the second floor.")
                print("The music leads you to a dusty old music room.")
                print("Inside, a grand piano plays itself, its keys moving as if by ghostly hands.")
                print("Do you approach the piano or try to stop the music?")
                
                approachPiano = input("> ")
                
                if approachPiano.lower() == "approach":
                    print("You approach the piano, mesmerized by its supernatural performance.")
                    print("Suddenly, the music stops, and a shadowy figure materializes beside you.")
                    print("It gestures toward a portrait on the wall. Do you examine the portrait?")
                    
                    examinePortrait = input("> ")
                    
                    if examinePortrait.lower() == "yes":
                        print("You examine the portrait and realize it depicts your ancestor, the mansion's former owner.")
                        print("The figure beside you whispers a cryptic message about breaking a curse.")
                        print("Do you heed the figure's advice or try to leave the mansion?")
                        
                        heedAdvice = input("> ")
                        
                        if heedAdvice.lower() == "heed":
                            print("You follow the figure's guidance, uncovering hidden clues and secrets.")
                            print("With each revelation, you feel closer to understanding the mansion's mysteries.")
                            print("You may yet find a way to free its restless spirits.")
                        elif heedAdvice.lower() == "leave":
                            print("You try to leave, but find the mansion's doors mysteriously locked.")
                            print("Trapped, you wander its halls forever, haunted by the ghostly figure.")
                        else:
                            print("Your uncertainty invites the mansion's malevolent forces.")
                            print("You become another lost soul bound to its endless torment.")
                    
                    elif examinePortrait.lower() == "no":
                        print("You decide not to examine the portrait.")
                        print("The figure beside you fades away, leaving you alone with the eerie silence.")
                        print("You feel an overwhelming urge to leave the mansion immediately.")
                        print("Do you attempt to escape or stay and confront the unknown?")
                        
                        confrontUnknown = input("> ")
                        
                        if confrontUnknown.lower() == "escape":
                            print("You rush towards the exit, but the mansion's layout seems to shift.")
                            print("Every turn leads you back to where you started.")
                            print("In despair, you realize you're trapped in a maze of the mansion's design.")
                        elif confrontUnknown.lower() == "stay":
                            print("You stay, determined to uncover the mansion's secrets.")
                            print("With each step, the mansion reveals more of its dark history.")
                            print("You may yet find a way to break its curse.")
                        else:
                            print("Your hesitation seals your fate.")
                            print("The mansion's malevolent presence claims you as its own.")
                
                elif approachPiano.lower() == "stop":
                    print("You try to stop the music, but the piano's keys move faster, playing an unsettling melody.")
                    print("The room grows colder, and shadowy hands materialize around you.")
                    print("Do you flee the music room or try to confront the spirits?")
                    
                    confrontSpirits = input("> ")
                    
                    if confrontSpirits.lower() == "flee":
                        print("You flee the music room, running down the stairs.")
                        print("The mansion seems to conspire against you, its corridors twisting and turning.")
                        print("Lost and disoriented, you stumble upon a hidden passage.")
                        print("Do you enter the passage or keep searching for an exit?")
                        
                        enterPassage = input("> ")
                        
                        if enterPassage.lower() == "enter":
                            print("You enter the passage and find yourself in a forgotten part of the mansion.")
                            print("Here, ancient artifacts and arcane symbols adorn the walls.")
                            print("You may have stumbled upon the key to unraveling the mansion's mysteries.")
                        elif enterPassage.lower() == "keep searching":
                            print("You keep searching, hoping to find a way out of the labyrinthine mansion.")
                            print("Every step feels like a descent into madness as the mansion toys with your sanity.")
                        else:
                            print("Your indecision proves fatal.")
                            print("The spirits of the mansion claim you, adding your essence to their eternal torment.")
                    
                    elif confrontSpirits.lower() == "confront":
                        print("You confront the spirits, demanding answers.")
                        print("They surround you, whispering tales of betrayal and tragedy.")
                        print("In their presence, you feel the weight of centuries of sorrow.")
                        print("Do you listen to their stories or reject their existence?")
                        
                        listenStories = input("> ")
                        
                        if listenStories.lower() == "listen":
                            print("You listen to the spirits' stories, empathizing with their pain.")
                            print("Moved by compassion, you vow to help them find peace.")
                            print("Together, you may uncover the truth behind the mansion's curse.")
                        elif listenStories.lower() == "reject":
                            print("You reject the spirits' existence, refusing to believe in their tales.")
                            print("Enraged, the spirits lash out, condemning you to a fate worse than death.")
                            print("Your soul becomes trapped in the mansion, a puppet of its vengeful spirits.")
                        else:
                            print("Your uncertainty fuels the spirits' anger.")
                            print("They consume your essence, adding your spirit to their spectral ranks.")
                    
                    else:
                        print("Your hesitation invites the spirits' wrath.")
                        print("They overwhelm you, dragging you into their realm of eternal torment.")
                
                else:
                    print("Your indecision proves fatal.")
                    print("The piano's haunting melody consumes your mind, driving you to madness.")
            
            elif investigateMusic.lower() == "leave":
                print("You decide to leave the mansion, unsettled by the eerie music.")
                print("As you reach for the door, it slams shut on its own, blocking your exit.")
                print("Trapped, you hear the music growing louder, drawing you back into the mansion's depths.")
                print("Do you search for another exit or confront the source of the music?")
                
                confrontMusicSource = input("> ")
                
                if confrontMusicSource.lower() == "search for exit":
                    print("You search desperately for another way out, but the mansion's layout seems to change.")
                    print("Every corridor leads you back to where you started, trapped in an endless loop.")
                    print("In despair, you realize you're caught in the mansion's sinister game.")
                elif confrontMusicSource.lower() == "confront music":
                    print("You confront the source of the music, following its haunting melody.")
                    print("It leads you to a hidden chamber where a spectral orchestra plays.")
                    print("Do you join the orchestra or try to silence the music?")
                    
                    joinOrchestra = input("> ")
                    
                    if joinOrchestra.lower() == "join":
                        print("You join the spectral orchestra, playing alongside ghostly musicians.")
                        print("The music transports you to another realm, where time and space blur.")
                        print("You may find peace or be lost forever in the symphony of the dead.")
                    elif joinOrchestra.lower() == "silence":
                        print("You try to silence the music, but the orchestra's intensity grows.")
                        print("The conductor, a ghostly figure, gestures for you to stop.")
                        print("Do you heed the conductor's command or resist?")
                        
                        heedCommand = input("> ")
                        
                        if heedCommand.lower() == "heed":
                            print("You heed the conductor's command, lowering your instrument.")
                            print("The music fades, and the orchestra disperses, leaving you alone in the chamber.")
                            print("You feel a sense of relief, but the mansion's mysteries remain unresolved.")
                        elif heedCommand.lower() == "resist":
                            print("You resist the conductor's command, playing louder in defiance.")
                            print("The orchestra's music swells to a deafening crescendo, consuming you.")
                            print("You become part of the eternal symphony, forever bound to the mansion.")
                        else:
                            print("Your hesitation proves costly.")
                            print("The orchestra's spectral music overwhelms your senses, trapping you in its melody.")
                    
                    else:
                        print("Your indecision invites the mansion's malevolent forces.")
                        print("The orchestra's music ensnares you, merging your soul with its haunting melody.")
                
                else:
                    print("Your indecision seals your fate.")
                    print("The mansion's malevolent presence claims you as its own.")
            
            else:
                print("Your hesitation invites the mansion's malevolent forces.")
                print("Its spirits consume your essence, trapping you in a nightmare of endless echoes.")
        
        else:
            print("Your indecision proves fatal.")
            print("The basement's shadows envelop you, dragging you into the mansion's dark depths.")
    
    else:
        print("Your indecision proves fatal.")
        print("The pitbull awakens, its eyes glowing with fury as it lunges towards you.")
        print("You are no match for its ferocity.")
        
elif roomChoice.lower() == "dining room":
    print("You chose to go into the dining room.")
    print("As you walk in, you see a shiny vase on the table.")
    print("Do you want to open the vase?")

    vaseChoice = input("> ")

    if vaseChoice.lower() == "yes":
        print("You cautiously open the vase and find a dusty old key inside.")
        print("The key looks ancient, perhaps a clue to the mansion's secrets.")
        print("Do you keep the key or discard it?")
        
        keepKey = input("> ")
        
        if keepKey.lower() == "keep":
            print("You decide to keep the key, sensing its importance.")
            print("As you pocket it, you notice a portrait on the wall with strange symbols.")
            print("Do you examine the portrait or search for more clues?")
            
            examinePortrait = input("> ")
            
            if examinePortrait.lower() == "examine":
                print("You examine the portrait closely, deciphering the hidden symbols.")
                print("They seem to point to a hidden compartment in the dining room.")
                print("Do you search for the compartment or investigate elsewhere?")
                
                searchCompartment = input("> ")
                
                if searchCompartment.lower() == "search":
                    print("You search the dining room, eventually finding a loose panel under the floor.")
                    print("Inside, you discover a hidden cache of valuable artifacts.")
                    print("You may have stumbled upon the mansion's lost treasure.")
                elif searchCompartment.lower() == "investigate":
                    print("You decide to investigate elsewhere in the mansion.")
                    print("As you explore, you hear faint whispers from the library.")
                    print("Do you investigate the library or continue searching?")
                    
                    investigateLibrary = input("> ")
                    
                    if investigateLibrary.lower() == "library":
                        print("You enter the library, filled with dusty tomes and ancient manuscripts.")
                        print("One book catches your eye, its pages glowing faintly.")
                        print("Do you open the book or leave it be?")
                        
                        openBook = input("> ")
                        
                        if openBook.lower() == "open":
                            print("You cautiously open the book, unleashing a burst of mystical energy.")
                            print("The energy surrounds you, granting fleeting visions of the mansion's past.")
                            print("You glimpse the struggles and triumphs of its former inhabitants.")
                        elif openBook.lower() == "leave":
                            print("You decide not to open the mysterious book.")
                            print("As you turn to leave the library, you hear footsteps behind you.")
                            print("A spectral figure materializes, blocking your path.")
                            print("Do you confront the figure or try to flee?")
                            
                            confrontFigure = input("> ")
                            
                            if confrontFigure.lower() == "confront":
                                print("You confront the spectral figure, demanding answers.")
                                print("It gestures towards a hidden passage in the library's wall.")
                                print("Do you enter the passage or demand more answers?")
                                
                                enterPassage = input("> ")
                                
                                if enterPassage.lower() == "enter":
                                    print("You enter the hidden passage and find a forgotten study.")
                                    print("Inside, you uncover journals detailing arcane rituals and forbidden knowledge.")
                                    print("You may have found the key to unraveling the mansion's darkest secrets.")
                                elif enterPassage.lower() == "demand":
                                    print("You demand more answers from the spectral figure, but it fades away.")
                                    print("Left alone, you feel a chill in the air, as if the mansion itself is watching.")
                                    print("You may have stirred something ancient and malevolent.")
                                else:
                                    print("Your indecision invites the mansion's malevolent forces.")
                                    print("They consume your essence, trapping you in a nightmare of forgotten truths.")
                            
                            elif confrontFigure.lower() == "flee":
                                print("You try to flee the library, but the spectral figure blocks your path.")
                                print("It reaches out, its touch draining your strength.")
                                print("With nowhere to run, you succumb to its haunting presence.")
                                print("Your spirit becomes trapped in the library, forever a prisoner of its secrets.")
                            
                            else:
                                print("Your hesitation seals your fate.")
                                print("The spectral figure's presence overwhelms you, binding your fate to the mansion.")
                        
                        else:
                            print("Your indecision proves costly.")
                            print("The library's mystic energies react, sealing your fate within its walls.")
                    
                    elif investigateLibrary.lower() == "continue":
                        print("You continue searching the mansion, hoping to uncover more clues.")
                        print("Every room holds fragments of its past, but no clear answers.")
                        print("The mansion seems determined to keep its secrets buried.")
                    else:
                        print("Your hesitation invites the mansion's malevolent forces.")
                        print("Its echoes consume your thoughts, leaving you lost in the labyrinth of time.")
                
                else:
                    print("Your indecision proves fatal.")
                    print("The mansion's darkness engulfs you, leaving you forever bound to its mysteries.")
            
            elif examinePortrait.lower() == "search for clues":
                print("You decide to search for more clues elsewhere in the mansion.")
                print("As you explore, you hear whispers coming from the attic.")
                print("Do you investigate the attic or continue searching?")
                
                investigateAttic = input("> ")
                
                if investigateAttic.lower() == "attic":
                    print("You climb up to the attic, filled with forgotten relics and dusty memories.")
                    print("Amidst the cobwebs, you find an old chest covered in strange symbols.")
                    print("Do you open the chest or leave it undisturbed?")
                    
                    openChest = input("> ")
                    
                    if openChest.lower() == "open":
                        print("You open the chest and find a collection of letters and a faded photograph.")
                        print("They hint at a tragic love story, intertwined with the mansion's history.")
                        print("You may have uncovered the key to understanding its haunting past.")
                    elif openChest.lower() == "leave":
                        print("You decide not to open the mysterious chest.")
                        print("As you turn to leave the attic, you hear a faint whisper behind you.")
                        print("A ghostly figure materializes, reaching out as if to show you something.")
                        print("Do you confront the figure or try to flee?")
                        
                        confrontGhost = input("> ")
                        
                        if confrontGhost.lower() == "confront":
                            print("You confront the ghostly figure, its presence chilling the air around you.")
                            print("It gestures towards a hidden compartment in the attic's floorboards.")
                            print("Do you search the compartment or demand answers?")
                            
                            searchCompartment = input("> ")
                            
                            if searchCompartment.lower() == "search":
                                print("You search the compartment and find a locked journal.")
                                print("The journal seems to detail the mansion's dark secrets and rituals.")
                                print("You may have found the key to uncovering its deepest mysteries.")
                            elif searchCompartment.lower() == "demand":
                                print("You demand answers from the ghostly figure, but it fades away.")
                                print("Left alone, you feel a chill in the air, as if the attic itself is watching.")
                                print("You may have disturbed something ancient and vengeful.")
                            else:
                                print("Your indecision seals your fate.")
                                print("The attic's spirits consume your essence, leaving you a prisoner of its shadows.")
                        
                        elif confrontGhost.lower() == "flee":
                            print("You try to flee the attic, but the ghostly figure blocks your path.")
                            print("Its presence drains your strength, leaving you paralyzed with fear.")
                            print("With nowhere to run, you become a prisoner of the attic's haunting echoes.")
                        
                        else:
                            print("Your hesitation proves fatal.")
                            print("The ghostly figure's presence overwhelms you, binding your fate to the attic's secrets.")
                    
                    else:
                        print("Your indecision proves costly.")
                        print("The attic's spirits react, sealing your fate within its dusty confines.")
                
                elif investigateAttic.lower() == "continue":
                    print("You continue searching the mansion, hoping to uncover more clues.")
                    print("Every room holds fragments of its past, but no clear answers.")
                    print("The mansion seems determined to keep its secrets buried.")
                else:
                    print("Your hesitation invites the mansion's malevolent forces.")
                    print("Its echoes consume your thoughts, leaving you lost in the labyrinth of time.")
            
            else:
                print("Your hesitation proves fatal.")
                print("The mansion's darkness engulfs you, leaving you forever bound to its mysteries.")
        
        elif keepKey.lower() == "discard":
            print("You decide to discard the key, dismissing it as insignificant.")
            print("As you leave the dining room, you hear a faint clicking sound behind you.")
            print("Do you investigate the sound or continue exploring?")
            
            investigateSound = input("> ")
            
            if investigateSound.lower() == "investigate":
                print("You cautiously trace the sound to a hidden mechanism in the wall.")
                print("With a click, a secret door opens, revealing a passage to the cellar.")
                print("Do you descend into the cellar or search for more hidden passages?")
                
                descendCellar = input("> ")
                
                if descendCellar.lower() == "descend":
                    print("You descend into the cellar, its air thick with ancient dust and darkness.")
                    print("As you explore, you stumble upon an old wine rack with a loose brick.")
                    print("Do you inspect the loose brick or search for more clues?")
                    
                    inspectBrick = input("> ")
                    
                    if inspectBrick.lower() == "inspect":
                        print("You inspect the loose brick and find a hidden compartment.")
                        print("Inside, there's a cryptic map leading to a forgotten cemetery.")
                        print("You may have discovered the key to unlocking the mansion's darkest secrets.")
                    elif inspectBrick.lower() == "search":
                        print("You decide to search for more clues in the cellar.")
                        print("Amidst the cobwebs, you find an old chest covered in mysterious runes.")
                        print("Do you open the chest or leave it undisturbed?")
                        
                        openChest = input("> ")
                        
                        if openChest.lower() == "open":
                            print("You cautiously open the chest and find a collection of ancient artifacts.")
                            print("They seem to hold mystical powers, resonating with the cellar's eerie atmosphere.")
                            print("You may have uncovered the key to understanding the mansion's true nature.")
                        elif openChest.lower() == "leave":
                            print("You decide not to open the mysterious chest.")
                            print("As you turn to leave the cellar, you hear a faint whisper behind you.")
                            print("A ghostly figure materializes, reaching out as if to show you something.")
                            print("Do you confront the figure or try to flee?")
                            
                            confrontGhost = input("> ")
                            
                            if confrontGhost.lower() == "confront":
                                print("You confront the ghostly figure, its presence chilling the air around you.")
                                print("It gestures towards a hidden passage in the cellar's wall.")
                                print("Do you enter the passage or demand answers?")
                                
                                enterPassage = input("> ")
                                
                                if enterPassage.lower() == "enter":
                                    print("You enter the hidden passage and find a forgotten crypt.")
                                    print("Inside, you uncover journals detailing arcane rituals and forbidden knowledge.")
                                    print("You may have found the key to unraveling the mansion's darkest secrets.")
                                elif enterPassage.lower() == "demand":
                                    print("You demand answers from the ghostly figure, but it fades away.")
                                    print("Left alone, you feel a chill in the air, as if the cellar itself is watching.")
                                    print("You may have stirred something ancient and malevolent.")
                                else:
                                    print("Your indecision seals your fate.")
                                    print("The cellar's spirits consume your essence, leaving you a prisoner of its shadows.")
                            
                            elif confrontGhost.lower() == "flee":
                                print("You try to flee the cellar, but the ghostly figure blocks your path.")
                                print("Its presence drains your strength, leaving you paralyzed with fear.")
                                print("With nowhere to run, you become a prisoner of the cellar's haunting echoes.")
                            
                            else:
                                print("Your hesitation proves fatal.")
                                print("The ghostly figure's presence overwhelms you, binding your fate to the cellar's secrets.")
                        
                        else:
                            print("Your indecision proves costly.")
                            print("The cellar's spirits react, sealing your fate within its dusty confines.")
                    
                    else:
                        print("Your hesitation proves fatal.")
                        print("The cellar's darkness engulfs you, leaving you forever bound to its mysteries.")
                
                elif descendCellar.lower() == "search for passages":
                    print("You search for more hidden passages in the cellar, hoping to uncover its secrets.")
                    print("Every step echoes with the mansion's forgotten whispers.")
                    print("The cellar seems determined to keep its mysteries buried.")
                else:
                    print("Your hesitation invites the mansion's malevolent forces.")
                    print("Its echoes consume your thoughts, leaving you lost in the labyrinth of time.")
            
            elif investigateSound.lower() == "continue exploring":
                print("You continue exploring the mansion, searching for more hidden secrets.")
                print("Every room holds fragments of its past, but no clear answers.")
                print("The mansion seems determined to keep its secrets buried.")
            else:
                print("Your indecision invites the mansion's malevolent forces.")
                print("Its echoes consume your thoughts, leaving you lost in the labyrinth of time.")
        
        else:
            print("Your indecision proves fatal.")
            print("The mansion's darkness engulfs you, leaving you forever bound to its mysteries.")
    
    elif vaseChoice.lower() == "no":
        print("You decide not to open the shiny vase.")
        print("As you turn to leave the dining room, you hear a faint whisper from the kitchen.")
        print("Do you investigate the kitchen or continue exploring?")
        
        investigateKitchen = input("> ")
        
        if investigateKitchen.lower() == "investigate":
            print("You cautiously enter the kitchen, its old utensils and dusty shelves casting eerie shadows.")
            print("Amidst the darkness, you notice a flickering light in the pantry.")
            print("Do you investigate the pantry or search for more clues?")
            
            investigatePantry = input("> ")
            
            if investigatePantry.lower() == "pantry":
                print("You cautiously open the pantry door and find a hidden passage.")
                print("The passage leads to a forgotten cellar filled with old wine barrels.")
                print("Do you descend into the cellar or search for more hidden passages?")
                
                descendCellar = input("> ")
                
                if descendCellar.lower() == "descend":
                    print("You descend into the cellar, its air thick with ancient dust and darkness.")
                    print("As you explore, you stumble upon an old wine rack with a loose brick.")
                    print("Do you inspect the loose brick or search for more clues?")
                    
                    inspectBrick = input("> ")
                    
                    if inspectBrick.lower() == "inspect":
                        print("You inspect the loose brick and find a hidden compartment.")
                        print("Inside, there's a cryptic map leading to a forgotten cemetery.")
                        print("You may have discovered the key to unlocking the mansion's darkest secrets.")
                    elif inspectBrick.lower() == "search":
                        print("You decide to search for more clues in the cellar.")
                        print("Amidst the cobwebs, you find an old chest covered in mysterious runes.")
                        print("Do you open the chest or leave it undisturbed?")
                        
                        openChest = input("> ")
                        
                        if openChest.lower() == "open":
                            print("You cautiously open the chest and find a collection of ancient artifacts.")
                            print("They seem to hold mystical powers, resonating with the cellar's eerie atmosphere.")
                            print("You may have uncovered the key to understanding the mansion's true nature.")
                        elif openChest.lower() == "leave":
                            print("You decide not to open the mysterious chest.")
                            print("As you turn to leave the cellar, you hear a faint whisper behind you.")
                            print("A ghostly figure materializes, reaching out as if to show you something.")
                            print("Do you confront the figure or try to flee?")
                            
                            confrontGhost = input("> ")
                            
                            if confrontGhost.lower() == "confront":
                                print("You confront the ghostly figure, its presence chilling the air around you.")
                                print("It gestures towards a hidden passage in the cellar's wall.")
                                print("Do you enter the passage or demand answers?")
                                
                                enterPassage = input("> ")
                                
                                if enterPassage.lower() == "enter":
                                    print("You enter the hidden passage and find a forgotten crypt.")
                                    print("Inside, you uncover journals detailing arcane rituals and forbidden knowledge.")
                                    print("You may have found the key to unraveling the mansion's darkest secrets.")
                                elif enterPassage.lower() == "demand":
                                    print("You demand answers from the ghostly figure, but it fades away.")
                                    print("Left alone, you feel a chill in the air, as if the cellar itself is watching.")
                                    print("You may have stirred something ancient and malevolent.")
                                else:
                                    print("Your indecision seals your fate.")
                                    print("The cellar's spirits consume your essence, leaving you a prisoner of its shadows.")
                            
                            elif confrontGhost.lower() == "flee":
                                print("You try to flee the cellar, but the ghostly figure blocks your path.")
                                print("Its presence drains your strength, leaving you paralyzed with fear.")
                                print("With nowhere to run, you become a prisoner of the cellar's haunting echoes.")
                            
                            else:
                                print("Your hesitation proves fatal.")
                                print("The ghostly figure's presence overwhelms you, binding your fate to the cellar's secrets.")
                        
                        else:
                            print("Your indecision proves costly.")
                            print("The cellar's spirits react, sealing your fate within its dusty confines.")
                    
                    else:
                        print("Your hesitation proves fatal.")
                        print("The cellar's darkness engulfs you, leaving you forever bound to its mysteries.")
                
                elif descendCellar.lower() == "search for passages":
                    print("You search for more hidden passages in the cellar, hoping to uncover its secrets.")
                    print("Every step echoes with the mansion's forgotten whispers.")
                    print("The cellar seems determined to keep its mysteries buried.")
                else:
                    print("Your hesitation invites the mansion's malevolent forces.")
                    print("Its echoes consume your thoughts, leaving you lost in the labyrinth of time.")
            
            elif investigatePantry.lower() == "search for clues":
                print("You decide to search for more clues elsewhere in the mansion.")
                print("As you explore, you hear whispers coming from the attic.")
                print("Do you investigate the attic or continue searching?")
                
                investigateAttic = input("> ")
                
                if investigateAttic.lower() == "attic":
                    print("You climb up to the attic, filled with forgotten relics and dusty memories.")
                    print("Amidst the cobwebs, you find an old chest covered in strange symbols.")
                    print("Do you open the chest or leave it undisturbed?")
                    
                    openChest = input("> ")
                    
                    if openChest.lower() == "open":
                        print("You cautiously open the chest and find a collection of letters and a faded photograph.")
                        print("They hint at a tragic love story, intertwined with the mansion's history.")
                        print("You may have uncovered the key to understanding its haunting past.")
                    elif openChest.lower() == "leave":
                        print("You decide not to open the mysterious chest.")
                        print("As you turn to leave the attic, you hear a faint whisper behind you.")
                        print("A ghostly figure materializes, reaching out as if to show you something.")
                        print("Do you confront the figure or try to flee?")
                        
                        confrontGhost = input("> ")
                        
                        if confrontGhost.lower() == "confront":
                            print("You confront the ghostly figure, its presence chilling the air around you.")
                            print("It gestures towards a hidden compartment in the attic's floorboards.")
                            print("Do you search the compartment or demand more answers?")
                            
                            searchCompartment = input("> ")
                            
                            if searchCompartment.lower() == "search":
                                print("You search the compartment and find a locked journal.")
                                print("The journal seems to detail the mansion's dark secrets and rituals.")
                                print("You may have found the key to uncovering its deepest mysteries.")
                            elif searchCompartment.lower() == "demand":
                                print("You demand more answers from the spectral figure, but it fades away.")
                                print("Left alone, you feel a chill in the air, as if the attic itself is watching.")
                                print("You may have stirred something ancient and vengeful.")
                            else:
                                print("Your indecision seals your fate.")
                                print("The attic's spirits consume your essence, leaving you a prisoner of its secrets.")
                        
                        elif confrontGhost.lower() == "flee":
                            print("You try to flee the attic, but the spectral figure blocks your path.")
                            print("Its presence drains your strength, leaving you paralyzed with fear.")
                            print("With nowhere to run, you become a prisoner of the attic's haunting echoes.")
                        
                        else:
                            print("Your hesitation proves fatal.")
                            print("The spectral figure's presence overwhelms you, binding your fate to the attic's secrets.")
                    
                    else:
                        print("Your indecision proves costly.")
                        print("The attic's mystic energies react, sealing your fate within its dusty confines.")
                
                elif investigateAttic.lower() == "continue":
                    print("You continue searching the mansion, hoping to uncover more clues.")
                    print("Every room holds fragments of its past, but no clear answers.")
                    print("The mansion seems determined to keep its secrets buried.")
                else:
                    print("Your hesitation invites the mansion's malevolent forces.")
                    print("Its echoes consume your thoughts, leaving you lost in the labyrinth of time.")
            
            else:
                print("Your hesitation proves fatal.")
                print("The mansion's darkness engulfs you, leaving you forever bound to its mysteries.")
        
        elif investigateKitchen.lower() == "continue exploring":
            print("You continue exploring the mansion, searching for more hidden secrets.")
            print("Every room holds fragments of its past, but no clear answers.")
            print("The mansion seems determined to keep its secrets buried.")
        else:
            print("Your indecision invites the mansion's malevolent forces.")
            print("Its echoes consume your thoughts, leaving you lost in the labyrinth of time.")
    
    else:
        print("Your hesitation invites the mansion's malevolent forces.")
        print("Its echoes consume your thoughts, leaving you lost in the labyrinth of time.")

print("\n--- GAME OVER ---")
