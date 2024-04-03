import pytest
import random
import pokemon
import assessMeTester_StringSimilarity
#TO RUN pytest --tb=short -s

def test_make_database(capsys, monkeypatch, printFeedback=True):
        success = True
        assertMessage = "" ##Assert message

        ##MODIFY
        testerName = "test_make_database"
        functionName = "make_database"

        expected = {43: (43, 'Abra', 'Psychic'), 1: (1, 'Alakazam', 'Psychic'), 23: (23, 'Arcanine', 'Fire'), 17: (17, 'Beedrill', 'Grass'), 91: (91, 'Bill', 'Trainer'), 2: (2, 'Blastoise', 'Water'), 44: (44, 'Bulbasaur', 'Grass'), 45: (45, 'Caterpie', 'Grass'), 3: (3, 'Chansey', 'Air'), 4: (4, 'Charizard', 'Fire'), 46: (46, 'Charmander', 'Fire'), 24: (24, 'Charmeleon', 'Fire'), 5: (5, 'Clefairy', 'Air'), 70: (70, 'Clefairy Doll', 'Trainer'), 71: (71, 'Computer Search', 'Trainer'), 80: (80, 'Defender', 'Trainer'), 72: (72, 'Devolution Spray', 'Trainer'), 25: (25, 'Dewgong', 'Water'), 47: (47, 'Diglett', 'Rock'), 48: (48, 'Doduo', 'Air'), 18: (18, 'Dragonair', 'Air'), 26: (26, 'Dratini', 'Air'), 49: (49, 'Drowzee', 'Psychic'), 19: (19, 'Dugtrio', 'Rock'), 20: (20, 'Electabuzz', 'Electric'), 21: (21, 'Electrode', 'Electric'), 96: (96, 'Energy - Colorless', 'Energy'), 100: (100, 'Energy - Elec', 'Energy'), 98: (98, 'Energy - Fire', 'Energy'), 99: (99, 'Energy - Grass', 'Energy'), 101: (101, 'Energy - Psychic', 'Energy'), 97: (97, 'Energy - Fight', 'Energy'), 102: (102, 'Energy - Water', 'Energy'), 92: (92, 'Energy Removal', 'Trainer'), 81: (81, 'Energy Retrieval', 'Trainer'), 27: (27, "Farfetcch'd", 'Air'), 82: (82, 'Full Heal', 'Trainer'), 50: (50, 'Gastly', 'Psychic'), 28: (28, 'Growlithe', 'Fire'), 93: (93, 'Gust of Wind', 'Trainer'), 6: (6, 'Gyarados', 'Water'), 29: (29, 'Haunter', 'Psychic'), 7: (7, 'Hitmonchan', 'Rock'), 73: (73, 'Imposter Professor Oak', 'Trainer'), 74: (74, 'Item Finder', 'Trainer'), 30: (30, 'IvySaur', 'Grass'), 31: (31, 'Jynx', 'Psychic'), 32: (32, 'Kadabra', 'Psychic'), 33: (33, 'Kakuna', 'Grass'), 51: (51, 'Koffing', 'Grass'), 75: (75, 'Lass', 'Trainer'), 8: (8, 'Machamp', 'Rock'), 34: (34, 'Machoke', 'Rock'), 52: (52, 'Machop', 'Rock'), 35: (35, 'Magikarp', 'Water'), 36: (36, 'Magmar', 'Fire'), 53: (53, 'Magnemite', 'Electric'), 9: (9, 'Magneton', 'Electric'), 83: (83, 'Maintenance', 'Trainer'), 54: (54, 'Metapod', 'Grass'), 10: (10, 'MewTwo', 'Psychic'), 11: (11, 'NidoKing', 'Grass'), 55: (55, 'Nidoran', 'Grass'), 37: (37, 'Nidorino', 'Grass'), 12: (12, 'Ninetales', 'Fire'), 56: (56, 'Onix', 'Rock'), 22: (22, 'Pidgeotto', 'Air'), 57: (57, 'Pidgey', 'Air'), 58: (58, 'Pikachu', 'Electric'), 84: (84, 'PlusPower', 'Trainer'), 87: (87, 'Pokedex', 'Trainer'), 76: (76, 'Pokemon Breeder', 'Trainer'), 85: (85, 'Pokemon Center', 'Trainer'), 86: (86, 'Pokemon Flute', 'Trainer'), 77: (77, 'Pokemon Trader', 'Trainer'), 59: (59, 'Poliwag', 'Water'), 38: (38, 'Poliwhirl', 'Water'), 13: (13, 'Poliwrath', 'Water'), 60: (60, 'Ponyta', 'Fire'), 39: (39, 'Porygon', 'Air'), 94: (94, 'Potion', 'Trainer'), 88: (88, 'Professor Oak', 'Trainer'), 14: (14, 'Raichu', 'Electric'), 40: (40, 'Raticate', 'Air'), 61: (61, 'Rattata', 'Air'), 89: (89, 'Revive', 'Trainer'), 62: (62, 'Sandshrew', 'Rock'), 78: (78, 'Scoop Up', 'Trainer'), 41: (41, 'Seel', 'Water'), 63: (63, 'Squirtle', 'Water'), 64: (64, 'Starmie', 'Water'), 65: (65, 'Staryu', 'Water'), 90: (90, 'Super Potion', 'Trainer'), 79: (79, 'Super Energy Removal', 'Trainer'), 95: (95, 'Switch', 'Trainer'), 66: (66, 'Tangela', 'Grass'), 15: (15, 'Venusaur', 'Grass'), 67: (67, 'Voltorb', 'Electric'), 68: (68, 'Vulpix', 'Fire'), 42: (42, 'Wartortle', 'Water'), 69: (69, 'Weedle', 'Grass'), 16: (16, 'Zapdos', 'Electric')}
          
        try:

            # invoke
            result = pokemon.make_database("data/pokemon.csv")
       
            
            if result==None:
                 success=False
                 assertMessage="The function must return a value!"
                 raise
             
            # Part for string comparison!
            if result==expected:
                assert True
            else:
                success = False
                assertMessage=f"The {functionName} is not correct!\nExpected:{expected}"
                assertMessage+=f"\nReturned:{result}"
        except AttributeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except TypeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except AssertionError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except:
            pass
        
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "\n******************************************* "+testerName+ " *****************\n"
        feedback = feedback + "\033[93m"+ assertMessage+"\033[0m"+"\n\n"
        feedback = feedback + "\n\033[91m*******************************************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
        feedback = feedback + "\n\n\n"

        if printFeedback and len(assertMessage)>0:
            print(feedback)
        assert success,assertMessage



