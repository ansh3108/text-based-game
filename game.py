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
        print("You turn around and leave the house safely.")
    else:
        print("Invalid choice. Please enter yes or no.")

elif roomChoice.lower() == "dining room":
    print("You chose to go into the dining room.")
    print("As you walk in, you see a shiny vase on the table.")
    print("Do you want to open the vase?")

    vaseChoice = input("> ")

    if vaseChoice.lower() == "yes":
        print("You open the vase and find a pile of bones!")
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

