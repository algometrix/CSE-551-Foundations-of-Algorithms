

women = ['1','2','3','4']
men   = ['A','B','C','D']

men_preference_list = {
     'A': ['1','2','3','4',] ,
     'B': ['2','3','4','1',] ,
     'C': ['3','4','1','2',] ,
     'D': ['4','1','3','2',] ,
}
women_preference_list = {
     '1': ['A','B','C','D',] ,
     '2': ['B','C','D','A',] ,
     '3': ['C','D','A','B',] ,
     '4': ['D','A','B','C',] ,
}

mating_matrix = {
     '1': [] ,
     '2': [] ,
     '3': [] ,
     '4': [] ,
}    

number_of_mates = len(women)

def find_highest_match_and_kick_others(woman, interested_men):
     preference_list = women_preference_list[woman]
     print(preference_list)
     for preferred_man in preference_list:
          for interested_man in interested_men:
               if preferred_man == interested_man:
                    return preferred_man

          
          




for i in range(1):
     for m in men:
          for interest in men_preference_list[m]:
               mating_matrix[interest].append(m)         

print(mating_matrix)

print(find_highest_match_and_kick_others('1',mating_matrix['1']))