def test_print_database(capsys, monkeypatch, printFeedback=True):

    inputs = {43: (43, 'Abra', 'Psychic'), 1: (1, 'Alakazam', 'Psychic'), 23: (23, 'Arcanine', 'Fire'), 17: (17, 'Beedrill', 'Grass'), 91: (91, 'Bill', 'Trainer'), 2: (2, 'Blastoise', 'Water'), 44: (44, 'Bulbasaur', 'Grass'), 45: (45, 'Caterpie', 'Grass'), 3: (3, 'Chansey', 'Air'), 4: (4, 'Charizard', 'Fire'), 46: (46, 'Charmander', 'Fire'), 24: (24, 'Charmeleon', 'Fire'), 5: (5, 'Clefairy', 'Air'), 70: (70, 'Clefairy Doll', 'Trainer'), 71: (71, 'Computer Search', 'Trainer'), 80: (80, 'Defender', 'Trainer'), 72: (72, 'Devolution Spray', 'Trainer'), 25: (25, 'Dewgong', 'Water'), 47: (47, 'Diglett', 'Rock'), 48: (48, 'Doduo', 'Air'), 18: (18, 'Dragonair', 'Air'), 26: (26, 'Dratini', 'Air'), 49: (49, 'Drowzee', 'Psychic'), 19: (19, 'Dugtrio', 'Rock'), 20: (20, 'Electabuzz', 'Electric'), 21: (21, 'Electrode', 'Electric'), 96: (96, 'Energy - Colorless', 'Energy'), 100: (100, 'Energy - Elec', 'Energy'), 98: (98, 'Energy - Fire', 'Energy'), 99: (99, 'Energy - Grass', 'Energy'), 101: (101, 'Energy - Psychic', 'Energy'), 97: (97, 'Energy - Fight', 'Energy'), 102: (102, 'Energy - Water', 'Energy'), 92: (92, 'Energy Removal', 'Trainer'), 81: (81, 'Energy Retrieval', 'Trainer'), 27: (27, "Farfetcch'd", 'Air'), 82: (82, 'Full Heal', 'Trainer'), 50: (50, 'Gastly', 'Psychic'), 28: (28, 'Growlithe', 'Fire'), 93: (93, 'Gust of Wind', 'Trainer'), 6: (6, 'Gyarados', 'Water'), 29: (29, 'Haunter', 'Psychic'), 7: (7, 'Hitmonchan', 'Rock'), 73: (73, 'Imposter Professor Oak', 'Trainer'), 74: (74, 'Item Finder', 'Trainer'), 30: (30, 'IvySaur', 'Grass'), 31: (31, 'Jynx', 'Psychic'), 32: (32, 'Kadabra', 'Psychic'), 33: (33, 'Kakuna', 'Grass'), 51: (51, 'Koffing', 'Grass'), 75: (75, 'Lass', 'Trainer'), 8: (8, 'Machamp', 'Rock'), 34: (34, 'Machoke', 'Rock'), 52: (52, 'Machop', 'Rock'), 35: (35, 'Magikarp', 'Water'), 36: (36, 'Magmar', 'Fire'), 53: (53, 'Magnemite', 'Electric'), 9: (9, 'Magneton', 'Electric'), 83: (83, 'Maintenance', 'Trainer'), 54: (54, 'Metapod', 'Grass'), 10: (10, 'MewTwo', 'Psychic'), 11: (11, 'NidoKing', 'Grass'), 55: (55, 'Nidoran', 'Grass'), 37: (37, 'Nidorino', 'Grass'), 12: (12, 'Ninetales', 'Fire'), 56: (56, 'Onix', 'Rock'), 22: (22, 'Pidgeotto', 'Air'), 57: (57, 'Pidgey', 'Air'), 58: (58, 'Pikachu', 'Electric'), 84: (84, 'PlusPower', 'Trainer'), 87: (87, 'Pokedex', 'Trainer'), 76: (76, 'Pokemon Breeder', 'Trainer'), 85: (85, 'Pokemon Center', 'Trainer'), 86: (86, 'Pokemon Flute', 'Trainer'), 77: (77, 'Pokemon Trader', 'Trainer'), 59: (59, 'Poliwag', 'Water'), 38: (38, 'Poliwhirl', 'Water'), 13: (13, 'Poliwrath', 'Water'), 60: (60, 'Ponyta', 'Fire'), 39: (39, 'Porygon', 'Air'), 94: (94, 'Potion', 'Trainer'), 88: (88, 'Professor Oak', 'Trainer'), 14: (14, 'Raichu', 'Electric'), 40: (40, 'Raticate', 'Air'), 61: (61, 'Rattata', 'Air'), 89: (89, 'Revive', 'Trainer'), 62: (62, 'Sandshrew', 'Rock'), 78: (78, 'Scoop Up', 'Trainer'), 41: (41, 'Seel', 'Water'), 63: (63, 'Squirtle', 'Water'), 64: (64, 'Starmie', 'Water'), 65: (65, 'Staryu', 'Water'), 90: (90, 'Super Potion', 'Trainer'), 79: (79, 'Super Energy Removal', 'Trainer'), 95: (95, 'Switch', 'Trainer'), 66: (66, 'Tangela', 'Grass'), 15: (15, 'Venusaur', 'Grass'), 67: (67, 'Voltorb', 'Electric'), 68: (68, 'Vulpix', 'Fire'), 42: (42, 'Wartortle', 'Water'), 69: (69, 'Weedle', 'Grass'), 16: (16, 'Zapdos', 'Electric')}
        
    expected_output = """NUMBER: 1  CARD: (1, 'Alakazam', 'Psychic')
NUMBER: 2  CARD: (2, 'Blastoise', 'Water')
NUMBER: 3  CARD: (3, 'Chansey', 'Air')
NUMBER: 4  CARD: (4, 'Charizard', 'Fire')
NUMBER: 5  CARD: (5, 'Clefairy', 'Air')
NUMBER: 6  CARD: (6, 'Gyarados', 'Water')
NUMBER: 7  CARD: (7, 'Hitmonchan', 'Rock')
NUMBER: 8  CARD: (8, 'Machamp', 'Rock')
NUMBER: 9  CARD: (9, 'Magneton', 'Electric')
NUMBER: 10  CARD: (10, 'MewTwo', 'Psychic')
NUMBER: 11  CARD: (11, 'NidoKing', 'Grass')
NUMBER: 12  CARD: (12, 'Ninetales', 'Fire')
NUMBER: 13  CARD: (13, 'Poliwrath', 'Water')
NUMBER: 14  CARD: (14, 'Raichu', 'Electric')
NUMBER: 15  CARD: (15, 'Venusaur', 'Grass')
NUMBER: 16  CARD: (16, 'Zapdos', 'Electric')
NUMBER: 17  CARD: (17, 'Beedrill', 'Grass')
NUMBER: 18  CARD: (18, 'Dragonair', 'Air')
NUMBER: 19  CARD: (19, 'Dugtrio', 'Rock')
NUMBER: 20  CARD: (20, 'Electabuzz', 'Electric')
NUMBER: 21  CARD: (21, 'Electrode', 'Electric')
NUMBER: 22  CARD: (22, 'Pidgeotto', 'Air')
NUMBER: 23  CARD: (23, 'Arcanine', 'Fire')
NUMBER: 24  CARD: (24, 'Charmeleon', 'Fire')
NUMBER: 25  CARD: (25, 'Dewgong', 'Water')
NUMBER: 26  CARD: (26, 'Dratini', 'Air')
NUMBER: 27  CARD: (27, "Farfetcch'd", 'Air')
NUMBER: 28  CARD: (28, 'Growlithe', 'Fire')
NUMBER: 29  CARD: (29, 'Haunter', 'Psychic')
NUMBER: 30  CARD: (30, 'IvySaur', 'Grass')
NUMBER: 31  CARD: (31, 'Jynx', 'Psychic')
NUMBER: 32  CARD: (32, 'Kadabra', 'Psychic')
NUMBER: 33  CARD: (33, 'Kakuna', 'Grass')
NUMBER: 34  CARD: (34, 'Machoke', 'Rock')
NUMBER: 35  CARD: (35, 'Magikarp', 'Water')
NUMBER: 36  CARD: (36, 'Magmar', 'Fire')
NUMBER: 37  CARD: (37, 'Nidorino', 'Grass')
NUMBER: 38  CARD: (38, 'Poliwhirl', 'Water')
NUMBER: 39  CARD: (39, 'Porygon', 'Air')
NUMBER: 40  CARD: (40, 'Raticate', 'Air')
NUMBER: 41  CARD: (41, 'Seel', 'Water')
NUMBER: 42  CARD: (42, 'Wartortle', 'Water')
NUMBER: 43  CARD: (43, 'Abra', 'Psychic')
NUMBER: 44  CARD: (44, 'Bulbasaur', 'Grass')
NUMBER: 45  CARD: (45, 'Caterpie', 'Grass')
NUMBER: 46  CARD: (46, 'Charmander', 'Fire')
NUMBER: 47  CARD: (47, 'Diglett', 'Rock')
NUMBER: 48  CARD: (48, 'Doduo', 'Air')
NUMBER: 49  CARD: (49, 'Drowzee', 'Psychic')
NUMBER: 50  CARD: (50, 'Gastly', 'Psychic')
NUMBER: 51  CARD: (51, 'Koffing', 'Grass')
NUMBER: 52  CARD: (52, 'Machop', 'Rock')
NUMBER: 53  CARD: (53, 'Magnemite', 'Electric')
NUMBER: 54  CARD: (54, 'Metapod', 'Grass')
NUMBER: 55  CARD: (55, 'Nidoran', 'Grass')
NUMBER: 56  CARD: (56, 'Onix', 'Rock')
NUMBER: 57  CARD: (57, 'Pidgey', 'Air')
NUMBER: 58  CARD: (58, 'Pikachu', 'Electric')
NUMBER: 59  CARD: (59, 'Poliwag', 'Water')
NUMBER: 60  CARD: (60, 'Ponyta', 'Fire')
NUMBER: 61  CARD: (61, 'Rattata', 'Air')
NUMBER: 62  CARD: (62, 'Sandshrew', 'Rock')
NUMBER: 63  CARD: (63, 'Squirtle', 'Water')
NUMBER: 64  CARD: (64, 'Starmie', 'Water')
NUMBER: 65  CARD: (65, 'Staryu', 'Water')
NUMBER: 66  CARD: (66, 'Tangela', 'Grass')
NUMBER: 67  CARD: (67, 'Voltorb', 'Electric')
NUMBER: 68  CARD: (68, 'Vulpix', 'Fire')
NUMBER: 69  CARD: (69, 'Weedle', 'Grass')
NUMBER: 70  CARD: (70, 'Clefairy Doll', 'Trainer')
NUMBER: 71  CARD: (71, 'Computer Search', 'Trainer')
NUMBER: 72  CARD: (72, 'Devolution Spray', 'Trainer')
NUMBER: 73  CARD: (73, 'Imposter Professor Oak', 'Trainer')
NUMBER: 74  CARD: (74, 'Item Finder', 'Trainer')
NUMBER: 75  CARD: (75, 'Lass', 'Trainer')
NUMBER: 76  CARD: (76, 'Pokemon Breeder', 'Trainer')
NUMBER: 77  CARD: (77, 'Pokemon Trader', 'Trainer')
NUMBER: 78  CARD: (78, 'Scoop Up', 'Trainer')
NUMBER: 79  CARD: (79, 'Super Energy Removal', 'Trainer')
NUMBER: 80  CARD: (80, 'Defender', 'Trainer')
NUMBER: 81  CARD: (81, 'Energy Retrieval', 'Trainer')
NUMBER: 82  CARD: (82, 'Full Heal', 'Trainer')
NUMBER: 83  CARD: (83, 'Maintenance', 'Trainer')
NUMBER: 84  CARD: (84, 'PlusPower', 'Trainer')
NUMBER: 85  CARD: (85, 'Pokemon Center', 'Trainer')
NUMBER: 86  CARD: (86, 'Pokemon Flute', 'Trainer')
NUMBER: 87  CARD: (87, 'Pokedex', 'Trainer')
NUMBER: 88  CARD: (88, 'Professor Oak', 'Trainer')
NUMBER: 89  CARD: (89, 'Revive', 'Trainer')
NUMBER: 90  CARD: (90, 'Super Potion', 'Trainer')
NUMBER: 91  CARD: (91, 'Bill', 'Trainer')
NUMBER: 92  CARD: (92, 'Energy Removal', 'Trainer')
NUMBER: 93  CARD: (93, 'Gust of Wind', 'Trainer')
NUMBER: 94  CARD: (94, 'Potion', 'Trainer')
NUMBER: 95  CARD: (95, 'Switch', 'Trainer')
NUMBER: 96  CARD: (96, 'Energy - Colorless', 'Energy')
NUMBER: 97  CARD: (97, 'Energy - Fight', 'Energy')
NUMBER: 98  CARD: (98, 'Energy - Fire', 'Energy')
NUMBER: 99  CARD: (99, 'Energy - Grass', 'Energy')
NUMBER: 100  CARD: (100, 'Energy - Elec', 'Energy')
NUMBER: 101  CARD: (101, 'Energy - Psychic', 'Energy')
NUMBER: 102  CARD: (102, 'Energy - Water', 'Energy')"""

    
    # Execute the function
      # Run the main function
    pokemon.print_database(inputs)
    #Get the feedback
    captured = capsys.readouterr()

    similarity_threshold = 0.99  # Set your desired threshold here

    similarity_score = assessMeTester_StringSimilarity.string_similarity(expected_output, captured.out)

   
    if similarity_score >= similarity_threshold:
        feedback = "Strings are similar enough (score: {0:.2f}%). Test passed!".format(similarity_score * 100)
    else:
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "***************test_print_database tester failed!***************"
        feedback = feedback+ "\nExpected:\n" +"\033[93m"+ expected_output+"\033[0m"+"\n\n"
        feedback = feedback + "\nCaptured:\n" +"\033[93m"+  captured.out +"\033[0m"
        feedback = feedback+ "\n\033[91m" ## RED START
        feedback = feedback + f"Strings are not similar enough (score: {similarity_score})"
        feedback = feedback + "\n***********************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
    # Use sys.stdout to write out the feedback message
    if(printFeedback):
        print(feedback + "\n")
  

    assert similarity_score >= similarity_threshold, f"Strings are not similar enough (score: {similarity_score})"


def test_make_pack(capsys, monkeypatch,printFeedback=True):
        success = True
        assertMessage = "" ##Assert message

        ##MODIFY
        testerName = "test_make_pack"
        functionName = "make_pack"

        input = {43: (43, 'Abra', 'Psychic'), 1: (1, 'Alakazam', 'Psychic'), 23: (23, 'Arcanine', 'Fire'), 17: (17, 'Beedrill', 'Grass'), 91: (91, 'Bill', 'Trainer'), 2: (2, 'Blastoise', 'Water'), 44: (44, 'Bulbasaur', 'Grass'), 45: (45, 'Caterpie', 'Grass'), 3: (3, 'Chansey', 'Air'), 4: (4, 'Charizard', 'Fire'), 46: (46, 'Charmander', 'Fire'), 24: (24, 'Charmeleon', 'Fire'), 5: (5, 'Clefairy', 'Air'), 70: (70, 'Clefairy Doll', 'Trainer'), 71: (71, 'Computer Search', 'Trainer'), 80: (80, 'Defender', 'Trainer'), 72: (72, 'Devolution Spray', 'Trainer'), 25: (25, 'Dewgong', 'Water'), 47: (47, 'Diglett', 'Rock'), 48: (48, 'Doduo', 'Air'), 18: (18, 'Dragonair', 'Air'), 26: (26, 'Dratini', 'Air'), 49: (49, 'Drowzee', 'Psychic'), 19: (19, 'Dugtrio', 'Rock'), 20: (20, 'Electabuzz', 'Electric'), 21: (21, 'Electrode', 'Electric'), 96: (96, 'Energy - Colorless', 'Energy'), 100: (100, 'Energy - Elec', 'Energy'), 98: (98, 'Energy - Fire', 'Energy'), 99: (99, 'Energy - Grass', 'Energy'), 101: (101, 'Energy - Psychic', 'Energy'), 97: (97, 'Energy - Fight', 'Energy'), 102: (102, 'Energy - Water', 'Energy'), 92: (92, 'Energy Removal', 'Trainer'), 81: (81, 'Energy Retrieval', 'Trainer'), 27: (27, "Farfetcch'd", 'Air'), 82: (82, 'Full Heal', 'Trainer'), 50: (50, 'Gastly', 'Psychic'), 28: (28, 'Growlithe', 'Fire'), 93: (93, 'Gust of Wind', 'Trainer'), 6: (6, 'Gyarados', 'Water'), 29: (29, 'Haunter', 'Psychic'), 7: (7, 'Hitmonchan', 'Rock'), 73: (73, 'Imposter Professor Oak', 'Trainer'), 74: (74, 'Item Finder', 'Trainer'), 30: (30, 'IvySaur', 'Grass'), 31: (31, 'Jynx', 'Psychic'), 32: (32, 'Kadabra', 'Psychic'), 33: (33, 'Kakuna', 'Grass'), 51: (51, 'Koffing', 'Grass'), 75: (75, 'Lass', 'Trainer'), 8: (8, 'Machamp', 'Rock'), 34: (34, 'Machoke', 'Rock'), 52: (52, 'Machop', 'Rock'), 35: (35, 'Magikarp', 'Water'), 36: (36, 'Magmar', 'Fire'), 53: (53, 'Magnemite', 'Electric'), 9: (9, 'Magneton', 'Electric'), 83: (83, 'Maintenance', 'Trainer'), 54: (54, 'Metapod', 'Grass'), 10: (10, 'MewTwo', 'Psychic'), 11: (11, 'NidoKing', 'Grass'), 55: (55, 'Nidoran', 'Grass'), 37: (37, 'Nidorino', 'Grass'), 12: (12, 'Ninetales', 'Fire'), 56: (56, 'Onix', 'Rock'), 22: (22, 'Pidgeotto', 'Air'), 57: (57, 'Pidgey', 'Air'), 58: (58, 'Pikachu', 'Electric'), 84: (84, 'PlusPower', 'Trainer'), 87: (87, 'Pokedex', 'Trainer'), 76: (76, 'Pokemon Breeder', 'Trainer'), 85: (85, 'Pokemon Center', 'Trainer'), 86: (86, 'Pokemon Flute', 'Trainer'), 77: (77, 'Pokemon Trader', 'Trainer'), 59: (59, 'Poliwag', 'Water'), 38: (38, 'Poliwhirl', 'Water'), 13: (13, 'Poliwrath', 'Water'), 60: (60, 'Ponyta', 'Fire'), 39: (39, 'Porygon', 'Air'), 94: (94, 'Potion', 'Trainer'), 88: (88, 'Professor Oak', 'Trainer'), 14: (14, 'Raichu', 'Electric'), 40: (40, 'Raticate', 'Air'), 61: (61, 'Rattata', 'Air'), 89: (89, 'Revive', 'Trainer'), 62: (62, 'Sandshrew', 'Rock'), 78: (78, 'Scoop Up', 'Trainer'), 41: (41, 'Seel', 'Water'), 63: (63, 'Squirtle', 'Water'), 64: (64, 'Starmie', 'Water'), 65: (65, 'Staryu', 'Water'), 90: (90, 'Super Potion', 'Trainer'), 79: (79, 'Super Energy Removal', 'Trainer'), 95: (95, 'Switch', 'Trainer'), 66: (66, 'Tangela', 'Grass'), 15: (15, 'Venusaur', 'Grass'), 67: (67, 'Voltorb', 'Electric'), 68: (68, 'Vulpix', 'Fire'), 42: (42, 'Wartortle', 'Water'), 69: (69, 'Weedle', 'Grass'), 16: (16, 'Zapdos', 'Electric')}
       

        expected = {(49, 'Drowzee', 'Psychic'), (61, 'Rattata', 'Air'), (99, 'Energy - Grass', 'Energy'), (97, 'Energy - Fight', 'Energy'), (33, 'Kakuna', 'Grass'), (82, 'Full Heal', 'Trainer'), (28, 'Growlithe', 'Fire'), (6, 'Gyarados', 'Water'), (2, 'Blastoise', 'Water'), (40, 'Raticate', 'Air')}
          
        try:

            # invoke
            random.seed(25)
            result = pokemon.make_pack(input)
                   
            if result==None:
                 success=False
                 assertMessage="The function must return a value!"
                 raise
             
            # Part for string comparison!
            if result==expected:
                assert True
            else:
                success = False
                assertMessage=f"The {functionName} is not correct!\nExpected:{expected}"
                assertMessage+=f"\nReturned:{result}"
        except AttributeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except TypeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except AssertionError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except:
            pass
        
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "\n******************************************* "+testerName+ " *****************\n"
        feedback = feedback + "\033[93m"+ assertMessage+"\033[0m"+"\n\n"
        feedback = feedback + "\n\033[91m*******************************************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
        feedback = feedback + "\n\n\n"

        if printFeedback and len(assertMessage)>0:
            print(feedback)
        assert success,assertMessage

def test_print_pack(capsys, monkeypatch, printFeedback=True):

    inputs = {(68, 'Vulpix', 'Fire'), (6, 'Gyarados', 'Water'), (67, 'Voltorb', 'Electric'), (101, 'Energy - Psychic', 'Energy'), (87, 'Pokedex', 'Trainer'), (26, 'Dratini', 'Air'), (66, 'Tangela', 'Grass'), (51, 'Koffing', 'Grass'), (16, 'Zapdos', 'Electric'), (45, 'Caterpie', 'Grass')}
            
    expected_output = """CARD1: 6 Gyarados Water
CARD2: 16 Zapdos Electric
CARD3: 26 Dratini Air
CARD4: 45 Caterpie Grass
CARD5: 51 Koffing Grass
CARD6: 66 Tangela Grass
CARD7: 67 Voltorb Electric
CARD8: 68 Vulpix Fire
CARD9: 87 Pokedex Trainer
CARD10: 101 Energy - Psychic Energy"""

    
    # Execute the function
      # Run the main function
    pokemon.print_pack(inputs)
    #Get the feedback
    captured = capsys.readouterr()

    similarity_threshold = 0.99  # Set your desired threshold here

    similarity_score = assessMeTester_StringSimilarity.string_similarity(expected_output, captured.out)

   
    if similarity_score >= similarity_threshold:
        feedback = "Strings are similar enough (score: {0:.2f}%). Test passed!".format(similarity_score * 100)
    else:
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "***************test_print_pack failed!***************"
        feedback = feedback+ "\nExpected:\n" +"\033[93m"+ expected_output+"\033[0m"+"\n\n"
        feedback = feedback + "\nCaptured:\n" +"\033[93m"+  captured.out +"\033[0m"
        feedback = feedback+ "\n\033[91m" ## RED START
        feedback = feedback + f"Strings are not similar enough (score: {similarity_score})"
        feedback = feedback + "\n***********************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
    # Use sys.stdout to write out the feedback message
    if(printFeedback):
        print(feedback + "\n")




def build_basic_collection_testing(capsys, monkeypatch, input, expected, printFeedback=True):
        success = True
        assertMessage = "" ##Assert message

        ##MODIFY
        testerName = "test_build_basic_collection"
        functionName = "build_basic_collection"
      
        try:

            # invoke
            result = pokemon.build_basic_collection(input)
                   
            if result==None:
                 success=False
                 assertMessage="The function must return a value!"
                 raise
             
            # Part for string comparison!
            if result==expected:
                assert True
            else:
                success = False
                assertMessage=f"The {functionName} is not correct!\nExpected:{expected}"
                assertMessage+=f"\nReturned:{result}"
        except AttributeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except TypeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except AssertionError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except:
            pass
        
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "\n******************************************* "+testerName+ " *****************\n"
        feedback = feedback + "\033[93m"+ assertMessage+"\033[0m"+"\n\n"
        feedback = feedback + "\n\033[91m*******************************************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
        feedback = feedback + "\n\n\n"

        if printFeedback and len(assertMessage)>0:
            print(feedback)
        assert success,assertMessage

def test_build_basic_collection(capsys, monkeypatch,printFeedback=True):
    #TEST1
    input = {43: (43, 'Abra', 'Psychic'), 1: (1, 'Alakazam', 'Psychic'), 23: (23, 'Arcanine', 'Fire'), 17: (17, 'Beedrill', 'Grass'), 91: (91, 'Bill', 'Trainer'), 2: (2, 'Blastoise', 'Water'), 44: (44, 'Bulbasaur', 'Grass'), 45: (45, 'Caterpie', 'Grass'), 3: (3, 'Chansey', 'Air'), 4: (4, 'Charizard', 'Fire'), 46: (46, 'Charmander', 'Fire'), 24: (24, 'Charmeleon', 'Fire'), 5: (5, 'Clefairy', 'Air'), 70: (70, 'Clefairy Doll', 'Trainer'), 71: (71, 'Computer Search', 'Trainer'), 80: (80, 'Defender', 'Trainer'), 72: (72, 'Devolution Spray', 'Trainer'), 25: (25, 'Dewgong', 'Water'), 47: (47, 'Diglett', 'Rock'), 48: (48, 'Doduo', 'Air'), 18: (18, 'Dragonair', 'Air'), 26: (26, 'Dratini', 'Air'), 49: (49, 'Drowzee', 'Psychic'), 19: (19, 'Dugtrio', 'Rock'), 20: (20, 'Electabuzz', 'Electric'), 21: (21, 'Electrode', 'Electric'), 96: (96, 'Energy - Colorless', 'Energy'), 100: (100, 'Energy - Elec', 'Energy'), 98: (98, 'Energy - Fire', 'Energy'), 99: (99, 'Energy - Grass', 'Energy'), 101: (101, 'Energy - Psychic', 'Energy'), 97: (97, 'Energy - Fight', 'Energy'), 102: (102, 'Energy - Water', 'Energy'), 92: (92, 'Energy Removal', 'Trainer'), 81: (81, 'Energy Retrieval', 'Trainer'), 27: (27, "Farfetcch'd", 'Air'), 82: (82, 'Full Heal', 'Trainer'), 50: (50, 'Gastly', 'Psychic'), 28: (28, 'Growlithe', 'Fire'), 93: (93, 'Gust of Wind', 'Trainer'), 6: (6, 'Gyarados', 'Water'), 29: (29, 'Haunter', 'Psychic'), 7: (7, 'Hitmonchan', 'Rock'), 73: (73, 'Imposter Professor Oak', 'Trainer'), 74: (74, 'Item Finder', 'Trainer'), 30: (30, 'IvySaur', 'Grass'), 31: (31, 'Jynx', 'Psychic'), 32: (32, 'Kadabra', 'Psychic'), 33: (33, 'Kakuna', 'Grass'), 51: (51, 'Koffing', 'Grass'), 75: (75, 'Lass', 'Trainer'), 8: (8, 'Machamp', 'Rock'), 34: (34, 'Machoke', 'Rock'), 52: (52, 'Machop', 'Rock'), 35: (35, 'Magikarp', 'Water'), 36: (36, 'Magmar', 'Fire'), 53: (53, 'Magnemite', 'Electric'), 9: (9, 'Magneton', 'Electric'), 83: (83, 'Maintenance', 'Trainer'), 54: (54, 'Metapod', 'Grass'), 10: (10, 'MewTwo', 'Psychic'), 11: (11, 'NidoKing', 'Grass'), 55: (55, 'Nidoran', 'Grass'), 37: (37, 'Nidorino', 'Grass'), 12: (12, 'Ninetales', 'Fire'), 56: (56, 'Onix', 'Rock'), 22: (22, 'Pidgeotto', 'Air'), 57: (57, 'Pidgey', 'Air'), 58: (58, 'Pikachu', 'Electric'), 84: (84, 'PlusPower', 'Trainer'), 87: (87, 'Pokedex', 'Trainer'), 76: (76, 'Pokemon Breeder', 'Trainer'), 85: (85, 'Pokemon Center', 'Trainer'), 86: (86, 'Pokemon Flute', 'Trainer'), 77: (77, 'Pokemon Trader', 'Trainer'), 59: (59, 'Poliwag', 'Water'), 38: (38, 'Poliwhirl', 'Water'), 13: (13, 'Poliwrath', 'Water'), 60: (60, 'Ponyta', 'Fire'), 39: (39, 'Porygon', 'Air'), 94: (94, 'Potion', 'Trainer'), 88: (88, 'Professor Oak', 'Trainer'), 14: (14, 'Raichu', 'Electric'), 40: (40, 'Raticate', 'Air'), 61: (61, 'Rattata', 'Air'), 89: (89, 'Revive', 'Trainer'), 62: (62, 'Sandshrew', 'Rock'), 78: (78, 'Scoop Up', 'Trainer'), 41: (41, 'Seel', 'Water'), 63: (63, 'Squirtle', 'Water'), 64: (64, 'Starmie', 'Water'), 65: (65, 'Staryu', 'Water'), 90: (90, 'Super Potion', 'Trainer'), 79: (79, 'Super Energy Removal', 'Trainer'), 95: (95, 'Switch', 'Trainer'), 66: (66, 'Tangela', 'Grass'), 15: (15, 'Venusaur', 'Grass'), 67: (67, 'Voltorb', 'Electric'), 68: (68, 'Vulpix', 'Fire'), 42: (42, 'Wartortle', 'Water'), 69: (69, 'Weedle', 'Grass'), 16: (16, 'Zapdos', 'Electric')}
    random.seed(25)
    expected = 46  
    build_basic_collection_testing(capsys, monkeypatch, input, expected, printFeedback=True)

    #TEST1
    input = {43: (43, 'Abra', 'Psychic'), 1: (1, 'Alakazam', 'Psychic'), 23: (23, 'Arcanine', 'Fire'), 17: (17, 'Beedrill', 'Grass'), 91: (91, 'Bill', 'Trainer'), 2: (2, 'Blastoise', 'Water'), 44: (44, 'Bulbasaur', 'Grass'), 45: (45, 'Caterpie', 'Grass'), 3: (3, 'Chansey', 'Air'), 4: (4, 'Charizard', 'Fire'), 46: (46, 'Charmander', 'Fire'), 24: (24, 'Charmeleon', 'Fire'), 5: (5, 'Clefairy', 'Air'), 70: (70, 'Clefairy Doll', 'Trainer'), 71: (71, 'Computer Search', 'Trainer'), 80: (80, 'Defender', 'Trainer'), 72: (72, 'Devolution Spray', 'Trainer'), 25: (25, 'Dewgong', 'Water'), 47: (47, 'Diglett', 'Rock'), 48: (48, 'Doduo', 'Air'), 18: (18, 'Dragonair', 'Air'), 26: (26, 'Dratini', 'Air'), 49: (49, 'Drowzee', 'Psychic'), 19: (19, 'Dugtrio', 'Rock'), 20: (20, 'Electabuzz', 'Electric'), 21: (21, 'Electrode', 'Electric'), 96: (96, 'Energy - Colorless', 'Energy'), 100: (100, 'Energy - Elec', 'Energy'), 98: (98, 'Energy - Fire', 'Energy'), 99: (99, 'Energy - Grass', 'Energy'), 101: (101, 'Energy - Psychic', 'Energy'), 97: (97, 'Energy - Fight', 'Energy'), 102: (102, 'Energy - Water', 'Energy'), 92: (92, 'Energy Removal', 'Trainer'), 81: (81, 'Energy Retrieval', 'Trainer'), 27: (27, "Farfetcch'd", 'Air'), 82: (82, 'Full Heal', 'Trainer'), 50: (50, 'Gastly', 'Psychic'), 28: (28, 'Growlithe', 'Fire'), 93: (93, 'Gust of Wind', 'Trainer'), 6: (6, 'Gyarados', 'Water'), 29: (29, 'Haunter', 'Psychic'), 7: (7, 'Hitmonchan', 'Rock'), 73: (73, 'Imposter Professor Oak', 'Trainer'), 74: (74, 'Item Finder', 'Trainer'), 30: (30, 'IvySaur', 'Grass'), 31: (31, 'Jynx', 'Psychic'), 32: (32, 'Kadabra', 'Psychic'), 33: (33, 'Kakuna', 'Grass'), 51: (51, 'Koffing', 'Grass'), 75: (75, 'Lass', 'Trainer'), 8: (8, 'Machamp', 'Rock'), 34: (34, 'Machoke', 'Rock'), 52: (52, 'Machop', 'Rock'), 35: (35, 'Magikarp', 'Water'), 36: (36, 'Magmar', 'Fire'), 53: (53, 'Magnemite', 'Electric'), 9: (9, 'Magneton', 'Electric'), 83: (83, 'Maintenance', 'Trainer'), 54: (54, 'Metapod', 'Grass'), 10: (10, 'MewTwo', 'Psychic'), 11: (11, 'NidoKing', 'Grass'), 55: (55, 'Nidoran', 'Grass'), 37: (37, 'Nidorino', 'Grass'), 12: (12, 'Ninetales', 'Fire'), 56: (56, 'Onix', 'Rock'), 22: (22, 'Pidgeotto', 'Air'), 57: (57, 'Pidgey', 'Air'), 58: (58, 'Pikachu', 'Electric'), 84: (84, 'PlusPower', 'Trainer'), 87: (87, 'Pokedex', 'Trainer'), 76: (76, 'Pokemon Breeder', 'Trainer'), 85: (85, 'Pokemon Center', 'Trainer'), 86: (86, 'Pokemon Flute', 'Trainer'), 77: (77, 'Pokemon Trader', 'Trainer'), 59: (59, 'Poliwag', 'Water'), 38: (38, 'Poliwhirl', 'Water'), 13: (13, 'Poliwrath', 'Water'), 60: (60, 'Ponyta', 'Fire'), 39: (39, 'Porygon', 'Air'), 94: (94, 'Potion', 'Trainer'), 88: (88, 'Professor Oak', 'Trainer'), 14: (14, 'Raichu', 'Electric'), 40: (40, 'Raticate', 'Air'), 61: (61, 'Rattata', 'Air'), 89: (89, 'Revive', 'Trainer'), 62: (62, 'Sandshrew', 'Rock'), 78: (78, 'Scoop Up', 'Trainer'), 41: (41, 'Seel', 'Water'), 63: (63, 'Squirtle', 'Water'), 64: (64, 'Starmie', 'Water'), 65: (65, 'Staryu', 'Water'), 90: (90, 'Super Potion', 'Trainer'), 79: (79, 'Super Energy Removal', 'Trainer'), 95: (95, 'Switch', 'Trainer'), 66: (66, 'Tangela', 'Grass'), 15: (15, 'Venusaur', 'Grass'), 67: (67, 'Voltorb', 'Electric'), 68: (68, 'Vulpix', 'Fire'), 42: (42, 'Wartortle', 'Water'), 69: (69, 'Weedle', 'Grass'), 16: (16, 'Zapdos', 'Electric')}
    random.seed(19)
    expected = 51
    build_basic_collection_testing(capsys, monkeypatch, input, expected, printFeedback=True)

     #TEST1
    input = {43: (43, 'Abra', 'Psychic'), 1: (1, 'Alakazam', 'Psychic'), 23: (23, 'Arcanine', 'Fire'), 17: (17, 'Beedrill', 'Grass'), 91: (91, 'Bill', 'Trainer'), 2: (2, 'Blastoise', 'Water'), 44: (44, 'Bulbasaur', 'Grass'), 45: (45, 'Caterpie', 'Grass'), 3: (3, 'Chansey', 'Air'), 4: (4, 'Charizard', 'Fire'), 46: (46, 'Charmander', 'Fire'), 24: (24, 'Charmeleon', 'Fire'), 5: (5, 'Clefairy', 'Air'), 70: (70, 'Clefairy Doll', 'Trainer'), 71: (71, 'Computer Search', 'Trainer'), 80: (80, 'Defender', 'Trainer'), 72: (72, 'Devolution Spray', 'Trainer'), 25: (25, 'Dewgong', 'Water'), 47: (47, 'Diglett', 'Rock'), 48: (48, 'Doduo', 'Air'), 18: (18, 'Dragonair', 'Air'), 26: (26, 'Dratini', 'Air'), 49: (49, 'Drowzee', 'Psychic'), 19: (19, 'Dugtrio', 'Rock'), 20: (20, 'Electabuzz', 'Electric'), 21: (21, 'Electrode', 'Electric'), 96: (96, 'Energy - Colorless', 'Energy'), 100: (100, 'Energy - Elec', 'Energy'), 98: (98, 'Energy - Fire', 'Energy'), 99: (99, 'Energy - Grass', 'Energy'), 101: (101, 'Energy - Psychic', 'Energy'), 97: (97, 'Energy - Fight', 'Energy'), 102: (102, 'Energy - Water', 'Energy'), 92: (92, 'Energy Removal', 'Trainer'), 81: (81, 'Energy Retrieval', 'Trainer'), 27: (27, "Farfetcch'd", 'Air'), 82: (82, 'Full Heal', 'Trainer'), 50: (50, 'Gastly', 'Psychic'), 28: (28, 'Growlithe', 'Fire'), 93: (93, 'Gust of Wind', 'Trainer'), 6: (6, 'Gyarados', 'Water'), 29: (29, 'Haunter', 'Psychic'), 7: (7, 'Hitmonchan', 'Rock'), 73: (73, 'Imposter Professor Oak', 'Trainer'), 74: (74, 'Item Finder', 'Trainer'), 30: (30, 'IvySaur', 'Grass'), 31: (31, 'Jynx', 'Psychic'), 32: (32, 'Kadabra', 'Psychic'), 33: (33, 'Kakuna', 'Grass'), 51: (51, 'Koffing', 'Grass'), 75: (75, 'Lass', 'Trainer'), 8: (8, 'Machamp', 'Rock'), 34: (34, 'Machoke', 'Rock'), 52: (52, 'Machop', 'Rock'), 35: (35, 'Magikarp', 'Water'), 36: (36, 'Magmar', 'Fire'), 53: (53, 'Magnemite', 'Electric'), 9: (9, 'Magneton', 'Electric'), 83: (83, 'Maintenance', 'Trainer'), 54: (54, 'Metapod', 'Grass'), 10: (10, 'MewTwo', 'Psychic'), 11: (11, 'NidoKing', 'Grass'), 55: (55, 'Nidoran', 'Grass'), 37: (37, 'Nidorino', 'Grass'), 12: (12, 'Ninetales', 'Fire'), 56: (56, 'Onix', 'Rock'), 22: (22, 'Pidgeotto', 'Air'), 57: (57, 'Pidgey', 'Air'), 58: (58, 'Pikachu', 'Electric'), 84: (84, 'PlusPower', 'Trainer'), 87: (87, 'Pokedex', 'Trainer'), 76: (76, 'Pokemon Breeder', 'Trainer'), 85: (85, 'Pokemon Center', 'Trainer'), 86: (86, 'Pokemon Flute', 'Trainer'), 77: (77, 'Pokemon Trader', 'Trainer'), 59: (59, 'Poliwag', 'Water'), 38: (38, 'Poliwhirl', 'Water'), 13: (13, 'Poliwrath', 'Water'), 60: (60, 'Ponyta', 'Fire'), 39: (39, 'Porygon', 'Air'), 94: (94, 'Potion', 'Trainer'), 88: (88, 'Professor Oak', 'Trainer'), 14: (14, 'Raichu', 'Electric'), 40: (40, 'Raticate', 'Air'), 61: (61, 'Rattata', 'Air'), 89: (89, 'Revive', 'Trainer'), 62: (62, 'Sandshrew', 'Rock'), 78: (78, 'Scoop Up', 'Trainer'), 41: (41, 'Seel', 'Water'), 63: (63, 'Squirtle', 'Water'), 64: (64, 'Starmie', 'Water'), 65: (65, 'Staryu', 'Water'), 90: (90, 'Super Potion', 'Trainer'), 79: (79, 'Super Energy Removal', 'Trainer'), 95: (95, 'Switch', 'Trainer'), 66: (66, 'Tangela', 'Grass'), 15: (15, 'Venusaur', 'Grass'), 67: (67, 'Voltorb', 'Electric'), 68: (68, 'Vulpix', 'Fire'), 42: (42, 'Wartortle', 'Water'), 69: (69, 'Weedle', 'Grass'), 16: (16, 'Zapdos', 'Electric')}
    random.seed(1)
    expected = 62  
    build_basic_collection_testing(capsys, monkeypatch, input, expected, printFeedback=True)


def average_number_of_packs_to_buy_testing(capsys, monkeypatch, input, expected, printFeedback=True):
        success = True
        assertMessage = "" ##Assert message

        ##MODIFY
        testerName = "test_average_number_of_packs_to_buy"
        functionName = "average_number_of_packs_to_buy"
      
        try:

            # invoke
            result = pokemon.average_number_of_packs_to_buy(input)
                   
            if result==None:
                 success=False
                 assertMessage="The function must return a value!"
                 raise
             
            # Part for string comparison!
            if abs(result-expected)<0.1:
                assert True
            else:
                success = False
                assertMessage=f"The {functionName} is not correct!\nExpected:{expected}"
                assertMessage+=f"\nReturned:{result}"
        except AttributeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except TypeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except AssertionError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except:
            pass
        
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "\n******************************************* "+testerName+ " *****************\n"
        feedback = feedback + "\033[93m"+ assertMessage+"\033[0m"+"\n\n"
        feedback = feedback + "\n\033[91m*******************************************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
        feedback = feedback + "\n\n\n"

        if printFeedback and len(assertMessage)>0:
            print(feedback)
        assert success,assertMessage



    

def test_average_number_of_packs_to_buy(capsys, monkeypatch,printFeedback=True):
    #TEST1
    input = {43: (43, 'Abra', 'Psychic'), 1: (1, 'Alakazam', 'Psychic'), 23: (23, 'Arcanine', 'Fire'), 17: (17, 'Beedrill', 'Grass'), 91: (91, 'Bill', 'Trainer'), 2: (2, 'Blastoise', 'Water'), 44: (44, 'Bulbasaur', 'Grass'), 45: (45, 'Caterpie', 'Grass'), 3: (3, 'Chansey', 'Air'), 4: (4, 'Charizard', 'Fire'), 46: (46, 'Charmander', 'Fire'), 24: (24, 'Charmeleon', 'Fire'), 5: (5, 'Clefairy', 'Air'), 70: (70, 'Clefairy Doll', 'Trainer'), 71: (71, 'Computer Search', 'Trainer'), 80: (80, 'Defender', 'Trainer'), 72: (72, 'Devolution Spray', 'Trainer'), 25: (25, 'Dewgong', 'Water'), 47: (47, 'Diglett', 'Rock'), 48: (48, 'Doduo', 'Air'), 18: (18, 'Dragonair', 'Air'), 26: (26, 'Dratini', 'Air'), 49: (49, 'Drowzee', 'Psychic'), 19: (19, 'Dugtrio', 'Rock'), 20: (20, 'Electabuzz', 'Electric'), 21: (21, 'Electrode', 'Electric'), 96: (96, 'Energy - Colorless', 'Energy'), 100: (100, 'Energy - Elec', 'Energy'), 98: (98, 'Energy - Fire', 'Energy'), 99: (99, 'Energy - Grass', 'Energy'), 101: (101, 'Energy - Psychic', 'Energy'), 97: (97, 'Energy - Fight', 'Energy'), 102: (102, 'Energy - Water', 'Energy'), 92: (92, 'Energy Removal', 'Trainer'), 81: (81, 'Energy Retrieval', 'Trainer'), 27: (27, "Farfetcch'd", 'Air'), 82: (82, 'Full Heal', 'Trainer'), 50: (50, 'Gastly', 'Psychic'), 28: (28, 'Growlithe', 'Fire'), 93: (93, 'Gust of Wind', 'Trainer'), 6: (6, 'Gyarados', 'Water'), 29: (29, 'Haunter', 'Psychic'), 7: (7, 'Hitmonchan', 'Rock'), 73: (73, 'Imposter Professor Oak', 'Trainer'), 74: (74, 'Item Finder', 'Trainer'), 30: (30, 'IvySaur', 'Grass'), 31: (31, 'Jynx', 'Psychic'), 32: (32, 'Kadabra', 'Psychic'), 33: (33, 'Kakuna', 'Grass'), 51: (51, 'Koffing', 'Grass'), 75: (75, 'Lass', 'Trainer'), 8: (8, 'Machamp', 'Rock'), 34: (34, 'Machoke', 'Rock'), 52: (52, 'Machop', 'Rock'), 35: (35, 'Magikarp', 'Water'), 36: (36, 'Magmar', 'Fire'), 53: (53, 'Magnemite', 'Electric'), 9: (9, 'Magneton', 'Electric'), 83: (83, 'Maintenance', 'Trainer'), 54: (54, 'Metapod', 'Grass'), 10: (10, 'MewTwo', 'Psychic'), 11: (11, 'NidoKing', 'Grass'), 55: (55, 'Nidoran', 'Grass'), 37: (37, 'Nidorino', 'Grass'), 12: (12, 'Ninetales', 'Fire'), 56: (56, 'Onix', 'Rock'), 22: (22, 'Pidgeotto', 'Air'), 57: (57, 'Pidgey', 'Air'), 58: (58, 'Pikachu', 'Electric'), 84: (84, 'PlusPower', 'Trainer'), 87: (87, 'Pokedex', 'Trainer'), 76: (76, 'Pokemon Breeder', 'Trainer'), 85: (85, 'Pokemon Center', 'Trainer'), 86: (86, 'Pokemon Flute', 'Trainer'), 77: (77, 'Pokemon Trader', 'Trainer'), 59: (59, 'Poliwag', 'Water'), 38: (38, 'Poliwhirl', 'Water'), 13: (13, 'Poliwrath', 'Water'), 60: (60, 'Ponyta', 'Fire'), 39: (39, 'Porygon', 'Air'), 94: (94, 'Potion', 'Trainer'), 88: (88, 'Professor Oak', 'Trainer'), 14: (14, 'Raichu', 'Electric'), 40: (40, 'Raticate', 'Air'), 61: (61, 'Rattata', 'Air'), 89: (89, 'Revive', 'Trainer'), 62: (62, 'Sandshrew', 'Rock'), 78: (78, 'Scoop Up', 'Trainer'), 41: (41, 'Seel', 'Water'), 63: (63, 'Squirtle', 'Water'), 64: (64, 'Starmie', 'Water'), 65: (65, 'Staryu', 'Water'), 90: (90, 'Super Potion', 'Trainer'), 79: (79, 'Super Energy Removal', 'Trainer'), 95: (95, 'Switch', 'Trainer'), 66: (66, 'Tangela', 'Grass'), 15: (15, 'Venusaur', 'Grass'), 67: (67, 'Voltorb', 'Electric'), 68: (68, 'Vulpix', 'Fire'), 42: (42, 'Wartortle', 'Water'), 69: (69, 'Weedle', 'Grass'), 16: (16, 'Zapdos', 'Electric')}
    random.seed(25)
    expected = 51.225  
    average_number_of_packs_to_buy_testing(capsys, monkeypatch, input, expected, printFeedback=True)

    #TEST1
    input = {43: (43, 'Abra', 'Psychic'), 1: (1, 'Alakazam', 'Psychic'), 23: (23, 'Arcanine', 'Fire'), 17: (17, 'Beedrill', 'Grass'), 91: (91, 'Bill', 'Trainer'), 2: (2, 'Blastoise', 'Water'), 44: (44, 'Bulbasaur', 'Grass'), 45: (45, 'Caterpie', 'Grass'), 3: (3, 'Chansey', 'Air'), 4: (4, 'Charizard', 'Fire'), 46: (46, 'Charmander', 'Fire'), 24: (24, 'Charmeleon', 'Fire'), 5: (5, 'Clefairy', 'Air'), 70: (70, 'Clefairy Doll', 'Trainer'), 71: (71, 'Computer Search', 'Trainer'), 80: (80, 'Defender', 'Trainer'), 72: (72, 'Devolution Spray', 'Trainer'), 25: (25, 'Dewgong', 'Water'), 47: (47, 'Diglett', 'Rock'), 48: (48, 'Doduo', 'Air'), 18: (18, 'Dragonair', 'Air'), 26: (26, 'Dratini', 'Air'), 49: (49, 'Drowzee', 'Psychic'), 19: (19, 'Dugtrio', 'Rock'), 20: (20, 'Electabuzz', 'Electric'), 21: (21, 'Electrode', 'Electric'), 96: (96, 'Energy - Colorless', 'Energy'), 100: (100, 'Energy - Elec', 'Energy'), 98: (98, 'Energy - Fire', 'Energy'), 99: (99, 'Energy - Grass', 'Energy'), 101: (101, 'Energy - Psychic', 'Energy'), 97: (97, 'Energy - Fight', 'Energy'), 102: (102, 'Energy - Water', 'Energy'), 92: (92, 'Energy Removal', 'Trainer'), 81: (81, 'Energy Retrieval', 'Trainer'), 27: (27, "Farfetcch'd", 'Air'), 82: (82, 'Full Heal', 'Trainer'), 50: (50, 'Gastly', 'Psychic'), 28: (28, 'Growlithe', 'Fire'), 93: (93, 'Gust of Wind', 'Trainer'), 6: (6, 'Gyarados', 'Water'), 29: (29, 'Haunter', 'Psychic'), 7: (7, 'Hitmonchan', 'Rock'), 73: (73, 'Imposter Professor Oak', 'Trainer'), 74: (74, 'Item Finder', 'Trainer'), 30: (30, 'IvySaur', 'Grass'), 31: (31, 'Jynx', 'Psychic'), 32: (32, 'Kadabra', 'Psychic'), 33: (33, 'Kakuna', 'Grass'), 51: (51, 'Koffing', 'Grass'), 75: (75, 'Lass', 'Trainer'), 8: (8, 'Machamp', 'Rock'), 34: (34, 'Machoke', 'Rock'), 52: (52, 'Machop', 'Rock'), 35: (35, 'Magikarp', 'Water'), 36: (36, 'Magmar', 'Fire'), 53: (53, 'Magnemite', 'Electric'), 9: (9, 'Magneton', 'Electric'), 83: (83, 'Maintenance', 'Trainer'), 54: (54, 'Metapod', 'Grass'), 10: (10, 'MewTwo', 'Psychic'), 11: (11, 'NidoKing', 'Grass'), 55: (55, 'Nidoran', 'Grass'), 37: (37, 'Nidorino', 'Grass'), 12: (12, 'Ninetales', 'Fire'), 56: (56, 'Onix', 'Rock'), 22: (22, 'Pidgeotto', 'Air'), 57: (57, 'Pidgey', 'Air'), 58: (58, 'Pikachu', 'Electric'), 84: (84, 'PlusPower', 'Trainer'), 87: (87, 'Pokedex', 'Trainer'), 76: (76, 'Pokemon Breeder', 'Trainer'), 85: (85, 'Pokemon Center', 'Trainer'), 86: (86, 'Pokemon Flute', 'Trainer'), 77: (77, 'Pokemon Trader', 'Trainer'), 59: (59, 'Poliwag', 'Water'), 38: (38, 'Poliwhirl', 'Water'), 13: (13, 'Poliwrath', 'Water'), 60: (60, 'Ponyta', 'Fire'), 39: (39, 'Porygon', 'Air'), 94: (94, 'Potion', 'Trainer'), 88: (88, 'Professor Oak', 'Trainer'), 14: (14, 'Raichu', 'Electric'), 40: (40, 'Raticate', 'Air'), 61: (61, 'Rattata', 'Air'), 89: (89, 'Revive', 'Trainer'), 62: (62, 'Sandshrew', 'Rock'), 78: (78, 'Scoop Up', 'Trainer'), 41: (41, 'Seel', 'Water'), 63: (63, 'Squirtle', 'Water'), 64: (64, 'Starmie', 'Water'), 65: (65, 'Staryu', 'Water'), 90: (90, 'Super Potion', 'Trainer'), 79: (79, 'Super Energy Removal', 'Trainer'), 95: (95, 'Switch', 'Trainer'), 66: (66, 'Tangela', 'Grass'), 15: (15, 'Venusaur', 'Grass'), 67: (67, 'Voltorb', 'Electric'), 68: (68, 'Vulpix', 'Fire'), 42: (42, 'Wartortle', 'Water'), 69: (69, 'Weedle', 'Grass'), 16: (16, 'Zapdos', 'Electric')}
    random.seed(19)
    expected = 50.259
    average_number_of_packs_to_buy_testing(capsys, monkeypatch, input, expected, printFeedback=True)

     #TEST1
    input = {43: (43, 'Abra', 'Psychic'), 1: (1, 'Alakazam', 'Psychic'), 23: (23, 'Arcanine', 'Fire'), 17: (17, 'Beedrill', 'Grass'), 91: (91, 'Bill', 'Trainer'), 2: (2, 'Blastoise', 'Water'), 44: (44, 'Bulbasaur', 'Grass'), 45: (45, 'Caterpie', 'Grass'), 3: (3, 'Chansey', 'Air'), 4: (4, 'Charizard', 'Fire'), 46: (46, 'Charmander', 'Fire'), 24: (24, 'Charmeleon', 'Fire'), 5: (5, 'Clefairy', 'Air'), 70: (70, 'Clefairy Doll', 'Trainer'), 71: (71, 'Computer Search', 'Trainer'), 80: (80, 'Defender', 'Trainer'), 72: (72, 'Devolution Spray', 'Trainer'), 25: (25, 'Dewgong', 'Water'), 47: (47, 'Diglett', 'Rock'), 48: (48, 'Doduo', 'Air'), 18: (18, 'Dragonair', 'Air'), 26: (26, 'Dratini', 'Air'), 49: (49, 'Drowzee', 'Psychic'), 19: (19, 'Dugtrio', 'Rock'), 20: (20, 'Electabuzz', 'Electric'), 21: (21, 'Electrode', 'Electric'), 96: (96, 'Energy - Colorless', 'Energy'), 100: (100, 'Energy - Elec', 'Energy'), 98: (98, 'Energy - Fire', 'Energy'), 99: (99, 'Energy - Grass', 'Energy'), 101: (101, 'Energy - Psychic', 'Energy'), 97: (97, 'Energy - Fight', 'Energy'), 102: (102, 'Energy - Water', 'Energy'), 92: (92, 'Energy Removal', 'Trainer'), 81: (81, 'Energy Retrieval', 'Trainer'), 27: (27, "Farfetcch'd", 'Air'), 82: (82, 'Full Heal', 'Trainer'), 50: (50, 'Gastly', 'Psychic'), 28: (28, 'Growlithe', 'Fire'), 93: (93, 'Gust of Wind', 'Trainer'), 6: (6, 'Gyarados', 'Water'), 29: (29, 'Haunter', 'Psychic'), 7: (7, 'Hitmonchan', 'Rock'), 73: (73, 'Imposter Professor Oak', 'Trainer'), 74: (74, 'Item Finder', 'Trainer'), 30: (30, 'IvySaur', 'Grass'), 31: (31, 'Jynx', 'Psychic'), 32: (32, 'Kadabra', 'Psychic'), 33: (33, 'Kakuna', 'Grass'), 51: (51, 'Koffing', 'Grass'), 75: (75, 'Lass', 'Trainer'), 8: (8, 'Machamp', 'Rock'), 34: (34, 'Machoke', 'Rock'), 52: (52, 'Machop', 'Rock'), 35: (35, 'Magikarp', 'Water'), 36: (36, 'Magmar', 'Fire'), 53: (53, 'Magnemite', 'Electric'), 9: (9, 'Magneton', 'Electric'), 83: (83, 'Maintenance', 'Trainer'), 54: (54, 'Metapod', 'Grass'), 10: (10, 'MewTwo', 'Psychic'), 11: (11, 'NidoKing', 'Grass'), 55: (55, 'Nidoran', 'Grass'), 37: (37, 'Nidorino', 'Grass'), 12: (12, 'Ninetales', 'Fire'), 56: (56, 'Onix', 'Rock'), 22: (22, 'Pidgeotto', 'Air'), 57: (57, 'Pidgey', 'Air'), 58: (58, 'Pikachu', 'Electric'), 84: (84, 'PlusPower', 'Trainer'), 87: (87, 'Pokedex', 'Trainer'), 76: (76, 'Pokemon Breeder', 'Trainer'), 85: (85, 'Pokemon Center', 'Trainer'), 86: (86, 'Pokemon Flute', 'Trainer'), 77: (77, 'Pokemon Trader', 'Trainer'), 59: (59, 'Poliwag', 'Water'), 38: (38, 'Poliwhirl', 'Water'), 13: (13, 'Poliwrath', 'Water'), 60: (60, 'Ponyta', 'Fire'), 39: (39, 'Porygon', 'Air'), 94: (94, 'Potion', 'Trainer'), 88: (88, 'Professor Oak', 'Trainer'), 14: (14, 'Raichu', 'Electric'), 40: (40, 'Raticate', 'Air'), 61: (61, 'Rattata', 'Air'), 89: (89, 'Revive', 'Trainer'), 62: (62, 'Sandshrew', 'Rock'), 78: (78, 'Scoop Up', 'Trainer'), 41: (41, 'Seel', 'Water'), 63: (63, 'Squirtle', 'Water'), 64: (64, 'Starmie', 'Water'), 65: (65, 'Staryu', 'Water'), 90: (90, 'Super Potion', 'Trainer'), 79: (79, 'Super Energy Removal', 'Trainer'), 95: (95, 'Switch', 'Trainer'), 66: (66, 'Tangela', 'Grass'), 15: (15, 'Venusaur', 'Grass'), 67: (67, 'Voltorb', 'Electric'), 68: (68, 'Vulpix', 'Fire'), 42: (42, 'Wartortle', 'Water'), 69: (69, 'Weedle', 'Grass'), 16: (16, 'Zapdos', 'Electric')}
    random.seed(1)
    expected = 51.936  
    average_number_of_packs_to_buy_testing(capsys, monkeypatch, input, expected, printFeedback=True)


def test_build_counting_collection(capsys, monkeypatch,printFeedback=True):
        success = True
        assertMessage = "" ##Assert message

        ##MODIFY
        testerName = "test_build_counting_collection"
        functionName = "build_counting_collection"

        input = {43: (43, 'Abra', 'Psychic'), 1: (1, 'Alakazam', 'Psychic'), 23: (23, 'Arcanine', 'Fire'), 17: (17, 'Beedrill', 'Grass'), 91: (91, 'Bill', 'Trainer'), 2: (2, 'Blastoise', 'Water'), 44: (44, 'Bulbasaur', 'Grass'), 45: (45, 'Caterpie', 'Grass'), 3: (3, 'Chansey', 'Air'), 4: (4, 'Charizard', 'Fire'), 46: (46, 'Charmander', 'Fire'), 24: (24, 'Charmeleon', 'Fire'), 5: (5, 'Clefairy', 'Air'), 70: (70, 'Clefairy Doll', 'Trainer'), 71: (71, 'Computer Search', 'Trainer'), 80: (80, 'Defender', 'Trainer'), 72: (72, 'Devolution Spray', 'Trainer'), 25: (25, 'Dewgong', 'Water'), 47: (47, 'Diglett', 'Rock'), 48: (48, 'Doduo', 'Air'), 18: (18, 'Dragonair', 'Air'), 26: (26, 'Dratini', 'Air'), 49: (49, 'Drowzee', 'Psychic'), 19: (19, 'Dugtrio', 'Rock'), 20: (20, 'Electabuzz', 'Electric'), 21: (21, 'Electrode', 'Electric'), 96: (96, 'Energy - Colorless', 'Energy'), 100: (100, 'Energy - Elec', 'Energy'), 98: (98, 'Energy - Fire', 'Energy'), 99: (99, 'Energy - Grass', 'Energy'), 101: (101, 'Energy - Psychic', 'Energy'), 97: (97, 'Energy - Fight', 'Energy'), 102: (102, 'Energy - Water', 'Energy'), 92: (92, 'Energy Removal', 'Trainer'), 81: (81, 'Energy Retrieval', 'Trainer'), 27: (27, "Farfetcch'd", 'Air'), 82: (82, 'Full Heal', 'Trainer'), 50: (50, 'Gastly', 'Psychic'), 28: (28, 'Growlithe', 'Fire'), 93: (93, 'Gust of Wind', 'Trainer'), 6: (6, 'Gyarados', 'Water'), 29: (29, 'Haunter', 'Psychic'), 7: (7, 'Hitmonchan', 'Rock'), 73: (73, 'Imposter Professor Oak', 'Trainer'), 74: (74, 'Item Finder', 'Trainer'), 30: (30, 'IvySaur', 'Grass'), 31: (31, 'Jynx', 'Psychic'), 32: (32, 'Kadabra', 'Psychic'), 33: (33, 'Kakuna', 'Grass'), 51: (51, 'Koffing', 'Grass'), 75: (75, 'Lass', 'Trainer'), 8: (8, 'Machamp', 'Rock'), 34: (34, 'Machoke', 'Rock'), 52: (52, 'Machop', 'Rock'), 35: (35, 'Magikarp', 'Water'), 36: (36, 'Magmar', 'Fire'), 53: (53, 'Magnemite', 'Electric'), 9: (9, 'Magneton', 'Electric'), 83: (83, 'Maintenance', 'Trainer'), 54: (54, 'Metapod', 'Grass'), 10: (10, 'MewTwo', 'Psychic'), 11: (11, 'NidoKing', 'Grass'), 55: (55, 'Nidoran', 'Grass'), 37: (37, 'Nidorino', 'Grass'), 12: (12, 'Ninetales', 'Fire'), 56: (56, 'Onix', 'Rock'), 22: (22, 'Pidgeotto', 'Air'), 57: (57, 'Pidgey', 'Air'), 58: (58, 'Pikachu', 'Electric'), 84: (84, 'PlusPower', 'Trainer'), 87: (87, 'Pokedex', 'Trainer'), 76: (76, 'Pokemon Breeder', 'Trainer'), 85: (85, 'Pokemon Center', 'Trainer'), 86: (86, 'Pokemon Flute', 'Trainer'), 77: (77, 'Pokemon Trader', 'Trainer'), 59: (59, 'Poliwag', 'Water'), 38: (38, 'Poliwhirl', 'Water'), 13: (13, 'Poliwrath', 'Water'), 60: (60, 'Ponyta', 'Fire'), 39: (39, 'Porygon', 'Air'), 94: (94, 'Potion', 'Trainer'), 88: (88, 'Professor Oak', 'Trainer'), 14: (14, 'Raichu', 'Electric'), 40: (40, 'Raticate', 'Air'), 61: (61, 'Rattata', 'Air'), 89: (89, 'Revive', 'Trainer'), 62: (62, 'Sandshrew', 'Rock'), 78: (78, 'Scoop Up', 'Trainer'), 41: (41, 'Seel', 'Water'), 63: (63, 'Squirtle', 'Water'), 64: (64, 'Starmie', 'Water'), 65: (65, 'Staryu', 'Water'), 90: (90, 'Super Potion', 'Trainer'), 79: (79, 'Super Energy Removal', 'Trainer'), 95: (95, 'Switch', 'Trainer'), 66: (66, 'Tangela', 'Grass'), 15: (15, 'Venusaur', 'Grass'), 67: (67, 'Voltorb', 'Electric'), 68: (68, 'Vulpix', 'Fire'), 42: (42, 'Wartortle', 'Water'), 69: (69, 'Weedle', 'Grass'), 16: (16, 'Zapdos', 'Electric')}
        expected= {(82, 'Full Heal', 'Trainer'): 6, (28, 'Growlithe', 'Fire'): 3, (61, 'Rattata', 'Air'): 4, (6, 'Gyarados', 'Water'): 5, (97, 'Energy - Fight', 'Energy'): 6, (99, 'Energy - Grass', 'Energy'): 3, (33, 'Kakuna', 'Grass'): 3, (2, 'Blastoise', 'Water'): 3, (40, 'Raticate', 'Air'): 6, (49, 'Drowzee', 'Psychic'): 6, (13, 'Poliwrath', 'Water'): 7, (94, 'Potion', 'Trainer'): 6, (88, 'Professor Oak', 'Trainer'): 4, (73, 'Imposter Professor Oak', 'Trainer'): 6, (16, 'Zapdos', 'Electric'): 5, (76, 'Pokemon Breeder', 'Trainer'): 5, (74, 'Item Finder', 'Trainer'): 6, (55, 'Nidoran', 'Grass'): 11, (5, 'Clefairy', 'Air'): 10, (71, 'Computer Search', 'Trainer'): 3, (66, 'Tangela', 'Grass'): 6, (80, 'Defender', 'Trainer'): 9, (68, 'Vulpix', 'Fire'): 3, (102, 'Energy - Water', 'Energy'): 7, (26, 'Dratini', 'Air'): 4, (41, 'Seel', 'Water'): 7, (46, 'Charmander', 'Fire'): 4, (24, 'Charmeleon', 'Fire'): 3, (14, 'Raichu', 'Electric'): 5, (21, 'Electrode', 'Electric'): 6, (54, 'Metapod', 'Grass'): 4, (75, 'Lass', 'Trainer'): 4, (87, 'Pokedex', 'Trainer'): 3, (77, 'Pokemon Trader', 'Trainer'): 6, (25, 'Dewgong', 'Water'): 2, (17, 'Beedrill', 'Grass'): 8, (59, 'Poliwag', 'Water'): 4, (52, 'Machop', 'Rock'): 2, (10, 'MewTwo', 'Psychic'): 8, (9, 'Magneton', 'Electric'): 9, (72, 'Devolution Spray', 'Trainer'): 4, (58, 'Pikachu', 'Electric'): 7, (29, 'Haunter', 'Psychic'): 5, (23, 'Arcanine', 'Fire'): 6, (70, 'Clefairy Doll', 'Trainer'): 8, (8, 'Machamp', 'Rock'): 8, (56, 'Onix', 'Rock'): 5, (64, 'Starmie', 'Water'): 5, (37, 'Nidorino', 'Grass'): 4, (79, 'Super Energy Removal', 'Trainer'): 5, (57, 'Pidgey', 'Air'): 2, (22, 'Pidgeotto', 'Air'): 5, (65, 'Staryu', 'Water'): 9, (84, 'PlusPower', 'Trainer'): 4, (62, 'Sandshrew', 'Rock'): 5, (7, 'Hitmonchan', 'Rock'): 6, (53, 'Magnemite', 'Electric'): 2, (3, 'Chansey', 'Air'): 7, (81, 'Energy Retrieval', 'Trainer'): 5, (45, 'Caterpie', 'Grass'): 4, (12, 'Ninetales', 'Fire'): 3, (30, 'IvySaur', 'Grass'): 4, (98, 'Energy - Fire', 'Energy'): 6, (27, "Farfetcch'd", 'Air'): 3, (19, 'Dugtrio', 'Rock'): 5, (48, 'Doduo', 'Air'): 5, (18, 'Dragonair', 'Air'): 3, (67, 'Voltorb', 'Electric'): 5, (39, 'Porygon', 'Air'): 2, (47, 'Diglett', 'Rock'): 6, (60, 'Ponyta', 'Fire'): 4, (34, 'Machoke', 'Rock'): 6, (15, 'Venusaur', 'Grass'): 6, (4, 'Charizard', 'Fire'): 2, (91, 'Bill', 'Trainer'): 6, (101, 'Energy - Psychic', 'Energy'): 3, (96, 'Energy - Colorless', 'Energy'): 4, (95, 'Switch', 'Trainer'): 2, (11, 'NidoKing', 'Grass'): 4, (92, 'Energy Removal', 'Trainer'): 3, (35, 'Magikarp', 'Water'): 5, (86, 'Pokemon Flute', 'Trainer'): 2, (90, 'Super Potion', 'Trainer'): 4, (36, 'Magmar', 'Fire'): 4, (20, 'Electabuzz', 'Electric'): 2, (89, 'Revive', 'Trainer'): 3, (42, 'Wartortle', 'Water'): 2, (38, 'Poliwhirl', 'Water'): 3, (1, 'Alakazam', 'Psychic'): 2, (63, 'Squirtle', 'Water'): 4, (78, 'Scoop Up', 'Trainer'): 2, (44, 'Bulbasaur', 'Grass'): 4, (31, 'Jynx', 'Psychic'): 3, (100, 'Energy - Elec', 'Energy'): 3, (51, 'Koffing', 'Grass'): 4, (50, 'Gastly', 'Psychic'): 2, (69, 'Weedle', 'Grass'): 4, (83, 'Maintenance', 'Trainer'): 2, (43, 'Abra', 'Psychic'): 1, (32, 'Kadabra', 'Psychic'): 1, (93, 'Gust of Wind', 'Trainer'): 2, (85, 'Pokemon Center', 'Trainer'): 1}
        try:

            # invoke
            random.seed(25)
            result = pokemon.build_counting_collection(input)
                   
            if result==None:
                 success=False
                 assertMessage="The function must return a value!"
                 raise
             
            # Part for string comparison!
            if result==expected:
                assert True
            else:
                success = False
                assertMessage=f"The {functionName} is not correct!\nExpected:{expected}"
                assertMessage+=f"\nReturned:{result}"
        except AttributeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except TypeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except AssertionError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except:
            pass
        
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "\n******************************************* "+testerName+ " *****************\n"
        feedback = feedback + "\033[93m"+ assertMessage+"\033[0m"+"\n\n"
        feedback = feedback + "\n\033[91m*******************************************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
        feedback = feedback + "\n\n\n"

        if printFeedback and len(assertMessage)>0:
            print(feedback)
        assert success,assertMessage



def test_print_counting_collection(capsys, monkeypatch, printFeedback=True):

    input = {(82, 'Full Heal', 'Trainer'): 6, (28, 'Growlithe', 'Fire'): 3, (61, 'Rattata', 'Air'): 4, (6, 'Gyarados', 'Water'): 5,(85, 'Pokemon Center', 'Trainer'): 1}
       
    expected_output = """CARD:(6, 'Gyarados', 'Water'), total number of card purchased:5
CARD:(28, 'Growlithe', 'Fire'), total number of card purchased:3
CARD:(61, 'Rattata', 'Air'), total number of card purchased:4
CARD:(82, 'Full Heal', 'Trainer'), total number of card purchased:6
CARD:(85, 'Pokemon Center', 'Trainer'), total number of card purchased:1"""

   
    # Execute the function
      # Run the main function
    pokemon.print_counting_collection(input)
    #Get the feedback
    captured = capsys.readouterr()

    similarity_threshold = 0.99  # Set your desired threshold here

    similarity_score = assessMeTester_StringSimilarity.string_similarity(expected_output, captured.out)

   
    if similarity_score >= similarity_threshold:
        feedback = "Strings are similar enough (score: {0:.2f}%). Test passed!".format(similarity_score * 100)
    else:
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "***************test_print_counting_collection tester failed!***************"
        feedback = feedback+ "\nExpected:\n" +"\033[93m"+ expected_output+"\033[0m"+"\n\n"
        feedback = feedback + "\nCaptured:\n" +"\033[93m"+  captured.out +"\033[0m"
        feedback = feedback+ "\n\033[91m" ## RED START
        feedback = feedback + f"Strings are not similar enough (score: {similarity_score})"
        feedback = feedback + "\n***********************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
    # Use sys.stdout to write out the feedback message
    if(printFeedback):
        print(feedback + "\n")
  

    assert similarity_score >= similarity_threshold, f"Strings are not similar enough (score: {similarity_score})"


def test_print_counting_collection_sorted(capsys, monkeypatch, printFeedback=True):

    input = {(82, 'Full Heal', 'Trainer'): 6, (28, 'Growlithe', 'Fire'): 3, (61, 'Rattata', 'Air'): 4, (6, 'Gyarados', 'Water'): 5,(85, 'Pokemon Center', 'Trainer'): 1}
    
    expected_output = """CARD: (82, 'Full Heal', 'Trainer') , total number of card purchased: 6
CARD: (6, 'Gyarados', 'Water') , total number of card purchased: 5
CARD: (61, 'Rattata', 'Air') , total number of card purchased: 4
CARD: (28, 'Growlithe', 'Fire') , total number of card purchased: 3
CARD: (85, 'Pokemon Center', 'Trainer') , total number of card purchased: 1"""

   
    # Execute the function
      # Run the main function
    pokemon.print_counting_collection_sorted(input)
    #Get the feedback
    captured = capsys.readouterr()

    similarity_threshold = 0.99  # Set your desired threshold here

    similarity_score = assessMeTester_StringSimilarity.string_similarity(expected_output, captured.out)

   
    if similarity_score >= similarity_threshold:
        feedback = "Strings are similar enough (score: {0:.2f}%). Test passed!".format(similarity_score * 100)
    else:
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "***************test_print_counting_collection_sorted tester failed!***************"
        feedback = feedback+ "\nExpected:\n" +"\033[93m"+ expected_output+"\033[0m"+"\n\n"
        feedback = feedback + "\nCaptured:\n" +"\033[93m"+  captured.out +"\033[0m"
        feedback = feedback+ "\n\033[91m" ## RED START
        feedback = feedback + f"Strings are not similar enough (score: {similarity_score})"
        feedback = feedback + "\n***********************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
    # Use sys.stdout to write out the feedback message
    if(printFeedback):
        print(feedback + "\n")
  

    assert similarity_score >= similarity_threshold, f"Strings are not similar enough (score: {similarity_score})"



def test_FinalGrade(capsys, monkeypatch):
    
    totalPoints = 0

    ## CALL the testers, do not print, otherwise you will mess with some of the testers
  
    test_functions = [
        (test_make_database,15),
        (test_print_database,5),
        (test_make_pack,15),
        (test_print_pack,5),
        (test_build_basic_collection,15),
        (test_average_number_of_packs_to_buy,15),
        (test_build_counting_collection,15),
        (test_print_counting_collection,5),
        (test_print_counting_collection_sorted,10)
    ]

    outputFeedbac = "############ TOTAL POINTS ###################\n"
    
    for function, point in test_functions:
        try:
            function(capsys,monkeypatch,False)
            outputFeedbac=outputFeedbac+f"PASS:{function.__name__}: {point}"+"\n"
            totalPoints += point
        except AssertionError:
            outputFeedbac=outputFeedbac+f"FAIL:{function.__name__}: {0}\n"
        
    
    print(outputFeedbac)
    print("Total points",totalPoints)
    
   # Define emoji ranges based on points
    if 90 <= totalPoints:
          emoji = "🌟✨💫💖😍🎉👏😎🥇🚀👏👏👏👏👏👏"
    elif 80 <= totalPoints < 90:
          emoji = "😃👍👌🙌🤗🥳😁👌👌👌👌"
    elif 70 <= totalPoints < 80:
          emoji = "😊😉❤️🌸🌼💝💓👌👌"
    elif 60 <= totalPoints < 70:
          emoji = "😐🤔😕😬😟😞"  # Thinking + Unamused + Disappointed
    else:
          emoji = "😢😥😭😩😖"
    print(emoji)
    assert True